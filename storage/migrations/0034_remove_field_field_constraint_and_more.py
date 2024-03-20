# Generated by Django 5.0.2 on 2024-02-18 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0033_alter_source_source_type_field_field_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='field',
            name='field_constraint',
        ),
        migrations.AlterField(
            model_name='field',
            name='field_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.source'),
        ),
        migrations.AlterField(
            model_name='field',
            name='source_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.sourcelist'),
        ),
        migrations.AddConstraint(
            model_name='field',
            constraint=models.UniqueConstraint(fields=('field_list', 'field_alias'), name='field_constraint'),
        ),
    ]