# Generated by Django 3.0.7 on 2020-08-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(null=True, verbose_name='publication_date'),
        ),
    ]