# Generated by Django 3.0 on 2021-04-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210414_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]