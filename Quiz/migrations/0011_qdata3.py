# Generated by Django 4.0.5 on 2022-08-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0010_qdata2'),
    ]

    operations = [
        migrations.CreateModel(
            name='QData3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(max_length=100)),
                ('nihongo', models.CharField(max_length=100)),
            ],
        ),
    ]
