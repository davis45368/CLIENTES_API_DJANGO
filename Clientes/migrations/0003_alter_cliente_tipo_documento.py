# Generated by Django 4.2.4 on 2023-08-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0002_alter_cliente_numero_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='tipo_documento',
            field=models.CharField(choices=[('NIT', 'Cedula'), ('CC', 'Nit')], max_length=50, null=True),
        ),
    ]
