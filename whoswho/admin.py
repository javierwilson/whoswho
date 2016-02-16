from django.contrib import admin
from django import forms

from taggit_labels.widgets import LabelWidget
from taggit.forms import TagField
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin, ImportExportMixin

from .models import *

class ContactResource(resources.ModelResource):
    organization = fields.Field(column_name='organization', attribute='organization', widget=ForeignKeyWidget(Organization, 'name'))
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

class EventInline(admin.TabularInline):
    #model = Contact.events.through
    model = Attendance
    extra = 0
    raw_id_fields = ('contact',)
    related_lookup_fields = {
        'fk': ['contact'],
    }



class OrganizationAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ['name']
    class Meta:
        skip_unchanged = True

#class ContactForm(forms.ModelForm):
#    tags = TagField(required=False, widget=LabelWidget)

class ContactAdmin(ImportExportMixin, admin.ModelAdmin):


    resource_class = ContactResource

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
            'monitor',
            'sex',
            'organization',
            'country',
            'state',
            'municipality',
            'events__event',
            #('country', admin.RelatedOnlyFieldListFilter),
            ]
    search_fields = ['first_name', 'last_name', 'organization__name', 'state']
    list_display = ('first_name', 'last_name', 'sex', 'country', 'organization', 'state', 'municipality', 'community', 'phone_personal')


class EventAdmin(ImportExportMixin, admin.ModelAdmin):

    def sex_totals(self, obj):
        men = obj.attendance_set.filter(contact__sex='M').count()
        women = obj.attendance_set.filter(contact__sex='W').count()
        unk = obj.attendance_set.filter(contact__sex='').count()
        total = obj.attendance_set.all().count()
        return ("Men: %s Women: %s Total: %s: Error: %s" % (men, women, total, unk))

    #list_display = ('name', 'place', 'start', 'sex_totals')
    list_display = ('name', 'place', 'start', 'men', 'women', 'total')
    list_filter = [
            'start',
    ]
    inlines = [
        EventInline,
    ]

class AttendanceAdmin(admin.ModelAdmin):
    raw_id_fields = ('contact',)
    related_lookup_fields = {
        'fk': ['contact'],
    }


admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Organization, OrganizationAdmin)

admin.site.register(ContactGroup, admin.ModelAdmin)
#admin.site.register(PhoneNumber, admin.ModelAdmin)
#admin.site.register(Website, admin.ModelAdmin)
#admin.site.register(SocialNetwork, admin.ModelAdmin)
#admin.site.register(Email, admin.ModelAdmin)
#admin.site.register(Address, admin.ModelAdmin)
admin.site.register(AttendeeType, admin.ModelAdmin)
admin.site.register(Profession, admin.ModelAdmin)
admin.site.register(Monitor, admin.ModelAdmin)
