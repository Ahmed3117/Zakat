

from django.contrib import admin
from .models import Case, Item,Home,Inbound,Category, MonthPay, Outbound, Available,Donator, Status,Place,DistributionWatcher,CaseLevel,Distribution
from django.forms import ModelForm
from django.forms.widgets import ClearableFileInput


from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html



admin.site.register(Category)



class QuantityRangeFilter(admin.SimpleListFilter):
    title = 'كمية ما بين'
    parameter_name = 'quantity_range'

    def lookups(self, request, model_admin):
        # Define the lookup choices for the filter
        return (
            ('0-100', '0 - 100'),
            ('101-200', '101 - 200'),
            ('201-500', '201 - 500'),
            ('501+', '501 او اكثر'),
        )

    def queryset(self, request, queryset):
        # Apply the filter to the queryset
        if self.value():
            range_start, range_end = self.value().split('-')
            if range_end == '+':
                try:
                    queryset = queryset.filter(quantity__gte=int(range_start))
                except:
                    queryset = queryset.filter(available_quantity__gte=int(range_start))
            else:
                try:
                    queryset = queryset.filter(quantity__range=(int(range_start), int(range_end)))
                except:
                    queryset = queryset.filter(available_quantity__range=(int(range_start), int(range_end)))

        return queryset

 

admin.site.register(Home)
admin.site.register(Place)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('category','name')
    list_filter = ('category','name')
    search_fields = ('category__name','name')
    ordering = ('category','name')
    list_per_page = 10
    list_editable = ('name',)

admin.site.register(Item, ItemAdmin)

class DonatorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 10
admin.site.register(Donator, DonatorAdmin)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    list_filter = ('status',)
    search_fields = ('status',)
    ordering = ('status',)
    list_per_page = 10
admin.site.register(Status, StatusAdmin)

from django.template.context_processors import csrf
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name','status','caselevel', 'date_added','distribtionamount','addmonth', 'monthdetails')
    list_filter = ('name','status__status','caselevel__caselevel', 'date_added')
    search_fields = ('name','caselevel__caselevel','status__status')
    ordering = ('name','status', 'date_added')
    list_per_page = 10
    list_editable = ()
    change_list_template = 'admin/zakah/Case/change_list.html'

    def addmonth(self, obj):
        case_id = obj.id
        csrf_token = csrf(self.request)['csrf_token']
        url = reverse('zakah:addmonth', args=[case_id])

        return format_html('''
            <a class="button btn rounded-pill main-btn" data-bs-toggle="modal" data-bs-target="#showcasesdistribution-{0}">اضف شهرية</a>

            <div class="modal" dir="ltr" id="showcasesdistribution-{0}" tabindex="-1" aria-labelledby="showcasesdistribution-{0}" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="showcasesdistributionLabel-{0}">اضف شهرية</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <form action="{1}" id="add-month-form-{0}" method="POST" enctype="multipart/form-data">
                                <input type="hidden" name="csrfmiddlewaretoken" value="{2}">
                                <div class="mb-3">
                                    <label for="fileInput-{0}" class="form-label">اختر ملف</label>
                                    <input type="file" class="form-control" id="fileInput-{0}" name="monthfile">
                                </div>
                                <div class="mb-3">
                                    <label for="textInput-{0}" class="form-label">ملاحظات</label>
                                    <input type="text" class="form-control" id="textInput-{0}" name="notes">
                                </div>
                                <button type="submit" class="btn btn-primary">اضف</button>
                            </form>
                        </div>
                        <div class="modal-footer">
                            <a class="btn btn-dark btn-sm" data-bs-dismiss="modal">الغاء</a>
                        </div>
                    </div>
                </div>
            </div>
        ''', case_id, url, csrf_token)
    
    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context=extra_context)
    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context=extra_context)
    
    def monthdetails(self, obj):
        case_id = obj.id
        url = reverse('admin:zakah_monthpay_changelist')
        url += f'?case_id={case_id}'
        return format_html('<a href="{}">تفاصيل</a>', url)

    
    monthdetails.short_description = 'تفاصيل الشهرية'
    addmonth.short_description = 'اضف شهرية'


    def DisableEditFields(self, request, queryset):
        self.list_editable = ()
    def EnableEditFields(self, request, queryset):
        self.list_editable = ('status','caselevel')

    DisableEditFields.short_description = "الغاء التعديل"  
    EnableEditFields.short_description = " تعديل"  
    actions = ['EnableEditFields','DisableEditFields']
