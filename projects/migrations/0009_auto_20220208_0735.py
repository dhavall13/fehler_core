# Generated by Django 2.2.26 on 2022-02-08 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_auto_20220207_1714"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="column",
            name="board",
        ),
        migrations.RemoveField(
            model_name="column",
            name="tasks",
        ),
        migrations.RemoveField(
            model_name="label",
            name="board",
        ),
        migrations.RemoveField(
            model_name="task",
            name="assignee",
        ),
        migrations.RemoveField(
            model_name="task",
            name="project",
        ),
        migrations.RemoveField(
            model_name="task",
            name="reporter",
        ),
        migrations.DeleteModel(
            name="Board",
        ),
        migrations.DeleteModel(
            name="Column",
        ),
        migrations.DeleteModel(
            name="Label",
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]
