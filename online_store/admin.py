from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from online_store.models import *


class ContactsInline(admin.StackedInline):
    model = Contacts


class ProductInline(admin.StackedInline):
    model = Dealer.products.through


@admin.action(description='Обнулить задолженность у выбранных объектов')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier_ref']
    list_filter = ('contacts__city',)
    fields = ['name', 'supplier', 'debt_to_supplier']
    list_select_related = ["supplier"]
    inlines = [ContactsInline, ProductInline]
    actions = [clear_debt]

    def supplier_ref(self, obj):
        if obj.supplier:
            link = reverse("admin:online_store_dealer_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier)

    supplier_ref.short_description = "Поставщик"
