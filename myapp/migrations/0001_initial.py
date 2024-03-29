# Generated by Django 4.2.7 on 2024-02-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuzdalUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=77, null=True)),
                ('token', models.CharField(max_length=77, null=True)),
                ('uid', models.CharField(max_length=77, null=True)),
                ('first_login', models.CharField(max_length=22, null=True)),
                ('last_login', models.CharField(max_length=22, null=True)),
                ('province', models.CharField(max_length=3, null=True)),
                ('category', models.CharField(max_length=3, null=True)),
                ('city', models.CharField(max_length=22, null=True)),
                ('zone', models.CharField(max_length=22, null=True)),
                ('name', models.CharField(max_length=33, null=True)),
                ('age', models.CharField(max_length=3, null=True)),
                ('phone', models.CharField(max_length=22, null=True)),
                ('page_title', models.CharField(max_length=77, null=True)),
                ('about_me', models.TextField(null=True)),
                ('cover_image', models.CharField(max_length=77, null=True)),
                ('images', models.TextField(null=True)),
                ('complaints', models.IntegerField(null=True)),
                ('state', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'suzdal_user',
                'indexes': [models.Index(fields=['id', 'email'], name='suzdal_user_id_2c1b59_idx')],
            },
        ),
        migrations.CreateModel(
            name='SuzdalImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(null=True)),
                ('image1', models.TextField(null=True)),
                ('image2', models.TextField(null=True)),
                ('image3', models.TextField(null=True)),
                ('image4', models.TextField(null=True)),
            ],
            options={
                'db_table': 'suzdal_image',
                'indexes': [models.Index(fields=['user_id'], name='suzdal_imag_user_id_35c770_idx')],
            },
        ),
    ]
