# Generated by Django 4.1 on 2023-06-07 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_alter_book_apartment_id_alter_rent_apartment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
