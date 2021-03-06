# Generated by Django 2.1.5 on 2019-02-02 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0008_auto_20190201_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=250)),
                ('content', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', to_field='identy')),
            ],
        ),
    ]
