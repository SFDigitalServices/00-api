# Generated by Django 3.2.10 on 2021-12-08 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExamplesChild",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_app.example",
                    ),
                ),
            ],
        ),
    ]
