# Generated by Django 5.0.6 on 2024-06-08 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0007_cliente_tipoinmueble_alter_propiedad_imagen_inmueble'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='propiedades.region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades.comuna'),
        ),
    ]