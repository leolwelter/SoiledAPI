# Generated by Django 3.1.7 on 2021-03-17 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sensors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reading',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Sensors.plant'),
            preserve_default=False,
        ),
    ]
