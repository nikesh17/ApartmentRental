# Generated by Django 4.1 on 2023-07-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0018_userpreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='location',
            field=models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Itahari', 'Itahari'), ('Butwal', 'Butwal')], max_length=100),
        ),
    ]
