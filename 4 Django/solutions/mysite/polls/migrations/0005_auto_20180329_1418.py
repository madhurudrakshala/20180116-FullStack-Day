# Generated by Django 2.0.3 on 2018-03-29 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180328_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='test_models',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]