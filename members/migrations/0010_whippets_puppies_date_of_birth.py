# Generated by Django 4.1.2 on 2023-07-17 10:29

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_remove_news_squareimg_news_horiimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whippets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('altTxt', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('squareImg', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='squareDefault.png', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='square')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='puppies',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
