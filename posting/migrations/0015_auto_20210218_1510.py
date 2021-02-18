# Generated by Django 3.1.6 on 2021-02-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0014_auto_20210203_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='also_send',
            new_name='notify_users',
        ),
        migrations.AddField(
            model_name='course',
            name='notify_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='replaytocomment',
            name='replay_content',
            field=models.TextField(verbose_name=''),
        ),
    ]
