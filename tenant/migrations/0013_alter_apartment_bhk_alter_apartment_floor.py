# Generated by Django 4.1 on 2023-06-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0012_remove_apartment_is_available_apartment_bhk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='bhk',
            field=models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK')], max_length=100),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.CharField(choices=[('Ground', 'Ground'), ('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Forth', 'Forth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('Seventh', 'Seventh'), ('Eighth', 'Eighth'), ('Nineth', 'Nineth'), ('Tenth', 'Tenth')], max_length=100),
        ),
    ]
