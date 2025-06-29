# Generated by Django 5.2.1 on 2025-06-04 16:31

import _socket
import django.core.validators
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_reportable", "0003_referencerangecollection_grade1_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="referencerangecollection",
            name="grade3",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="referencerangecollection",
            name="grade4",
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name="HistoricalGradingData",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                        verbose_name="Hostname created",
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                        verbose_name="Hostname modified",
                    ),
                ),
                (
                    "device_created",
                    models.CharField(blank=True, max_length=10, verbose_name="Device created"),
                ),
                (
                    "device_modified",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Device modified"
                    ),
                ),
                (
                    "locale_created",
                    models.CharField(
                        blank=True,
                        help_text="Auto-updated by Modeladmin",
                        max_length=10,
                        null=True,
                        verbose_name="Locale created",
                    ),
                ),
                (
                    "locale_modified",
                    models.CharField(
                        blank=True,
                        help_text="Auto-updated by Modeladmin",
                        max_length=10,
                        null=True,
                        verbose_name="Locale modified",
                    ),
                ),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("label", models.CharField(max_length=25)),
                ("description", models.CharField(max_length=255, null=True)),
                ("reference_group", models.CharField(max_length=25, null=True)),
                ("lower", models.FloatField(null=True)),
                ("lower_operator", models.CharField(max_length=15, null=True)),
                ("lower_inclusive", models.BooleanField(default=False)),
                ("lln", models.CharField(default=None, max_length=15, null=True)),
                ("upper", models.FloatField(null=True)),
                ("upper_operator", models.CharField(max_length=2, null=True)),
                ("upper_inclusive", models.BooleanField(default=False)),
                ("uln", models.CharField(default=None, max_length=15, null=True)),
                (
                    "gender",
                    models.CharField(
                        max_length=1,
                        validators=[django.core.validators.RegexValidator("[MF]{1}")],
                    ),
                ),
                ("units", models.CharField(max_length=15)),
                ("age_units", models.CharField(max_length=15)),
                ("age_lower", models.IntegerField()),
                ("age_lower_operator", models.CharField(max_length=15)),
                ("age_lower_inclusive", models.BooleanField(default=False)),
                ("age_upper", models.IntegerField(null=True)),
                ("age_upper_operator", models.CharField(max_length=15, null=True)),
                ("age_upper_inclusive", models.BooleanField(null=True)),
                ("fasting", models.BooleanField(default=False)),
                (
                    "phrase",
                    models.CharField(
                        help_text="calculated by the formula instance",
                        max_length=50,
                        null=True,
                        verbose_name="Value phrase",
                    ),
                ),
                (
                    "age_phrase",
                    models.CharField(
                        help_text="calculated in save()", max_length=25, null=True
                    ),
                ),
                ("grade", models.IntegerField()),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reference_range_collection",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="edc_reportable.referencerangecollection",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Grading Reference",
                "verbose_name_plural": "historical Grading References",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalNormalData",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                        verbose_name="Hostname created",
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                        verbose_name="Hostname modified",
                    ),
                ),
                (
                    "device_created",
                    models.CharField(blank=True, max_length=10, verbose_name="Device created"),
                ),
                (
                    "device_modified",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Device modified"
                    ),
                ),
                (
                    "locale_created",
                    models.CharField(
                        blank=True,
                        help_text="Auto-updated by Modeladmin",
                        max_length=10,
                        null=True,
                        verbose_name="Locale created",
                    ),
                ),
                (
                    "locale_modified",
                    models.CharField(
                        blank=True,
                        help_text="Auto-updated by Modeladmin",
                        max_length=10,
                        null=True,
                        verbose_name="Locale modified",
                    ),
                ),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                ("label", models.CharField(max_length=25)),
                ("description", models.CharField(max_length=255, null=True)),
                ("reference_group", models.CharField(max_length=25, null=True)),
                ("lower", models.FloatField(null=True)),
                ("lower_operator", models.CharField(max_length=15, null=True)),
                ("lower_inclusive", models.BooleanField(default=False)),
                ("lln", models.CharField(default=None, max_length=15, null=True)),
                ("upper", models.FloatField(null=True)),
                ("upper_operator", models.CharField(max_length=2, null=True)),
                ("upper_inclusive", models.BooleanField(default=False)),
                ("uln", models.CharField(default=None, max_length=15, null=True)),
                (
                    "gender",
                    models.CharField(
                        max_length=1,
                        validators=[django.core.validators.RegexValidator("[MF]{1}")],
                    ),
                ),
                ("units", models.CharField(max_length=15)),
                ("age_units", models.CharField(max_length=15)),
                ("age_lower", models.IntegerField()),
                ("age_lower_operator", models.CharField(max_length=15)),
                ("age_lower_inclusive", models.BooleanField(default=False)),
                ("age_upper", models.IntegerField(null=True)),
                ("age_upper_operator", models.CharField(max_length=15, null=True)),
                ("age_upper_inclusive", models.BooleanField(null=True)),
                ("fasting", models.BooleanField(default=False)),
                (
                    "phrase",
                    models.CharField(
                        help_text="calculated by the formula instance",
                        max_length=50,
                        null=True,
                        verbose_name="Value phrase",
                    ),
                ),
                (
                    "age_phrase",
                    models.CharField(
                        help_text="calculated in save()", max_length=25, null=True
                    ),
                ),
                (
                    "grade",
                    models.IntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reference_range_collection",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="edc_reportable.referencerangecollection",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Normal Reference",
                "verbose_name_plural": "historical Normal References",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
