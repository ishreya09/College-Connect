# Generated by Django 4.2.6 on 2023-11-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0006_remove_club_branch_remove_clubmember_club_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mentor",
            name="username",
        ),
        migrations.AlterField(
            model_name="clubmember",
            name="joined_on",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="mentor",
            name="last_application_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
