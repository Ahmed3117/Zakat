from django.utils import timezone
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission





class Home(models.Model):
    manager_name = models.CharField(max_length=70,verbose_name = "اسم المدير")
    manager_phone = models.CharField(max_length=15,verbose_name = "تليفون المدير")
    manager_mail = models.CharField(max_length=30,verbose_name = "ايميل المدير")
    manager_address = models.CharField(max_length=70,verbose_name = "عنوان المدير")
    manager_title = models.CharField(max_length=70,verbose_name = " عنوان الموقع")
    manager_caption1 = models.CharField(max_length=200,verbose_name = "كلمة معبرة اولى ")
    manager_caption2 = models.CharField(max_length=300,verbose_name = "كلمة معبرة ثانية ")
    class Meta:
        verbose_name_plural = 'معلومات الصفحة الرئيسية'
        verbose_name = 'معلومة الصفحة الرئيسية'
    def __str__(self):
        return self.manager_name

class Category(models.Model):
    name = models.CharField(verbose_name = "التصنيف",max_length=50)
    class Meta:
        verbose_name = "التصنيف"
        verbose_name_plural = "التصنيف"
    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE , null=True,blank=True,verbose_name = "التصنيف")
    name = models.CharField(max_length=50,verbose_name='اسم العنصر')
    class Meta:
        verbose_name_plural = 'عناصر تبرع'
        verbose_name = 'عنصر تبرع'
    def __str__(self):
        return self.name

@receiver(post_save, sender=Item)
def create_available(sender, instance, created, **kwargs):
    if created:
        Available.objects.create(item=instance)


class Donator(models.Model):
    name = models.CharField(max_length=50,verbose_name='اسم المتبرع')
    class Meta:
        verbose_name_plural = 'المتبرع'
        verbose_name = 'متبرع'
    def __str__(self):
        return self.name
    
class Status(models.Model):
    status = models.CharField(max_length=50,verbose_name="سبب الاعانة") # يتيم و مريض و ....
    class Meta:
        verbose_name_plural = 'اسباب الاعانات'
        verbose_name = 'سبب اعانة'
    def __str__(self):
        return self.status
    
class CaseLevel(models.Model):
    caselevel = models.CharField(max_length=50,verbose_name="درجة الحالة") #  ,مؤقته , حرجة,متوسطة و طارئة و ....
    class Meta:
        verbose_name_plural = ' درجة الحالة'
        verbose_name = ' درجة حالة'
    def __str__(self):
        return self.caselevel

class Case(models.Model):
    defaultcaselevel = CaseLevel.objects.first().caselevel
    name = models.CharField(max_length=50,verbose_name = "اسم الحالة")
    caselevel = models.ForeignKey(CaseLevel, on_delete=models.CASCADE,verbose_name = "درجة الحالة" ,default =defaultcaselevel)
    status = models.ForeignKey(Status, on_delete=models.CASCADE,verbose_name = "سبب الاعانة")
    notes = models.TextField(max_length=1000,null=True,blank=True,verbose_name = " ملاحظات")
    date_added = models.DateTimeField(auto_now=True,verbose_name = " تاريخ الاضافة")
    def distribtionamount(self):
        ammount_for_one_person = Distribution.objects.get(caselevel=self.caselevel).ammount_for_one_person()
        return ammount_for_one_person
    distribtionamount.short_description = 'الكمية الشهرية'
    class Meta:
        verbose_name_plural = 'الحالات'
        verbose_name = 'حالة'
    def __str__(self):
        return self.name 

class MonthPay(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE,verbose_name = " الحالة" )
    month_date = models.DateTimeField(auto_now=True,verbose_name = " تاريخ الشهرية")
    file = models.FileField(upload_to='month_pay_files/', null=True,blank=True,verbose_name = " ملفات توثيق الورود")
    notes = models.TextField(max_length=1000,null=True,blank=True,verbose_name = " ملاحظات")
    def distribtionamount(self):
        return self.case.distribtionamount()
    distribtionamount.short_description = 'الكمية الشهرية'
    class Meta:
        verbose_name_plural = 'الشهريات'
        verbose_name = 'شهرية'
    def __str__(self):
        return self.case.name 

