# Generated by Django 2.2.6 on 2019-10-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_adverse_event", "0002_auto_20190802_0059")]

    operations = [
        migrations.AlterModelOptions(
            name="aeclassification",
            options={"ordering": ["display_index", "display_name"]},
        ),
        migrations.AlterModelOptions(
            name="causeofdeath", options={"ordering": ["display_index", "display_name"]}
        ),
        migrations.AlterModelOptions(
            name="saereason", options={"ordering": ["display_index", "display_name"]}
        ),
        migrations.RemoveIndex(
            model_name="aeclassification", name="edc_adverse_id_8133d9_idx"
        ),
        migrations.RemoveIndex(model_name="causeofdeath", name="edc_adverse_id_42a796_idx"),
        migrations.RemoveIndex(model_name="saereason", name="edc_adverse_id_88072b_idx"),
        migrations.RenameField(
            model_name="aeclassification", old_name="name", new_name="display_name"
        ),
        migrations.RenameField(
            model_name="causeofdeath", old_name="name", new_name="display_name"
        ),
        migrations.RenameField(
            model_name="saereason", old_name="name", new_name="display_name"
        ),
        migrations.RenameField(
            model_name="aeclassification", old_name="short_name", new_name="name"
        ),
        migrations.RenameField(
            model_name="causeofdeath", old_name="short_name", new_name="name"
        ),
        migrations.RenameField(model_name="saereason", old_name="short_name", new_name="name"),
        migrations.AddIndex(
            model_name="aeclassification",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="edc_adverse_id_6431b6_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="causeofdeath",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="edc_adverse_id_ca88f1_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="saereason",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="edc_adverse_id_dc0e62_idx",
            ),
        ),
    ]
