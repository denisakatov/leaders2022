# Generated by Django 3.2.16 on 2022-10-30 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_code', models.CharField(blank=True, default='', max_length=25, verbose_name='внешний ключ пациента')),
                ('media_file', models.FileField(blank=True, upload_to='', verbose_name='файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'иследование',
                'verbose_name_plural': 'исследования',
            },
        ),
    ]