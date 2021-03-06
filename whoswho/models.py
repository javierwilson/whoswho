from django.conf import settings
from django.core.files.storage import get_storage_class
from django.db import models
from django.utils.functional import LazyObject
from django.utils.translation import ugettext as _

from easy_thumbnails.fields import ThumbnailerImageField
from django_countries.fields import CountryField
from taggit_autosuggest.managers import TaggableManager
#from taggit.managers import TaggableManager


class AvatarStorage(LazyObject):
    def _setup(self):
        AVATAR_FILE_STORAGE = getattr(settings, 'AVATAR_FILE_STORAGE', settings.DEFAULT_FILE_STORAGE)
        self._wrapped = get_storage_class(AVATAR_FILE_STORAGE)()

avatar_storage = AvatarStorage()

EDUCATION_CHOICES = (
    ('P', _('Primaria')),
    ('S', _('Secundaria')),
    ('U', _('Universitaria')),
    ('O', _('--')),
)

SEX_CHOICES = (
    ('M', _('Man')),
    ('F', _('Woman')),
    ('O', _('--')),
)

ADR_TYPES = (
    ('Home', 'Home'),
    ('Work', 'Work'),
)

TEL_TYPES = (
    ('Mobile', 'Mobile'),
    ('Mobile Work', 'Mobile Work'),
    ('Work', 'Work'),
    ('Fax', 'Fax'),
    ('Skype', 'Skype'),
)

EMAIL_TYPES = (
    ('Home', 'Home'),
    ('Work', 'Work'),
)

WEBSITE_TYPES = (
    ('Work', 'Work'),
    ('Personal', 'Personal'),
    ('Portfolio', 'Portfolio'),
    ('Blog', 'Blog'),
)

SOCNET_TYPES = (
    ('Skype', 'Skype'),
    ('Twitter', 'Twitter'),
    ('LinkedIn', 'LinkedIn'),
    ('Facebook', 'Facebook'),
    ('Pinterest', 'Pinterest'),
)

social_net_prefixes = dict(
    Skype='skype:',
    Twitter='https://twitter.com/',
    LinkedIn='http://linkedin.com/',
    Facebook='http://www.facebook.com/',
    Pinterest='http://www.pinterest.com/',
)


