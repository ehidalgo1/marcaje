# Generated by Django 3.0 on 2020-03-05 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Marcaje', '0004_auto_20200305_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='token',
        ),
        migrations.AlterField(
            model_name='marcaje',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Marcaje.Usuario'),
        ),
    ]