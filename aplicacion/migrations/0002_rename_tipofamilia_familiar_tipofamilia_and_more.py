# Generated by Django 4.0.3 on 2022-04-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='Tipofamilia',
            new_name='tipofamilia',
        ),
        migrations.AddField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
