# Generated by Django 2.2.4 on 2019-08-25 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='mygalary_image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
