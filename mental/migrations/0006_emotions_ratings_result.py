# Generated by Django 3.2.19 on 2023-07-24 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mental', '0005_awareness_meditation'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result1', models.CharField(max_length=225)),
                ('result2', models.CharField(max_length=225)),
                ('result3', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mental.user')),
            ],
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('ratings', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mental.user')),
            ],
        ),
        migrations.CreateModel(
            name='emotions',
            fields=[
                ('emotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('emotions', models.CharField(max_length=225)),
                ('emotions_score', models.CharField(max_length=225)),
                ('date', models.CharField(max_length=225)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mental.user')),
            ],
        ),
    ]
