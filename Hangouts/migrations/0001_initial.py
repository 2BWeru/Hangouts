# Generated by Django 4.0.5 on 2022-07-11 20:57

import Hangouts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('fname', models.CharField(max_length=30)),
                ('bio', models.TextField(max_length=300)),
                ('instagram_acc', models.CharField(max_length=200)),
                ('facebook_acc', models.CharField(max_length=200)),
                ('idNo', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to=Hangouts.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=1000)),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='postSite')),
                ('date', models.DateField(auto_now_add=True)),
                ('Location', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviews', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site', to='Hangouts.site')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
                ('post', models.ImageField(blank=True, default='', null=True, upload_to='post')),
                ('date', models.DateField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hangouts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=1000)),
                ('due_date', models.DateTimeField()),
                ('photo', models.ImageField(blank=True, default='', null=True, upload_to='postEvent')),
                ('Location', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filter', to='Hangouts.category')),
            ],
        ),
    ]
