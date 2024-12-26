from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Dealer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование дилера")
    supplier = models.ForeignKey('self',
                                 on_delete=models.SET_NULL,
                                 related_name='supply_to',
                                 verbose_name='Поставщик',
                                 **NULLABLE)
    debt_to_supplier = models.DecimalField(default=0.00,
                                           max_digits=10,
                                           decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком')
    date_of_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Объект сети"
        verbose_name_plural = "Объекты сети"
        ordering = ["name"]


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    building = models.CharField(max_length=20, verbose_name='Номер дома')
    dealer = models.OneToOneField(Dealer,
                                  on_delete=models.CASCADE,
                                  related_name='contacts',
                                  verbose_name='Дилер',
                                  **NULLABLE)

    def __str__(self):
        return (f"Почта: {self.email}, страна: {self.country}, город: {self.city}, "
                f"улица: {self.street}, номер дома: {self.building}")

    class Meta:
        verbose_name = "Контактная информация"
        ordering = ["country"]


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    model = models.CharField(max_length=100, verbose_name='Модель продукта')
    dealer = models.ManyToManyField(Dealer, related_name='products', verbose_name='Дилер')
    date_of_release = models.DateField(auto_now=False,
                                       auto_now_add=False,
                                       verbose_name="Дата выхода продукта на рынок")

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]



