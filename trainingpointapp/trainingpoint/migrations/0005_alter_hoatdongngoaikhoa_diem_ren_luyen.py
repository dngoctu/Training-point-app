# Generated by Django 5.0.4 on 2024-04-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingpoint', '0004_alter_sinhvien_gioi_tinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoatdongngoaikhoa',
            name='diem_ren_luyen',
            field=models.IntegerField(default=5),
        ),
    ]
