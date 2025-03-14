# Generated by Django 5.1.6 on 2025-02-16 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('field_of_study', models.CharField(max_length=50)),
                ('year_of_study', models.IntegerField()),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
