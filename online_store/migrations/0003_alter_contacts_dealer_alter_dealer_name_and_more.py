# Generated by Django 5.1.4 on 2024-12-24 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_remove_dealer_contacts_alter_contacts_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='dealer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_info', to='online_store.dealer', verbose_name='Дилер'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование дилера'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supply_to', to='online_store.dealer', verbose_name='Поставщик'),
        ),
    ]
