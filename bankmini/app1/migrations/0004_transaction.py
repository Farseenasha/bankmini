# Generated by Django 5.0.6 on 2024-05-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_age_customs_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('details', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('user_amount', models.IntegerField()),
            ],
        ),
    ]