# Generated by Django 4.2.4 on 2023-08-08 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lecture_img',
        ),
        migrations.RemoveField(
            model_name='post',
            name='lecture_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='platform',
        ),
    ]
