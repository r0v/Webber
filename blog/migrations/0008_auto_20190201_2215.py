# Generated by Django 2.1.5 on 2019-02-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190109_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to='post/%Y/%m/%D/'),
        ),
    ]