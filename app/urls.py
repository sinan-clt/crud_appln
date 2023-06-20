from django.urls import path
from .views import ItemListAPIView, ItemRetrieveAPIView, ItemUpdateAPIView, ItemDeleteAPIView, ItemCreateAPIView, ItemBulkAPIView

urlpatterns = [
    path('create_item', ItemCreateAPIView.as_view(), name='item-create'),
    path('list_item', ItemListAPIView.as_view(), name='item-list'),
    path('view_item_by_id/<int:pk>', ItemRetrieveAPIView.as_view(), name='single-item-view'),
    path('update_item/<int:pk>', ItemUpdateAPIView.as_view(), name='item-update'),
    path('delete_item/<int:pk>', ItemDeleteAPIView.as_view(), name='item-delete'),

    path('bulk_item/<int:pk>/', ItemBulkAPIView.as_view(), name='item-bulk-detail'),
    path('bulk-delete/', ItemBulkAPIView.as_view(), name='item-bulk-delete'),
]
