# Generated by Django 2.2 on 2020-07-28 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='Male', max_length=6)),
                ('user_country', models.CharField(max_length=254)),
                ('user_joinas', models.CharField(choices=[('DOCTOR', 'Doctor'), ('PATIENT', 'Patient')], default='Doctor', max_length=7)),
                ('user_age', models.IntegerField(default=0)),
                ('user_jobtitle', models.TextField(max_length=254)),
                ('user_img', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('user_blogtitle', models.TextField(max_length=254)),
                ('user_blogdes', models.TextField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Artical', models.TextField(default='')),
                ('Artical_img', models.ImageField(default='default.jpg', upload_to='post_pics')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counseling.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]