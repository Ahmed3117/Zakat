

from django.utils import timezone
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver


class Item(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


@receiver(post_save, sender=Item)
def create_available(sender, instance, created, **kwargs):
    if created:
        Available.objects.create(item=instance)
        Inbound.objects.create(item=instance)
        Outbound.objects.create(item=instance)

class Inbound(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        super(Inbound, self).save(*args, **kwargs)
        try:
            available = Available.objects.get(item=self.item)
        except Available.DoesNotExist:
            available = Available.objects.create(item=self.item)
        in_sum = Inbound.objects.filter(item=self.item).aggregate(Sum('quantity'))['quantity__sum'] or 0
        out_sum = Outbound.objects.filter(item=self.item).aggregate(Sum('quantity'))['quantity__sum'] or 0
        available.available_quantity = in_sum - out_sum
        available.save()
    def __str__(self):
        return self.item.name + str(self.quantity)

class Outbound(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    def save(self, *args, **kwargs):
        super(Outbound, self).save(*args, **kwargs)
        try:
            available = Available.objects.get(item=self.item)
        except Available.DoesNotExist:
            available = Available.objects.create(item=self.item)
        in_sum = Inbound.objects.filter(item=self.item).aggregate(Sum('quantity'))['quantity__sum'] or 0
        out_sum = Outbound.objects.filter(item=self.item).aggregate(Sum('quantity'))['quantity__sum'] or 0
        available.available_quantity = in_sum - out_sum
        available.save()

    def __str__(self):
        return self.item.name + str(self.quantity)

class Available(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    available_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item.name} ({self.available_quantity})"