# Generated by Django 4.1.2 on 2023-07-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_puppies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puppies',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
