# Generated by Django 2.0.4 on 2018-04-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kanBankasiApp', '0002_delete_il'),
    ]

    operations = [
        migrations.CreateModel(
            name='Il',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('il_adi', models.CharField(max_length=30)),
            ],
        ),
    ]
