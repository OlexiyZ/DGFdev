# Generated by Django 5.0.2 on 2024-03-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0039_alter_query_query_conditions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_function',
            field=models.TextField(blank=True),
        ),
    ]
