# Generated by Django 3.1.4 on 2020-12-14 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walk_in_clinic', '0002_auto_20201214_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='text',
            new_name='clinic_name',
        ),
    ]
