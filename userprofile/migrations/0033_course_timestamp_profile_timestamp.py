# Generated by Django 4.0.4 on 2022-12-12 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0032_alter_course_description_alter_event_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
