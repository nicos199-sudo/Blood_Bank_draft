# Generated by Django 2.0.13 on 2020-06-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood_bank_app', '0003_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField(auto_now_add=True, null=True)),
                ('quantite', models.IntegerField()),
                ('groupe_sanguin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blood_bank_app.Sang')),
            ],
        ),
        migrations.CreateModel(
            name='Hopitaux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='partenaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blood_bank_app.Hopitaux'),
        ),
    ]