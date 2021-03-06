# Generated by Django 2.0.4 on 2018-04-23 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanBankasiApp', '0007_kangrubu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=20)),
                ('soyad', models.CharField(max_length=20)),
                ('dogum_tarihi', models.DateField(blank=True, null=True)),
                ('cinsiyet', models.NullBooleanField(choices=[(True, 'Erkek'), (False, 'Kadın')])),
                ('telefon', models.CharField(max_length=11)),
                ('il_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.Il')),
                ('ilce_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.Ilce')),
                ('kanGrubu_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.KanGrubu')),
                ('rol_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.Rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
