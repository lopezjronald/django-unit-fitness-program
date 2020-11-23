# Generated by Django 3.1.3 on 2020-11-23 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0003_auto_20201122_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airman',
            options={'ordering': ('-last_name',)},
        ),
        migrations.AlterModelOptions(
            name='failure',
            options={'ordering': ('-failure_date',)},
        ),
        migrations.AlterModelOptions(
            name='physical_training_leader',
            options={'ordering': ('-ptl_expiration_date',)},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('-profile_expiration_date',)},
        ),
        migrations.AlterModelOptions(
            name='unit_fitness_program_manager',
            options={'ordering': ('-ufpm_expiration_date',)},
        ),
        migrations.AlterField(
            model_name='airman',
            name='rank',
            field=models.CharField(choices=[('AB', 'AB'), ('Amn', 'Amn'), ('A1C', 'A1C'), ('SrA', 'SrA'), ('SSgt', 'SSgt'), ('TSgt', 'TSgt'), ('MSgt', 'MSgt'), ('SMSgt', 'SMSgt'), ('CMSgt', 'CMSgt'), ('2nd Lt', '2nd Lt'), ('1st Lt', '1st Lt'), ('Capt', 'Capt'), ('Maj', 'Maj'), ('Lt Col', 'Lt Col'), ('Col', 'Col'), ('Brig Gen', 'Brig Gen'), ('Maj Gen', 'Maj Gen'), ('Lt Gen', 'Lt Gen'), ('Gen', 'General')], default='ab', max_length=10),
        ),
    ]
