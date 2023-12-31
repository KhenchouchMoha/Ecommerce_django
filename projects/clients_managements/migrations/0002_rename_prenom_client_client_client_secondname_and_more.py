# Generated by Django 4.2.6 on 2023-10-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients_managements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='prenom_client',
            new_name='client_SecondName',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='nom_client',
            new_name='client_firstName',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='id_client',
            new_name='client_id',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='login_client',
            new_name='client_login',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='mot_de_passe_client',
            new_name='client_mot_de_passe',
        ),
        migrations.RemoveField(
            model_name='client',
            name='adresse_client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email_client',
        ),
        migrations.RemoveField(
            model_name='client',
            name='numero_client',
        ),
        migrations.AddField(
            model_name='client',
            name='client_Adresse',
            field=models.TextField(default='adresse'),
        ),
        migrations.AddField(
            model_name='client',
            name='client_Email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='client',
            name='client_Number',
            field=models.TextField(default='060000000'),
        ),
    ]
