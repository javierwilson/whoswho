from django.contrib import admin
from django import forms

from taggit_labels.widgets import LabelWidget
from taggit.forms import TagField
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

from .models import *

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class SocialInline(admin.TabularInline):
    model = SocialNetwork
    extra = 0

class WebsiteInline(admin.TabularInline):
    model = Website
    extra = 0

class PhoneInline(admin.TabularInline):
    model = PhoneNumber
    extra = 0

class EmailInline(admin.TabularInline):
    model = Email
    extra = 0

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

class EventInline(admin.StackedInline):
    #model = Contact.events.through
    model = Attendance
    extra = 0



#class ContactForm(forms.ModelForm):
#    tags = TagField(required=False, widget=LabelWidget)

class ContactAdmin(ImportExportMixin, admin.ModelAdmin):

    #formfield_overrides = {
    #    TagField: {'widget': LabelWidget}
    #}

    inlines = [
        AddressInline,
        EmailInline,
        PhoneInline,
        SocialInline,
        WebsiteInline,
        EventInline,
    ]

    list_filter = [
            #'event_set.name',
            'organization',
            'country',
            #('country', admin.RelatedOnlyFieldListFilter),
            ]
    search_fields = ['first_name', 'last_name', 'organization']
    list_display = ('first_name', 'last_name', 'country', 'organization')


class EventAdmin(admin.ModelAdmin):

    list_display = ('name', 'place', 'start')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)

admin.site.register(ContactGroup, admin.ModelAdmin)
admin.site.register(PhoneNumber, admin.ModelAdmin)
admin.site.register(Website, admin.ModelAdmin)
admin.site.register(SocialNetwork, admin.ModelAdmin)
admin.site.register(Email, admin.ModelAdmin)
admin.site.register(Address, admin.ModelAdmin)
admin.site.register(Organization, admin.ModelAdmin)
admin.site.register(AttendeeType, admin.ModelAdmin)
admin.site.register(Profession, admin.ModelAdmin)
