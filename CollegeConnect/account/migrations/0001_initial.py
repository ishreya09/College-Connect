# Generated by Django 4.2.6 on 2023-10-18 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("branch", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "student_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("bio", models.CharField(blank=True, max_length=500, null=True)),
                ("college_email", models.EmailField(max_length=500)),
                (
                    "whatsapp_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                (
                    "whatsapp_link",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("email_confirmed", models.BooleanField(default=False)),
                ("is_mentor", models.BooleanField(default=False)),
                ("show_number", models.BooleanField(default=False)),
                ("year_of_passing_out", models.IntegerField(blank=True, null=True)),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="branch.branch",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="branch.department",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Mentor",
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
                ("resume", models.FileField(upload_to="resume/")),
                (
                    "description",
                    models.CharField(blank=True, max_length=5000, null=True),
                ),
                (
                    "domain",
                    taggit.managers.TaggableManager(
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                (
                    "student",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mentor",
                        to="account.student",
                    ),
                ),
            ],
        ),
    ]
