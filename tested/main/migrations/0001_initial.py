# Generated by Django 5.0.6 on 2024-07-03 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('session', models.TextField()),
                ('company', models.TextField()),
                ('login', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]
