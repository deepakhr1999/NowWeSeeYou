# Generated by Django 2.1.2 on 2019-01-12 19:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='next_class',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
