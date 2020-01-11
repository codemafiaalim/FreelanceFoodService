# Generated by Django 2.2.7 on 2020-01-11 14:37

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
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='store_name', max_length=100)),
                ('desc', models.CharField(default='default desc', max_length=1000)),
                ('location', models.CharField(choices=[('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Wari', 'Wari')], default='Farmgate', max_length=200)),
                ('covImg', models.ImageField(upload_to='pic_ups')),
                ('active', models.BooleanField(default=True)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5)),
                ('catagory', models.CharField(choices=[('HomeMade', 'HomeMade'), ('Professional', 'Professional')], default='HomeMade', max_length=200)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]