# Generated by Django 3.2.18 on 2023-04-20 00:53

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
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('select1_content', models.CharField(max_length=1000)),
                ('select2_content', models.CharField(max_length=1000)),
                ('select1_users', models.ManyToManyField(related_name='select1_balances', to=settings.AUTH_USER_MODEL)),
                ('select2_users', models.ManyToManyField(related_name='select2_balances', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
