# Generated by Django 3.1.6 on 2021-03-02 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
    ]
