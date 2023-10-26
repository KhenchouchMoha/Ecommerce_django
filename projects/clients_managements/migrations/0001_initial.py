# Generated by Django 4.2.6 on 2023-10-25 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_client', models.CharField(max_length=50)),
                ('prenom_client', models.CharField(max_length=50)),
                ('adresse_client', models.TextField()),
                ('numero_client', models.TextField()),
                ('email_client', models.EmailField(max_length=254)),
                ('login_client', models.CharField(max_length=50)),
                ('mot_de_passe_client', models.CharField(max_length=50)),
            ],
        ),
    ]