@receiver(post_save, sender=Case)
def create_distripution(sender, instance, created, **kwargs):
    if created:
        DistributionWatcher.objects.create(case=instance)


class Place(models.Model):
    place = models.CharField(max_length=100,null=True,blank=True,verbose_name = " محل التخزين")
    class Meta:
        verbose_name_plural = 'اماكن التخزين'
        verbose_name = 'مكان تخزين'
    def __str__(self):
        return self.place 

class InOutCommon(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,verbose_name = " العنصر")
    quantity = models.IntegerField(default=0,verbose_name = " الكمية")
    date = models.DateTimeField(default=timezone.now ,verbose_name = " التاريخ")
    file = models.FileField(upload_to='inbound_files/', null=True,blank=True,verbose_name = " ملفات توثيق الورود")
    notes = models.TextField(max_length=1000,null=True,blank=True,verbose_name = " ملاحظات")

class Inbound(InOutCommon):
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE, null=True,blank=True,verbose_name = " المتبرع")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True,blank=True,verbose_name = " مكان التخزين")
    
    class Meta:
        verbose_name_plural = 'الوارد'
        verbose_name = 'الوارد'
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
    def item_category(self):
        return self.item.category
    item_category.short_description = 'التصنيف'
    def __str__(self):
        return self.item.name + str(self.quantity)

class Outbound(InOutCommon):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True,blank=True,verbose_name = " الحالة الصادر لها")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True,blank=True,verbose_name = " مكان التخزين")

    class Meta:
        verbose_name_plural = 'الصادر'
        verbose_name = 'صادر'
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
    def item_category(self):
        return self.item.category
    item_category.short_description = 'التصنيف'
    def __str__(self):
        return self.item.name + str(self.quantity)

class Available(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,verbose_name = " العنصر")
    available_quantity = models.IntegerField(default=0,verbose_name = " الكمية المتاحة")
    def item_category(self):
        return self.item.category
    item_category.short_description = 'التصنيف'
    class Meta:
        verbose_name_plural = 'كميات العناصر المتاحة'
        verbose_name = 'كمية متاحة'

    def __str__(self):
        return f"{self.item.name} ({self.available_quantity})"

class Distribution(models.Model):
    caselevel = models.ForeignKey(CaseLevel, on_delete=models.CASCADE,verbose_name = "درجة الحالة" )
    ammount_money = models.IntegerField(default=0,verbose_name = "  صرفية مالية")
    def ammount_for_one_person(self):
        cases= Case.objects.filter(caselevel=self.caselevel).count()
        ammount_money_for_caselevel= self.ammount_money
        ammount_for_one_person = ammount_money_for_caselevel/cases
        return ammount_for_one_person
    ammount_for_one_person.short_description = ' الكمية للشخص الواحد'

    def save(self, *args, **kwargs):
        # check if the object already exists
        existing = Distribution.objects.filter(caselevel=self.caselevel).first()
        if existing:
            # update the existing object
            existing.ammount_money = self.ammount_money
            existing.save()
        else:
            # create a new object
            super(Distribution, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'شهريات مالية'
        verbose_name = 'شهرية مالية'
    def __str__(self):
        return f"{self.caselevel.caselevel} ({self.ammount_money})"
    
class DistributionWatcher(models.Model):
    # monthpay = models.ForeignKey(Case, on_delete=models.CASCADE,verbose_name = " الحالة" ) 
    case = models.ForeignKey(Case, on_delete=models.CASCADE,verbose_name = " الحالة" ) # الشهرية
    def distribtionamount(self):
        ammount = Distribution.objects.get(caselevel=self.case.caselevel).ammount_money
        cases = Case.objects.filter(caselevel=self.case.caselevel).count()
        return ammount/cases
    def status(self):
        return self.case.status.status
    def caselevel(self):
        return self.case.caselevel.caselevel
    distribtionamount.short_description = 'الكمية الشهرية'
    status.short_description = 'سبب الاعانة'
    caselevel.short_description = 'درجة الحالة'
    class Meta:
        verbose_name_plural = 'متابعة الشهريات'
        verbose_name = 'شهرية'
    def __str__(self):
        return self.case.name
        # return f"{self.caselevel.caselevel} ({self.ammount_money})"



