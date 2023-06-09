# Generated by Django 4.1.5 on 2023-04-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('change_lives_app1', '0032_alter_patient_model_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_model',
            name='image',
            field=models.ImageField(upload_to='patient_images/'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='document',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
