# Generated by Django 3.2.3 on 2021-06-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]