# Generated by Django 3.0.7 on 2020-08-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='publication_date'),
        ),
    ]
