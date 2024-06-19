from django.db import models

class Kategor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class Cake(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    kategor = models.ForeignKey('Kategor', on_delete=models.DO_NOTHING,
                                blank=True, null=True, related_name='cakes')
    def get_absolute_url(self):
        return f'/profile/'

    def __str__(self):
        return self.name



class CakeOrder(models.Model):
    cake_id1 = models.AutoField(primary_key=True)
    cake_id = models.ForeignKey('Cake', on_delete=models.DO_NOTHING,
                                blank=True, null=True, related_name='cakes')
    cake_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    order_description = models.TextField()
    # Добавьте другие поля, связанные с заказом (например, дата, статус и т. д.)

    def __str__(self):
        return self.phone_number