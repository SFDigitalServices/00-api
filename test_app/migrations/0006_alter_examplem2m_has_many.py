# Generated by Django 3.2.10 on 2022-01-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0005_alter_exampleschild_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplem2m',
            name='has_many',
            field=models.ManyToManyField(related_name='examplem2ms', related_query_name='examplem2ms', to='test_app.Example'),
        ),
    ]