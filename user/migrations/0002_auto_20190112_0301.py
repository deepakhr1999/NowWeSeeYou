# Generated by Django 2.1.2 on 2019-01-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='branch',
            field=models.CharField(blank=True, choices=[('CSE', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering')], max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rollno',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]