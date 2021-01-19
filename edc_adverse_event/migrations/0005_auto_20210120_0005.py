# Generated by Django 3.0.9 on 2021-01-19 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("edc_adverse_event", "0004_auto_20200513_0023"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="saereason",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "get_latest_by": "modified",
                "ordering": ["display_index", "display_name"],
            },
        ),
    ]
