# Generated by Django 5.0.2 on 2024-09-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_remove_customer_user_customer_email_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
