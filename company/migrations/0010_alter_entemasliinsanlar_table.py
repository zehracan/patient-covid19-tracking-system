# Generated by Django 4.0 on 2022-01-03 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_temaslikisi_alter_covid_temasli'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='entemasliinsanlar',
            table='temaslikisiler',
        ),
    ]