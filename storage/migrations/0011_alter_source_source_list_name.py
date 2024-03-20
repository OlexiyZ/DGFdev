# Generated by Django 5.0.1 on 2024-02-10 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storage", "0010_alter_query_field_list_id_alter_query_source_list_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="source",
            name="source_list_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="storage.sourcelist"
            ),
        ),
    ]
