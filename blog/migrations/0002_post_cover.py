# Generated by Django 2.0.13 on 2019-10-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(default='img_default.jpg', upload_to='images/'),
        ),
    ]
