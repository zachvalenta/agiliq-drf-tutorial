# Generated by Django 2.0.4 on 2018-04-29 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180428_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='choice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice'),
        ),
    ]
