# Generated by Django 2.2.13 on 2021-10-19 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spaces", "0002_auto_20211019_1331"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spacemembership",
            name="invite",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="fehler_auth.Invite",
            ),
        ),
    ]