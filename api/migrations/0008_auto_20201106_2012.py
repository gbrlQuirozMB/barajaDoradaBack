# Generated by Django 2.2.16 on 2020-11-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20201106_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carta',
            name='imagen',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, default=0, null=True, upload_to=''),
        ),
    ]
