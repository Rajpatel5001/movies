# Generated by Django 4.1.7 on 2023-02-21 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('choiese', models.CharField(choices=[('ch', 'ch'), ('ok', 'ok')], default='ch', max_length=20)),
                ('date', models.DateField()),
                ('classes', models.CharField(choices=[('A', 'A'), ('b', 'b')], max_length=20)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('gender', models.CharField(choices=[('M', 'male'), ('female', 'F')], max_length=20)),
                ('storyline', models.TextField()),
                ('cast_on', models.CharField(choices=[('amazon_prime', 'amazon_prime')], max_length=50)),
            ],
        ),
    ]