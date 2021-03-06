# Generated by Django 3.1.3 on 2020-11-30 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_amount', models.CharField(db_index=True, max_length=150)),
                ('frozza_username', models.SlugField(blank=True, max_length=150, null=True)),
                ('review', models.TextField(blank=True, max_length=5000, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='deposit_photos/', verbose_name='Add image (optional)')),
                ('status', models.BooleanField(db_index=True, default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
