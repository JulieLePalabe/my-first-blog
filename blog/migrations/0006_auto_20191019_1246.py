# Generated by Django 2.0.13 on 2019-10-19 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='img_article',
            field=models.ImageField(default='img_article/imgdef.jpg', upload_to='img_article/'),
        ),
        migrations.AddField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
