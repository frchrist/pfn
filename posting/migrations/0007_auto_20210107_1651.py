# Generated by Django 3.1.1 on 2021-01-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0006_auto_20210107_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='level',
            field=models.CharField(choices=[('Débutant', 'Débutant'), ('Intermédiaire', 'Intermédiaire')], max_length=13),
        ),
    ]
