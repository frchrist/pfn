# Generated by Django 3.1.6 on 2021-02-03 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0012_auto_20210203_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replaytocomment',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.commentaire', verbose_name='commentaire'),
        ),
    ]