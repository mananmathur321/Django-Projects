# Generated by Django 4.0.6 on 2022-08-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=70)),
                ('pno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=70)),
                ('pwd', models.CharField(max_length=70)),
            ],
        ),
    ]
