# Generated by Django 4.2.5 on 2024-04-11 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ArtPortfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='is_for_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='about',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='contact_email',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
