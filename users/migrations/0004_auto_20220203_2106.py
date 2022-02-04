# Generated by Django 3.1.13 on 2022-02-03 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220203_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=35, null=True)),
                ('postcode', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.adress'),
        ),
        migrations.AlterField(
            model_name='freelanceprofile',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.adress'),
        ),
    ]
