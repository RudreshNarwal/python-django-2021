# Generated by Django 4.1.2 on 2022-10-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20220626_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='logo.png', null=True, upload_to=''),
        ),
    ]
