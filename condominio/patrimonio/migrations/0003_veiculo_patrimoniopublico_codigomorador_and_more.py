# Generated by Django 5.0.6 on 2024-08-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0002_rename_patrimonioprivadoutensilio_patrimonioprivadocompartilhaveis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('placa', models.IntegerField(default=0)),
                ('cor', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('codigoMorador', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='patrimoniopublico',
            name='codigoMorador',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patrimoniopublico',
            name='emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
