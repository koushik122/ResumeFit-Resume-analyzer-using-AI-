# Generated by Django 5.1.3 on 2025-01-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_desc', models.TextField()),
                ('resume_file', models.FileField(upload_to='')),
            ],
        ),
    ]
