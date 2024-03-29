# Generated by Django 4.1.2 on 2023-07-16 13:05

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_image_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(null=True)),
                ('contents', models.TextField(null=True)),
                ('altTxt', models.TextField(blank=True, null=True)),
                ('squareImg', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='defaultS.jpg', force_format=None, keep_meta=True, quality=75, scale=None, size=[1000, 1000], upload_to='square')),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='horiImg',
        ),
        migrations.RemoveField(
            model_name='image',
            name='vertiImg',
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='puppies',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='puppies',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
