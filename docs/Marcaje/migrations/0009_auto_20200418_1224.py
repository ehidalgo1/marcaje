# Generated by Django 3.0 on 2020-04-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marcaje', '0008_remove_marcaje_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcaje',
            name='salida',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
