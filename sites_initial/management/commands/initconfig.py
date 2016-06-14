from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Generate necessary basic config'

    def handle(self, *args, **options):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = get_random_string(50, chars)

        template = """
from .base import Base as DefaultBase

class Base(DefaultBase):
    SECRET_KEY = '{secret_key}'
"""
        f = open("xenim/settings/base_local.py", "w")
        f.write(template.format(secret_key=secret_key))

