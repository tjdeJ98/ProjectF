# Generated by Django 5.0.4 on 2024-04-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_image_capture_date_image_photographer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date published'),
        ),
    ]
