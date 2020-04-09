# Generated by Django 3.0.3 on 2020-04-08 20:25

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_student_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(default='profile_img/user.png', upload_to=account.models.get_image_name),
        ),
    ]
