# Generated by Django 2.1.3 on 2019-02-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20190221_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
