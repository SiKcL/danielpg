# Generated by Django 5.0.7 on 2024-07-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('fono', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('personas', models.PositiveIntegerField()),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO_ASISTEN', 'No Asisten')], default='RESERVADO', max_length=10)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
