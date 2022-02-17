# Generated by Django 2.2.27 on 2022-02-09 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20220208_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_board', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='board.Column'),
        ),
    ]