# Generated by Django 3.2.4 on 2021-06-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='email',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
