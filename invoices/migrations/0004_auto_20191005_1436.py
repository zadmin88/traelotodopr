# Generated by Django 2.2.4 on 2019-10-05 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20190925_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payments',
        ),
        migrations.AddField(
            model_name='payments',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='invoices.Invoice'),
        ),
    ]
