# Generated by Django 2.1.4 on 2018-12-28 13:27

from __future__ import unicode_literals
from django.db import models, migrations

def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "category")

def delete_stores(apps, schema_editor):
    Store = apps.get_model("blog", "Category")
    Store.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_stores_from_fixture,delete_stores),
    ]
