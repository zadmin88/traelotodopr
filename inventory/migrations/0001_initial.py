# Generated by Django 2.2.4 on 2019-09-23 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
