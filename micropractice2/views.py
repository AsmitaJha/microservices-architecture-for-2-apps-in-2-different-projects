from django.shortcuts import render

PRODUCT_SERVICE_URL = "http://127.0.0.1:8000/products/"

import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer

# URL of the Product microservice


@api_view(["POST"])
def create_order(request):
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity")

    # Fetch product details from the Product microservice, product app has been created in another project in this case
    response = requests.get(
        f"{PRODUCT_SERVICE_URL}{product_id}/"
    )  # fetching product_id from product url which has been defined in the other project including product app

    if response.status_code == 200:
        product_data = response.json()

        # Create the order
        order = Order.objects.create(product_id=product_id, quantity=quantity)
        return Response(
            {
                "message": "Order placed successfully",
                "order_id": order.id,
                "product": product_data,
                "quantity": quantity,
            }
        )
    else:
        return Response({"error": "Product not found"}, status=404)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
