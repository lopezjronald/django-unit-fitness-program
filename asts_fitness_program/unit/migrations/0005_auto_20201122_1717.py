# Generated by Django 3.1.3 on 2020-11-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0004_auto_20201122_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airman',
            name='rank',
            field=models.CharField(choices=[('AB', 'AB'), ('Amn', 'Amn'), ('A1C', 'A1C'), ('SrA', 'SrA'), ('SSgt', 'SSgt'), ('TSgt', 'TSgt'), ('MSgt', 'MSgt'), ('SMSgt', 'SMSgt'), ('CMSgt', 'CMSgt'), ('2nd Lt', '2nd Lt'), ('1st Lt', '1st Lt'), ('Capt', 'Capt'), ('Maj', 'Maj'), ('Lt Col', 'Lt Col'), ('Col', 'Col'), ('Brig Gen', 'Brig Gen'), ('Maj Gen', 'Maj Gen'), ('Lt Gen', 'Lt Gen'), ('Gen', 'General')], default='AB', max_length=10),
        ),
    ]