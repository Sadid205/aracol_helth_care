# Generated by Django 5.1.4 on 2025-01-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('super_admin', 'super_admin'), ('patient', 'patient')], default='patient', max_length=20),
        ),
    ]