# Generated by Django 5.1.3 on 2024-12-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_tarefa_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='prazo',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
