# Generated by Django 2.2.5 on 2019-10-08 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Please',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailplus', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]
