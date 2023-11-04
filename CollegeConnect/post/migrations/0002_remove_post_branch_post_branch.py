# Generated by Django 4.2.6 on 2023-11-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("branch", "0001_initial"),
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="branch",
        ),
        migrations.AddField(
            model_name="post",
            name="branch",
            field=models.ManyToManyField(to="branch.branch", verbose_name="branches"),
        ),
    ]
