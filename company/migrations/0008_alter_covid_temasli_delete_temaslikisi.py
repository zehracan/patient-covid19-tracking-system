# Generated by Django 4.0 on 2022-01-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_temaslikisiler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid',
            name='temasli',
            field=models.ManyToManyField(blank=True, to='company.TemasliKisiler'),
        ),
        migrations.DeleteModel(
            name='TemasliKisi',
        ),
    ]
