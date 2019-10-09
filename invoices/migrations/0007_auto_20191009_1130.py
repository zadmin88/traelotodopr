# Generated by Django 2.2.4 on 2019-10-09 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_auto_20191007_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='shipment',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Shipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('amount', models.IntegerField()),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice')),
            ],
        ),
    ]