# Generated by Django 5.1.4 on 2024-12-26 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0003_alter_contacts_dealer_alter_dealer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='dealer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='online_store.dealer', verbose_name='Дилер'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='debt_to_supplier',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True, verbose_name='Задолженность перед поставщиком'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='dealer',
        ),
        migrations.AddField(
            model_name='product',
            name='dealer',
            field=models.ManyToManyField(related_name='products', to='online_store.dealer', verbose_name='Дилер'),
        ),
    ]
