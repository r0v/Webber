# Generated by Django 2.1.4 on 2018-12-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181224_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='gender',
            field=models.BooleanField(choices=[(False, 'Kobieta'), (True, 'Mężczyzna')], default=(False, 'Kobieta')),
        ),
    ]
