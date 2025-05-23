# Generated by Django 4.2.11 on 2025-05-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_django', '0003_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='produtos/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
