# Generated by Django 3.1.4 on 2020-12-26 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201226_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='api.group'),
        ),
    ]
