# Generated by Django 3.1.3 on 2021-11-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
    ]
