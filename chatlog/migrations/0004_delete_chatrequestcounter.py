# Generated by Django 4.2.3 on 2023-08-02 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatlog', '0003_chatrequestcounter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatRequestCounter',
        ),
    ]
