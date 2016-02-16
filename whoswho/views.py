from django.conf import settings
from django.shortcuts import redirect

from decorators import render_to
import hashlib

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context import RequestContext
from django.db.models import Count, Min, Sum, Avg

from taggit.models import Tag

from .forms import *
from .models import *
from .helper import VCard


def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)

@render_to('home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('addressbook_index')
    return context()

@login_required
def add_group(request):

    if request.method == "GET":
        form = ContactGroupForm()
    else:
        group = ContactGroup()
        form = ContactGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            # request.user.message_set.create(message = 'Successfully saved group.')
            return HttpResponseRedirect(reverse('addressbook_index'))
    return render(
        request, 'add_group.html',
        RequestContext(request, {'form': form})
    )


@login_required
def add_contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        contact_form = ContactForm(request.POST, user=request.user)  # A form bound to the POST data
        # Create a formset from the submitted data
        email_formset = EmailFormSet(request.POST, prefix="email")
        phone_formset = PhoneFormSet(request.POST, prefix="phone")
        address_formset = AddressFormSet(request.POST, prefix="address")
        if contact_form.is_valid() and email_formset.is_valid() and phone_formset.is_valid() and address_formset.is_valid():
            contact = contact_form.save()
            for form in email_formset.forms:
                email = form.save(commit=False)
                email.contact = contact
                email.save()
            for form in phone_formset.forms:
                phone = form.save(commit=False)
                phone.contact = contact
                phone.save()
            for form in address_formset.forms:
                address = form.save(commit=False)
                address.contact = contact
                address.save()
            # request.user.message_set.create(message = 'Successfully saved contact.')
            return HttpResponseRedirect(reverse('addressbook_index'))  # Redirect to a 'success' page
    else:
        groups = ContactGroup.objects.all()
        if not groups:
            return HttpResponseRedirect(reverse('addressbook_add_group'))
        contact_form = ContactForm(user=request.user)
        email_formset = EmailFormSet(prefix="email")
        phone_formset = PhoneFormSet(prefix="phone")
        address_formset = AddressFormSet(prefix="address")
    return render(
        request, 'add_contact.html',
        RequestContext(request, {
            'phone_formset': phone_formset,
            'contact_form': contact_form,
            'email_formset': email_formset,
            'address_formset': address_formset,
        }))


@login_required
def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    #if contact.group.user != request.user:
    #    return HttpResponse(contact.group.user.username + request.user.username)
        #raise Http404
    if request.method == "POST":
        contact_form = ContactForm(request.POST, instance=contact, user=request.user)
        phone_formset = PhoneEditFormSet(request.POST, instance=contact, prefix="phone")
        address_formset = AddressEditFormSet(request.POST, instance=contact, prefix="address")
        email_formset = EmailEditFormSet(request.POST, instance=contact, prefix="email")
        if (
            contact_form.is_valid() and
            phone_formset.is_valid() and
            address_formset.is_valid() and
            email_formset.is_valid()
        ):
            contact_form.save()
            email_formset.save()
            address_formset.save()
            phone_formset.save()
            return HttpResponseRedirect(reverse('addressbook_index'))
    else:
        contact_form = ContactForm(instance=contact, user=request.user)
        phone_formset = PhoneEditFormSet(instance=contact, prefix="phone")
        address_formset = AddressEditFormSet(instance=contact, prefix="address")
        email_formset = EmailEditFormSet(instance=contact, prefix="email")
    return render(
        request, 'edit_contact.html',
        RequestContext(request, {
            'email_formset': email_formset,
            'phone_formset': phone_formset,
            'address_formset': address_formset,
            'contact_form': contact_form,
            'contact': contact,
        }))


@login_required
def index(request):

    groups = ContactGroup.objects.all()
    tags = Tag.objects.all()
    events = Event.objects.all()
    contacts = Contact.objects.all()

    if request.GET.get('tag'):
        name = request.GET['tag']
        contacts = contacts.filter(tags__name=name)
    if request.GET.get('event'):
        name = request.GET['event']
        contacts = contacts.filter(events__event__name=name)
        #contacts = Contact.objects.filter(attendance_set__contact__name=name)
        #contacts = Contact.objects.filter(events__name=name)
    if request.GET.get('group'):
        name = request.GET['group']
        contacts = contacts.filter(groups__name=name)

    totals = contacts.values('sex').annotate(count=Count('sex')).order_by('sex')
    SEX_DICT = dict(SEX_CHOICES)
    for total in totals:
        total['sex'] = dict(SEX_CHOICES).get(total['sex'], total['sex'])

    return render(
        request, 'index.html',
        {
            'totals': totals,
            'contacts': contacts,
            'groups': groups,
            'tags': tags,
            'events': events,
        })


def get_hash(str):
    str = str.lower().strip()
    md5 = hashlib.md5()
    md5.update(str)
    return md5.hexdigest()


@login_required
def single_contact(request, pk):
    groups = ContactGroup.objects.all()
    tags = Tag.objects.all()
    events = Event.objects.all()
    contact = Contact.objects.get(pk=pk)

    contact_card = {
        'full_name': "%s: %s" % (contact.id, contact.full_name()),
        'phone_number': contact.phone,
        'email': contact.email,
        # FIXME: no username? 'url': reverse('app:detail', kwargs={'username': contact.username}),
        'company': contact.organization,
    }

    if request.method == "GET":
        emails = Email.objects.filter(contact=contact)
        email_hash = ''
        if emails:
            email = emails[0]
            email_hash = get_hash(email.email)

        # FIXME is email required?
        #addresses = Address.objects.filter(contact=contact)
        #if addresses:
        #    address = addresses[0]
        #phones = PhoneNumber.objects.filter(contact=contact)
        return render(
            request, 'single_contact.html',
            RequestContext(request, {
                'contact': contact,
                'emails': emails,
                'hash': email_hash,
                #'addresses': addresses,
                #'phones': phones,
                #'vcard_str': str(VCard(contact_card)),
                'groups': groups,
                'tags': tags,
                'events': events,
            }))

    elif request.method == "POST":
        #FIXME: allow delete?
	#contact.delete()
        return HttpResponseRedirect(reverse('addressbook_index'))
    else:
        raise Http404

@login_required
def download_vcard(request, vcard=VCard):
    """
    View function for returning single vcard
    """
    pk = request.GET.get('id')
    contact = Contact.objects.get(pk=pk)
    output = vcard(contact).output_string()
    filename = "contact_%s%s.vcf" % (contact.first_name, contact.last_name)
    response = HttpResponse(output, content_type="text/x-vCard")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response