admin.site.register(Case, CaseAdmin)

class CaseLEvelAdmin(admin.ModelAdmin):
    list_display = ('caselevel',)
    list_filter = ('caselevel',)
    search_fields = ('caselevel',)
    ordering = ('caselevel',)
    list_per_page = 10
admin.site.register(CaseLevel, CaseLEvelAdmin)

@admin.register(Inbound)
class InboundAdmin(admin.ModelAdmin):
    list_display = ('item','item_category','place','donator', 'quantity', 'date','file')
    list_filter = ('item__category','item','place__place', 'quantity', 'date', QuantityRangeFilter)
    change_list_template = 'admin/change_list.html'
    search_fields = ('item__category__name','item__name','donator__name','notes')
    ordering = ('item','place', 'quantity', 'date')
    list_per_page = 10
    list_editable = ()
    change_list_template = 'admin/zakah/Inbound/change_list.html'
    def DisableEditFields(self, request, queryset):
        self.list_editable = ()
    def EnableEditFields(self, request, queryset):
        self.list_editable = ('place','donator', 'quantity', 'date','file')

    DisableEditFields.short_description = "الغاء التعديل"  
    EnableEditFields.short_description = " تعديل"  
    actions = ['EnableEditFields','DisableEditFields']
@admin.register(Outbound)
class OutbounddAdmin(admin.ModelAdmin):
    list_display = ('item','item_category','place', 'case' ,'quantity', 'date','file')
    list_filter = ('item__category','item','place__place', 'quantity', 'case__name','case__status__status', 'date', QuantityRangeFilter)
    change_list_template = 'admin/change_list.html'
    search_fields = ('item__category__name','item__name','case__status__status')
    ordering = ('item','place','quantity', 'date')
    list_per_page = 10
    list_editable = ()
    def DisableEditFields(self, request, queryset):
        self.list_editable = ()
    def EnableEditFields(self, request, queryset):
        self.list_editable = ('place', 'case' ,'quantity', 'date','file')

    DisableEditFields.short_description = "الغاء التعديل"  
    EnableEditFields.short_description = " تعديل"  
    actions = ['EnableEditFields','DisableEditFields']
@admin.register(Available)
class AvailabledAdmin(admin.ModelAdmin):
    list_display = ('item','item_category', 'available_quantity')
    list_filter = ('item','item__category' , 'available_quantity', QuantityRangeFilter)
    change_list_template = 'admin/change_list.html'
    search_fields = ('item__name','item__category__name')
    ordering = ('item', 'available_quantity')
    list_per_page = 10
    change_list_template = 'admin/zakah/Inbound/change_list.html'
  
@admin.register(DistributionWatcher)
class DistributionWatcherAdmin(admin.ModelAdmin):
    list_display = ('case','caselevel','status','distribtionamount')
    list_filter = ()
    change_list_template = 'admin/change_list.html'
    search_fields = ('case','distribtionamount')
    list_per_page = 10
    change_list_template = 'admin/zakah/Inbound/change_list.html'
  


class DistributionAdmin(admin.ModelAdmin):
    list_display = ('caselevel', 'ammount_money', 'ammount_for_one_person')

admin.site.register(Distribution, DistributionAdmin)

class MonthPayAdmin(admin.ModelAdmin):
    list_display = ('case', 'month_date', 'file','notes','distribtionamount')

admin.site.register(MonthPay, MonthPayAdmin)