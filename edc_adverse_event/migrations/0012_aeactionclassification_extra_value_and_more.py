# Generated by Django 4.2.3 on 2023-08-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_adverse_event", "0011_alter_aeactionclassification_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="aeactionclassification",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="aeclassification",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="causeofdeath",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="saereason",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
