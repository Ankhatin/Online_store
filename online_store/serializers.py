import json

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer

from online_store.models import Dealer, Contacts, Product


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ['dealer']


class DealerSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(required=False)
    products = ProductSerializer(many=True, required=False)

    def validate_debt_to_supplier(self, data):
        if data < 0:
            raise ValidationError("Debt must be a positive value")

    def create(self, validated_data):
        contact_info = validated_data.pop('contacts', [])
        products = validated_data.pop('products', [])
        # создаем экземпляр объекта сети
        dealer = Dealer.objects.create(**validated_data)
        if contact_info:
            # создаем экземпляр контактов
            Contacts.objects.create(**contact_info, dealer=dealer)
        product_list = []
        for product in products:
            product, _ = Product.objects.get_or_create(**product)
            product_list.append(product)
        dealer.products.set(product_list)
        return dealer


    class Meta:
        model = Dealer
        fields = ['id', 'name', 'supplier', 'debt_to_supplier', 'contacts', 'products']


class ContactsField(serializers.RelatedField):
    def to_representation(self, value):
        data = vars(value)
        data.pop('_state')
        data.pop('dealer_id')
        return data

    def get_queryset(self):
        super().get_queryset()

    def to_internal_value(self, data):
        return data


class DealerUpdateSerializer(serializers.ModelSerializer):
    '''
    Создаем отдельный класс сериализатора для обновления данных дилера,
    чтобы избежать ошибки на уникальность поля email,
    когда контактыне данные с таким email уже существуют
    '''

    contacts = ContactsField(required=False)
    products = ProductSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        '''
        Метод обновляет экземпляр объекта сети
        В случае наличия контактных данных и/или продуктов обновляет
        или добавляет экзмемлпяры указанных моделей в набор данных объекта сети
        :param instance:
        :param validated_data:
        :return:
        '''
        contact_info = validated_data.pop('contacts', {})
        products_info = validated_data.pop('products', [])
        instance = super().update(instance, validated_data)
        instance.debt_to_supplier = validated_data.get('debt_to_supplier', instance.debt_to_supplier)
        if contact_info:
            if instance.contacts:
                # если у дилера существует связанный экземпляр контактов обновляем в нём данные
                if instance.contacts.email == contact_info['email']:
                    # если email не изменился обновляем поля контакта
                    serializer = ContactsSerializer(instance.contacts, data=contact_info, partial=True)
                    if serializer.is_valid():
                        instance.contacts = serializer.save()
                else:
                    # если при обновлении изменен email, проверяем его на уникальность
                    if not Contacts.objects.filter(email=contact_info['email']).exists():
                        serializer = ContactsSerializer(instance.contacts, data=contact_info, partial=True)
                        if serializer.is_valid():
                            instance.contacts = serializer.save()
                    else:
                        raise serializers.ValidationError
            else:
                # если у дилера были не заполнены контакты создаем экземпляр
                Contacts.objects.create(email=contact_info['email'],
                                        country=contact_info['country'],
                                        city=contact_info['city'],
                                        street=contact_info['street'],
                                        building=contact_info['building'],
                                        dealer=instance)
        product_list = []
        for product in products_info:
            product, _ = Product.objects.get_or_create(**product)
            product_list.append(product)
        instance.products.set(product_list)
        return instance

    class Meta:
        model = Dealer
        fields = ['id', 'name', 'supplier', 'debt_to_supplier', 'contacts', 'products']
        read_only_fields = ['debt_to_supplier']