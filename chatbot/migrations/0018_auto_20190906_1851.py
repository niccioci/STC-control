# Generated by Django 2.2.3 on 2019-09-06 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0017_auto_20190828_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='from_notification',
        ),
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]