# Generated by Django 3.1.1 on 2021-01-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0009_auto_20210111_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('Publier', 'publier'), ('Corbeille', 'corbeille')], default='corbeille', max_length=13),
        ),
    ]