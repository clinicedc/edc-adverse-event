# Generated by Django 3.2.13 on 2022-09-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_adverse_event", "0009_auto_20220907_0157"),
    ]

    operations = [
        migrations.AddField(
            model_name="aeactionclassification",
            name="plural_name",
            field=models.CharField(max_length=250, null=True, verbose_name="Plural name"),
        ),
        migrations.AddField(
            model_name="aeclassification",
            name="plural_name",
            field=models.CharField(max_length=250, null=True, verbose_name="Plural name"),
        ),
        migrations.AddField(
            model_name="causeofdeath",
            name="plural_name",
            field=models.CharField(max_length=250, null=True, verbose_name="Plural name"),
        ),
        migrations.AddField(
            model_name="saereason",
            name="plural_name",
            field=models.CharField(max_length=250, null=True, verbose_name="Plural name"),
        ),
    ]
