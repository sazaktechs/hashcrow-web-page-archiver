# Generated by Django 3.2 on 2023-11-03 14:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('url', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SnapShot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='api.hash')),
            ],
        ),
        migrations.AddField(
            model_name='hash',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snapshots', to='api.url'),
        ),
    ]
