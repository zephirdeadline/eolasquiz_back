# Generated by Django 2.1.2 on 2018-10-29 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20181024_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniq_id', models.CharField(max_length=64)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='quiz',
            name='created_at',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Quiz'),
        ),
    ]
