from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Create groups"

    def handle(self, *args, **options):
        group_flvl, created_flvl = Group.objects.get_or_create(name='first_level')
        group_slvl, created_slvl = Group.objects.get_or_create(name='second_level')
