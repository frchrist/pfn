# Generated by Django 3.1.6 on 2021-03-19 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='quize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quize.quize'),
        ),
    ]