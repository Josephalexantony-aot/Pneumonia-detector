# Generated by Django 3.1 on 2021-01-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('D_name', models.CharField(max_length=50)),
                ('D_address', models.CharField(max_length=200)),
                ('D_gender', models.CharField(max_length=10)),
                ('D_qualification', models.CharField(max_length=50)),
                ('D_email', models.EmailField(max_length=50)),
                ('D_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=50)),
                ('t_nNo', models.IntegerField()),
                ('patientAge', models.IntegerField()),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phoneNo', models.IntegerField()),
                ('discription', models.CharField(max_length=200, null=True)),
                ('regDate', models.DateTimeField(auto_now=True)),
                ('doct_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='XrayUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('xray_image', models.ImageField(upload_to='images/')),
                ('result', models.CharField(max_length=50)),
                ('image_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
