# Generated by Django 4.0.5 on 2022-06-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebookapi', '0002_alter_note_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
