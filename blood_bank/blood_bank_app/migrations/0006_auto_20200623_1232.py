# Generated by Django 2.0.13 on 2020-06-23 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank_app', '0005_auto_20200623_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='quantite',
            new_name='quantite_commande',
        ),
    ]