# Generated by Django 5.1.2 on 2024-10-16 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Usuarios',
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='usuarios',
        ),
    ]
