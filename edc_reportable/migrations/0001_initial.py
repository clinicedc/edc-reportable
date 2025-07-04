# Generated by Django 6.0 on 2025-05-05 19:11

import _socket
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ReferenceRangeCollection",
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
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
            options={
                "verbose_name": "Reference Range Collection",
                "verbose_name_plural": "Reference Range Collections",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
                "default_manager_name": "objects",
                "indexes": [
                    models.Index(
                        fields=["modified", "created"], name="edc_reporta_modifie_197943_idx"
                    ),
                    models.Index(
                        fields=["user_modified", "user_created"],
                        name="edc_reporta_user_mo_48976f_idx",
                    ),
                ],
            },
        ),
        migrations.CreateModel(
            name="NormalData",
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
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
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
                ("gender", models.CharField(max_length=15)),
                ("units", models.CharField(max_length=15)),
                ("age_units", models.CharField(max_length=15)),
                ("age_lower", models.IntegerField()),
                ("age_lower_operator", models.CharField(max_length=15)),
                ("age_lower_inclusive", models.BooleanField(default=False)),
                ("age_upper", models.IntegerField()),
                ("age_upper_operator", models.CharField(max_length=15)),
                ("age_upper_inclusive", models.BooleanField(default=False)),
                ("fasting", models.BooleanField(default=False)),
                ("phrase", models.CharField(max_length=50, null=True)),
                ("age_phrase", models.CharField(max_length=25, null=True)),
                ("grade", models.IntegerField(null=True)),
                (
                    "reference_range_collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="edc_reportable.referencerangecollection",
                    ),
                ),
            ],
            options={
                "verbose_name": "Normal Reference",
                "verbose_name_plural": "Normal References",
            },
        ),
        migrations.CreateModel(
            name="GradingData",
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
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
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
                ("gender", models.CharField(max_length=15)),
                ("units", models.CharField(max_length=15)),
                ("age_units", models.CharField(max_length=15)),
                ("age_lower", models.IntegerField()),
                ("age_lower_operator", models.CharField(max_length=15)),
                ("age_lower_inclusive", models.BooleanField(default=False)),
                ("age_upper", models.IntegerField()),
                ("age_upper_operator", models.CharField(max_length=15)),
                ("age_upper_inclusive", models.BooleanField(default=False)),
                ("fasting", models.BooleanField(default=False)),
                ("phrase", models.CharField(max_length=50, null=True)),
                ("age_phrase", models.CharField(max_length=25, null=True)),
                ("grade", models.IntegerField()),
                (
                    "reference_range_collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="edc_reportable.referencerangecollection",
                    ),
                ),
            ],
            options={
                "verbose_name": "Grading Reference",
                "verbose_name_plural": "Grading References",
            },
        ),
    ]
