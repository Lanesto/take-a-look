# Generated by Django 2.2.5 on 2019-11-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191127_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='label',
            field=models.CharField(choices=[(0, 'Cat'), (1, 'Dog')], max_length=16),
        ),
        migrations.AlterField(
            model_name='history',
            name='prediction',
            field=models.CharField(choices=[(0, 'Cat'), (1, 'Dog')], max_length=16),
        ),
    ]