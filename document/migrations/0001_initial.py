# Generated by Django 5.0.4 on 2024-04-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_image', models.CharField(max_length=200)),
                ('doc_title', models.CharField(max_length=150)),
            ],
        ),
    ]
