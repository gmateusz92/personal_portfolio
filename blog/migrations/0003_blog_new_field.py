# Generated by Django 4.1.1 on 2022-09-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_project_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='new_field',
            field=models.CharField(max_length=140, null=True),
        ),
    ]