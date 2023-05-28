

from django.utils import timezone
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    name = models.CharField(_("التصنيف"),max_length=50)
    class Meta:
        verbose_name = _("التصنيف")
        verbose_name_plural = _("التصنيف")
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True,blank=True)
    name = models.CharField(_("الاسم"),max_length=50)
    class Meta:
        verbose_name = _("عنصر")
        verbose_name_plural = _("عناصر")
    def __str__(self):
        return self.name


class Donator(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Status(models.Model):
    status = models.CharField(max_length=50) # يتيم و مريض و ....
    def __str__(self):
        return self.status
class Case(models.Model):
    name = models.CharField(max_length=50) # يتيم و مريض و ....
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    notes = models.TextField(max_length=1000,null=True,blank=True)
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name + " " + self.status.status

@receiver(post_save, sender=Item)
def create_available(sender, instance, created, **kwargs):
    if created:
        Available.objects.create(item=instance)
        # Inbound.objects.create(item=instance)
        # Outbound.objects.create(item=instance)

class InOutCommon(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True,blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='inoutbound_files/', null=True,blank=True) # it should be a separated table
    notes = models.TextField(max_length=1000,null=True,blank=True)

class Inbound(InOutCommon):
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE, null=True,blank=True)
    
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

class Outbound(InOutCommon):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True,blank=True)
    
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



import json
from django.db import models

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     data = models.TextField()

#     def set_data(self, data):
#         self.data = json.dumps(data)

#     def get_data(self):
#         return json.loads(self.data)

# # Create a new instance of MyModel with dynamic data
# my_model = MyModel(name='John')
# my_model.set_data({'field1': 'value1', 'field2': 'value2'})
# my_model.save()

# # Query the model
# results = MyModel.objects.filter(name='John')
# for result in results:
#     print(result.get_data())