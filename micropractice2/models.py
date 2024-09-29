from django.db import models

class Order(models.Model):
    product_id = models.PositiveIntegerField()  # Store product ID, will fetch details from Product service
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for Product ID {self.product_id}"