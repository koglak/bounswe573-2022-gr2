# Generated by Django 3.2.12 on 2022-04-08 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_remove_course_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]