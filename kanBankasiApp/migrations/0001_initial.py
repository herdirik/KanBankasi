# Generated by Django 2.0.4 on 2018-04-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
