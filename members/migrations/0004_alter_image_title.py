# Generated by Django 4.1.2 on 2023-07-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_puppies_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
