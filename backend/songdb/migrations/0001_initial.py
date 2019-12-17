# Generated by Django 3.0 on 2019-12-17 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('year_of_birth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('genre', models.CharField(choices=[('r', 'Rock'), ('p', 'Pop'), ('j', 'Jazz'), ('h', 'Hip Hop'), ('m', 'Metal')], max_length=1)),
                ('release_date', models.DateField()),
                ('story', models.TextField()),
                ('band_or_not', models.BooleanField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songdb.Country')),
                ('singers', models.ManyToManyField(to='songdb.Person')),
            ],
        ),
    ]
