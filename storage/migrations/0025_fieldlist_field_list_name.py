# Generated by Django 5.0.1 on 2024-02-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0024_remove_fieldlist_data_source_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldlist',
            name='field_list_name',
            field=models.CharField(default='FL_CDC_WITH', max_length=255),
        ),
    ]
