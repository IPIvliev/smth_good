# Generated by Django 4.2 on 2023-04-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_technicaltable_calculation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingtable',
            name='application',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accountingtable',
            name='contractor',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accountingtable',
            name='nomenclature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accountingtable',
            name='payment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
