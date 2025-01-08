# Generated by Django 5.1.4 on 2025-01-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_alter_medicine_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='description',
            field=models.CharField(default='default', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicine',
            name='image',
            field=models.URLField(default='default', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]