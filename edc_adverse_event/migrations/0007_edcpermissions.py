# Generated by Django 3.2.13 on 2022-08-24 21:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("edc_auth", "0026_rename_permissions_edcpermissions"),
        ("edc_adverse_event", "0006_auto_20210425_1628"),
    ]

    operations = [
        migrations.CreateModel(
            name="EdcPermissions",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("edc_auth.edcpermissions",),
        ),
    ]
