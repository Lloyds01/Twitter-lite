# Generated by Django 3.2.4 on 2021-07-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
