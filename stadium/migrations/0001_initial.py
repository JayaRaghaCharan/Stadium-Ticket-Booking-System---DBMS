# Generated by Django 4.0.4 on 2022-05-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stadium_id', models.IntegerField()),
                ('game', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('username', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('pin', models.IntegerField()),
                ('rent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='matches',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('game', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('stadium', models.CharField(max_length=50)),
                ('stadium_id', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('S1', models.IntegerField()),
                ('S2', models.IntegerField()),
                ('S3', models.IntegerField()),
                ('S4', models.IntegerField()),
                ('S5', models.IntegerField()),
                ('S6', models.IntegerField()),
                ('S7', models.IntegerField()),
                ('S8', models.IntegerField()),
                ('S9', models.IntegerField()),
                ('S10', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='snacks',
            fields=[
                ('snacks_id', models.IntegerField(primary_key=True, serialize=False)),
                ('snacks', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='stadium',
            fields=[
                ('stadium_id', models.IntegerField(primary_key=True, serialize=False)),
                ('game', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('pin', models.IntegerField()),
                ('rent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('ticket', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('match_name', models.CharField(max_length=30)),
                ('match_id', models.IntegerField()),
                ('stadium', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('seat', models.IntegerField()),
                ('price', models.IntegerField()),
                ('snacks_id', models.IntegerField()),
            ],
        ),
    ]
