# Generated by Django 4.0.4 on 2022-05-10 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invertory', '0019_alter_departments_title_alter_employees_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomenclature_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField(blank=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invertory.places')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invertory.statuses')),
            ],
        ),
        migrations.DeleteModel(
            name='Amortization',
        ),
    ]
