# Generated by Django 4.1.6 on 2023-07-11 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mental', '0004_awareness'),
    ]

    operations = [
        migrations.AddField(
            model_name='awareness',
            name='meditation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mental.meditation'),
            preserve_default=False,
        ),
    ]
