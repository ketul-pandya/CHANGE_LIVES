# Generated by Django 4.1.5 on 2023-03-20 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_lives_app1', '0006_remove_registration_registration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='confirm_password',
        ),
        migrations.AddField(
            model_name='registration',
            name='author_name',
            field=models.CharField(default='author', max_length=100),
            preserve_default=False,
        ),
    ]
