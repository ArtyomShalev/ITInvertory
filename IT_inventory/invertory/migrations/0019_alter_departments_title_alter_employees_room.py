# Generated by Django 4.0.4 on 2022-05-09 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invertory', '0018_alter_departments_title_alter_docs_type_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invertory.places'),
        ),
    ]