# Generated by Django 3.2.5 on 2021-07-14 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addbook', '0004_auto_20210714_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log_in',
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='log_in',
            old_name='password',
            new_name='passwords',
        ),
    ]