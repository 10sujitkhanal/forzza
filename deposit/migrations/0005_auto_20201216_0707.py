# Generated by Django 3.1.4 on 2020-12-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0004_auto_20201213_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='deposit_photos', verbose_name='Add image (optional)'),
        ),
    ]
