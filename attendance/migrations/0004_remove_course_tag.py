# Generated by Django 2.1.2 on 2019-01-12 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_course_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='tag',
        ),
    ]
