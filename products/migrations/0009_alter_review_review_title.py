# Generated by Django 3.2 on 2022-06-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_title',
            field=models.TextField(max_length=100),
        ),
    ]
