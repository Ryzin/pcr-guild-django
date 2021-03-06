# Generated by Django 3.0.6 on 2020-05-21 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_auto_20200520_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('id', models.CharField(default='8cb8b99e9b1111ea9b7ed46d6df5224b', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
                ('desc', models.CharField(default='', max_length=256)),
                ('create', models.DateTimeField()),
                ('join', models.IntegerField(choices=[(0, 'Auto'), (1, 'Password'), (2, 'Validate'), (3, 'Forbid')])),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='manage', to='user.User')),
            ],
        ),
    ]
