# Generated by Django 4.2 on 2023-04-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_accountingtable_marginarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='technicaltable',
            name='calculation',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Формула расчёта'),
        ),
    ]