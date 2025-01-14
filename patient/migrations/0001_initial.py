# Generated by Django 5.1.4 on 2025-01-14 03:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.URLField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('3rd Gender', '3rd Gender')], max_length=10, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_district', models.CharField(blank=True, max_length=100, null=True)),
                ('union_pourashava_ward', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=14)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('profession', models.CharField(blank=True, max_length=50, null=True)),
                ('height_feet', models.PositiveIntegerField(blank=True, null=True)),
                ('height_inches', models.PositiveIntegerField(blank=True, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10, null=True)),
                ('aracol_app_point', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('referral_unique_code', models.CharField(blank=True, max_length=10, null=True)),
                ('total_registration_by_refer', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('successfull_referrals', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('rewards_received', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('super_admin', 'super_admin'), ('patient', 'patient')], default='patient', max_length=20)),
                ('recently_viewed_profile', models.ManyToManyField(blank=True, related_name='viewed_by', to='doctor.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
