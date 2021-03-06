# Generated by Django 3.2 on 2021-04-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdetails',
            name='phone',
            field=models.BigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='postdetails',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postdetails',
            name='status',
            field=models.CharField(choices=[('Verified', 'Verified'), ('Non Verified', 'Not Verified')], max_length=20),
        ),
    ]
