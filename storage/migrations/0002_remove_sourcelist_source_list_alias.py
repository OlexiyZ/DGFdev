# Generated by Django 5.0.1 on 2024-02-10 16:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sourcelist",
            name="source_list_alias",
        ),
    ]
