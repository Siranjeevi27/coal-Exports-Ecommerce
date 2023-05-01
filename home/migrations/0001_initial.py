# Generated by Django 4.1.3 on 2023-03-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('origin', models.CharField(choices=[('USA', 'United States'), ('AUS', 'Australia'), ('CAN', 'Canada'), ('RUS', 'Russia'), ('CHN', 'China')], max_length=100)),
                ('availability', models.BooleanField(default=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]