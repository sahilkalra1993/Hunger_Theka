# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-04 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20170602_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='Drinks',
        ),
        migrations.DeleteModel(
            name='Hotdog',
        ),
        migrations.DeleteModel(
            name='Maggi',
        ),
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.DeleteModel(
            name='Sandwich',
        ),
        migrations.DeleteModel(
            name='Shakes',
        ),
        migrations.DeleteModel(
            name='Wraps',
        ),
        migrations.AddField(
            model_name='detail',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu'),
        ),
    ]
