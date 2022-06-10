# Generated by Django 2.2.27 on 2022-04-16 16:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fehler_auth', '0002_auto_20211002_1511'),
        ('spaces', '0004_auto_20211115_0957'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spacemembership',
            unique_together={('space', 'member', 'invite')},
        ),
    ]