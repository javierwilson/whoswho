from os.path import isfile
from django.core.management.base import BaseCommand, CommandError
from addressbook.models import Contact, ContactGroup, PhoneNumber, SocialNetwork, Email
import csv

class Command(BaseCommand):
    help = 'Imports CSV data'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=file)

    def handle(self, *args, **options):
        for afile in options['file']:
            self.import_file(afile)
            self.stdout.write('Successfully closed file "%s"' % afile)

    def import_file(self, afile):
        reader = csv.reader(afile)
        for row in reader:
            print row
            (first_name, last_name) = row[0].split(' ', 1)
            _, created = Contact.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                title=row[1],
            )
            print created
            phonenumber, created = PhoneNumber.objects.get_or_create(contact=_,  phone = row[2])
            email, created = Email.objects.get_or_create(contact=_, email =
row[3], )
            socialnetwork, created = SocialNetwork.objects.get_or_create(contact=_, handle = row[4], type = 'FooNetwork')
            Foo, created = ContactGroup.objects.get_or_create(name=row[5])
            Bar, created = ContactGroup.objects.get_or_create(name='Bar')
            _.groups.add(Foo)
            _.groups.add(Bar)
