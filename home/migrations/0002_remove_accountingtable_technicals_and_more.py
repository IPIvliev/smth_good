# Generated by Django 4.2 on 2023-04-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountingtable',
            name='technicals',
        ),
        migrations.AddField(
            model_name='technicaltable',
            name='accounts',
            field=models.ManyToManyField(blank=True, related_name='tech_tables', through='home.ConnectionTechAccount', to='home.accountingtable'),
        ),
    ]
