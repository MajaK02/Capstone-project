# Generated by Django 4.2.17 on 2025-01-22 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on', 'author']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on', 'author']},
        ),
    ]
