# Generated by Django 6.0 on 2025-05-06 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_reportable", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gradingdata",
            name="age_upper",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="gradingdata",
            name="age_upper_inclusive",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="gradingdata",
            name="age_upper_operator",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="normaldata",
            name="age_upper",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="normaldata",
            name="age_upper_inclusive",
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name="normaldata",
            name="age_upper_operator",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
