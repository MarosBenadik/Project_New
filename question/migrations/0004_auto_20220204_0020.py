# Generated by Django 3.1.13 on 2022-02-04 00:20

from django.db import migrations, models
import question.models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_question_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(default='uploads/profilepictures/default.png', upload_to=question.models.getcurrentusername),
        ),
    ]
