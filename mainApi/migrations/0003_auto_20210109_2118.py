# Generated by Django 3.1.5 on 2021-01-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApi', '0002_answer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='Images', verbose_name='Выберите своё изображение'),
        ),
    ]