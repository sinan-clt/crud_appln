from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.pagination import PageNumberPagination


class ItemCreateAPIView(APIView):

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemListAPIView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5
        items = Item.objects.filter(is_deleted=False)

        sort_by = request.query_params.get('sort_by')
        if sort_by == 'price_low_to_high':
            items = items.order_by('price')
        elif sort_by == 'price_high_to_low':
            items = items.order_by('-price')

        paginated_items = paginator.paginate_queryset(items, request)
        serializer = ItemSerializer(paginated_items, many=True)
        return paginator.get_paginated_response(serializer.data)


class ItemRetrieveAPIView(APIView):

    def get(self, request, pk):
        try:
            item = Item.objects.get(id=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)


class ItemUpdateAPIView(APIView):

    def put(self, request, pk):
        try:
            item = Item.objects.get(id=pk)
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)



class ItemDeleteAPIView(APIView):

    def delete(self, request, pk):
        try:
            item = Item.objects.get(id=pk)
            item.is_deleted = True
            item.save()
            remaining_items = Item.objects.filter(is_deleted=False)
            serializer = ItemSerializer(remaining_items, many=True)
            data = {
                'message': "Item deleted succesfully",
                'status':status.HTTP_200_OK,
                'remaining_items': serializer.data
            }
            return Response(data)
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)



class ItemBulkAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                item = Item.objects.get(id=pk)
                serializer = ItemSerializer(item)
                return Response(serializer.data)
            except Item.DoesNotExist:
                return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
            

    def delete(self, request):
        item_ids = request.data.get('item_ids', [])
        items = Item.objects.filter(id__in=item_ids)
        items.update(is_deleted=True)
        remaining_items = Item.objects.filter(is_deleted=False)
        serializer = ItemSerializer(remaining_items, many=True)
        data = {
            'message': "Items deleted successfully",
            'status': status.HTTP_200_OK,
            'remaining_items': serializer.data
        }
        return Response(data)
