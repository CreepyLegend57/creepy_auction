# Generated by Django 4.2.1 on 2023-05-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_remove_auctionitems_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitems',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='pictures/'),
        ),
    ]
