from django.urls import path

from online_store.apps import OnlineStoreConfig
from online_store.views import DealerListView, DealerCreateView, DealerRetrieveView, DealerUpdateView, DealerDestroyView

app_name = OnlineStoreConfig.name

urlpatterns = [
    path("dealers/", DealerListView.as_view(), name="dealers"),
    path("dealers/create/", DealerCreateView.as_view(), name="dealer_create"),
    path('dealers/<int:pk>/', DealerRetrieveView.as_view(), name='dealer'),
    path('dealers/update/<int:pk>/', DealerUpdateView.as_view(), name='dealer_update'),
    path("dealers/delete/<int:pk>/", DealerDestroyView.as_view(), name="dealer_delete"),
]