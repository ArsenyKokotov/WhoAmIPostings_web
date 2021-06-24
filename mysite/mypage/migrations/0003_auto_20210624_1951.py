# Generated by Django 2.2.12 on 2021-06-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0002_description_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt', models.CharField(max_length=500)),
                ('new_file', models.FileField(upload_to='uploaded_files/')),
            ],
        ),
        migrations.AlterField(
            model_name='description',
            name='txt_description',
            field=models.CharField(max_length=10000),
        ),
    ]