# Generated by Django 3.2.25 on 2024-06-20 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('password_manager_app', '0002_auto_20240621_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to=settings.AUTH_USER_MODEL),
        ),
    ]
