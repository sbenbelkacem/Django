# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom_utilisateur', models.CharField(max_length=40)),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('adresse_email', models.CharField(max_length=25)),
                ('data_de_naissance', models.DateTimeField(verbose_name=b'date de naissance')),
                ('numero_telephone_fixe', models.CharField(max_length=10)),
                ('numero_telephone_mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
