# Generated by Django 5.0.1 on 2024-02-18 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0021_remove_field_field_list_id_field_field_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.fieldlist'),
        ),
    ]
