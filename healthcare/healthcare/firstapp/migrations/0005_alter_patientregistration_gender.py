# Generated by Django 3.2.3 on 2021-05-30 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_alter_patientregistration_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientregistration',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10),
        ),
    ]
