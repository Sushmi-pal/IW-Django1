# Generated by Django 3.0.8 on 2020-07-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogview',
            name='blogs',
            field=models.TextField(null=True),
        ),
    ]