# Generated by Django 5.1.4 on 2024-12-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='contacts',
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='debt_to_supplier',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
