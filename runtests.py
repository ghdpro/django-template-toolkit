#!/usr/bin/env python

import django
from django.conf import settings
from django.core.management import call_command


def runtests():
    settings.configure()
    django.setup()
    call_command('test')


if __name__ == '__main__':
    runtests()
