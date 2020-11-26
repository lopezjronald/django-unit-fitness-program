# Generated by Django 3.1.3 on 2020-11-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0011_auto_20201122_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failure',
            name='airman_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman'),
        ),
        migrations.AlterField(
            model_name='physical_training_leader',
            name='airman_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='airman_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman'),
        ),
        migrations.AlterField(
            model_name='unit_fitness_program_manager',
            name='airman_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unit.airman'),
        ),
    ]
