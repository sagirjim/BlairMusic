# Generated by Django 3.1.7 on 2021-05-13 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientesapp', '0004_auto_20210513_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orden',
            old_name='clientes',
            new_name='client',
        ),
    ]
