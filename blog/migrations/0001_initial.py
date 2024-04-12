# Generated by Django 5.0.4 on 2024-04-12 16:28

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galleries', '0005_alter_category_featured_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('hidden', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(blank=True, to='galleries.image')),
            ],
        ),
    ]
