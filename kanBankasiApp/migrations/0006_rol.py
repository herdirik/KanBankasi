# Generated by Django 2.0.4 on 2018-04-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanBankasiApp', '0005_hastane'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_adi', models.CharField(max_length=20)),
            ],
        ),
    ]
