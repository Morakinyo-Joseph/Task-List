# Generated by Django 4.0.1 on 2022-01-09 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Examples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('complete', models.BooleanField()),
                ('examples', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.todolist')),
            ],
        ),
    ]
