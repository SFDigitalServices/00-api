# Generated by Django 3.2.11 on 2022-03-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0006_alter_examplem2m_has_many"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleBetter",
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
                ("char1", models.CharField(max_length=10)),
                ("char2", models.CharField(max_length=10)),
                ("char3", models.CharField(max_length=10)),
                ("char4", models.CharField(max_length=10)),
            ],
        ),
    ]