class Profession(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Name'))

    class Meta:
        ordering = ['name']
        verbose_name = _("Profession")
        verbose_name_plural = _("Profession")

    def __unicode__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Name'))
    country = CountryField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __unicode__(self):
        return "%s %s" % (self.name, self.country)


class ContactGroup(models.Model):
    name = models.CharField(max_length=40, verbose_name='Group Name', unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Monitor(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Contact(models.Model):
    groups = models.ManyToManyField(ContactGroup, blank=True)
    last_name = models.CharField(max_length=80, blank=False)
    first_name = models.CharField(max_length=80, blank=False)
    middle_name = models.CharField(max_length=40, blank=True)
    title = models.CharField(max_length=40, blank=True)
    sex = models.CharField(max_length=1, null=True, choices=SEX_CHOICES)
    organization = models.ForeignKey(Organization, null=True, blank=True)
    #organization_custom = models.CharField(max_length=100, null=True, blank=True)
    profession = models.ForeignKey(Profession, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    blurb = models.TextField(null=True, blank=True)
    profile_image = ThumbnailerImageField(upload_to="profile_images/", blank=True, null=True)
    qr_image = models.ImageField(upload_to="qr_images/", blank=True, null=True)
    twitter_handle = models.CharField(max_length=50, blank=True, null=True)
    worked_with = models.ManyToManyField('self', blank=True)
    tags = TaggableManager(blank=True)
    #events = models.ManyToManyField('Event', through='Attendance')

    # new fields to make my life simpler
    phone_work = models.CharField(max_length=20, null=True, blank=True)
    phone_personal = models.CharField(max_length=20, null=True, blank=True)
    email_work = models.EmailField(null=True, blank=True)
    email_personal = models.EmailField(null=True, blank=True)

    # address
    street = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    municipality = models.CharField(max_length=40, null=True, blank=True)
    community = models.CharField(max_length=40, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)

    # finca
    area_mz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    area_productiva_mz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    area_desarrollo_mz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # extra
    women_home = models.IntegerField(null=True, blank=True)
    men_home = models.IntegerField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    age = models.IntegerField(null=True, blank=True, verbose_name="Age")
    education = models.CharField(max_length=1, null=True, blank=True, choices=EDUCATION_CHOICES)
    education_custom = models.CharField(max_length=100, null=True, blank=True)
    document = models.CharField(max_length=40, null=True, blank=True)

    # control
    ref = models.IntegerField(null=True, blank=True, verbose_name="Reference")
    modified = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    monitor = models.ForeignKey(Monitor, null=True, blank=True)

    class Meta:
        unique_together = (('first_name', 'last_name'),)
        ordering = ['first_name', 'last_name']

    def email(self):
        if self.email_work:
            return email_work
        else:
            return email_personal

    def phone(self):
        if self.phone_work:
            return phone_work
        else:
            return phone_personal

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return "%s %s (%s): %s %s" % (self.first_name, self.last_name, self.sex, self.country, self.organization)

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.profile_image.storage = avatar_storage
        self.profile_image.thumbnail_storage = avatar_storage


class Event(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Name'))
    title = models.CharField(max_length=400, null=True, blank=True, verbose_name=_('Title'))
    organizer = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Organizer'))
    #activities = models.ManyToManyField('Activity', blank=True, verbose_name=_('Activities'))
    text = models.TextField(blank=True,)
    start = models.DateTimeField(blank=True, null=True, verbose_name=_('Start'))
    end = models.DateTimeField(blank=True, null=True, verbose_name=_('End'))
    place = models.CharField(max_length=200, null=True, blank=True, verbose_name=_('Place'))
    monitor = models.BooleanField(default=False)

    class Meta:
        ordering = ['start', 'name']

    def __unicode__(self):
        return "%s %s" % (self.name, self.start, )

    def _women(self):
        women = self.attendance_set.filter(contact__sex='F').count()
        return women
    _women.short_description = _('Women')
    _women.integer = True
    women = property(_women)

    def _men(self):
        men = self.attendance_set.filter(contact__sex='M').count()
        return men
    _men.short_description = _('Men')
    men = property(_men)

    def _total(self):
        total = self.attendance_set.all().count()
        return total
    _total.short_description = _('Total')
    total = property(_total)


class AttendeeType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Name'))

    class Meta:
        ordering = ['name']
        verbose_name = _("Attendee Type")
        verbose_name_plural = _("Attendee Types")

    def __unicode__(self):
        return self.name


class Attendance(models.Model):
    contact = models.ForeignKey(Contact, related_name='events')
    event = models.ForeignKey(Event)
    date = models.DateField(null=True, blank=True)
    type = models.ForeignKey(AttendeeType, null=True, blank=True)

    class Meta:
        unique_together = ('contact', 'event')
    def __unicode__(self):
        return self.event.name


class Address(models.Model):
    contact = models.ForeignKey(Contact)
    street = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = CountryField()
    zip = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=20, choices=ADR_TYPES)
    public_visible = models.BooleanField(default=False)
    contact_visible = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s %s: %s %s, %s, %s' % (
            self.contact.first_name,
            self.contact.last_name,
            self.street,
            self.city,
            self.state,
            self.country
        )


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TEL_TYPES)
    public_visible = models.BooleanField(default=False)
    contact_visible = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s: %s" % (self.contact.first_name, self.contact.last_name, self.phone)


class Email(models.Model):
    contact = models.ForeignKey(Contact)
    email = models.EmailField()
    type = models.CharField(max_length=20, choices=EMAIL_TYPES)
    public_visible = models.BooleanField(default=False)
    contact_visible = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s: %s" % (self.contact.first_name, self.contact.last_name, self.email)


class Website(models.Model):
    contact = models.ForeignKey(Contact)
    website = models.URLField(blank=True)
    type = models.CharField(max_length=20, choices=WEBSITE_TYPES)
    public_visible = models.BooleanField(default=False)
    contact_visible = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s: %s" % (self.contact.first_name, self.type, self.website)


class SocialNetwork(models.Model):
    contact = models.ForeignKey(Contact)
    handle = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=SOCNET_TYPES)
    public_visible = models.BooleanField(default=False)
    contact_visible = models.BooleanField(default=False)

    @property
    def url(self):
        prefixes = social_net_prefixes
        prefix = getattr(settings, '%s_PREFIX' % self.type.upper(), prefixes[self.type])
        return '%s%s' % (prefix, self.handle)

    def __unicode__(self):
        return "%s %s: %s" % (self.contact.first_name, self.type, self.handle)
