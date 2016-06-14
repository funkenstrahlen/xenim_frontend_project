# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_initials(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.bulk_create([
        Site(domain="streams.xenim.de", name="streams.xenim.de", pk=1),
        Site(domain="xsn.io", name="xsn.io", pk=4),
        Site(domain="feeds.streams.xenim.de", name="feeds.streams.xenim.de", pk=5),
        Site(domain="dashboard.xenim.de", name="dashboard.xenim.de", pk=6),
        Site(domain="review.streams.xenim.de", name="review.streams.xenim.de", pk=7),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initials, migrations.RunPython.noop),
    ]
