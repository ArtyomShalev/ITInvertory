# Generated by Django 4.0.4 on 2022-05-01 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invertory', '0012_alter_registry_document_delete_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomenclature',
            name='place',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
