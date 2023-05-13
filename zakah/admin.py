from django.contrib import admin
from .models import Case, Item,Inbound, Outbound, Available,Donator, Status
from django.forms import ModelForm
from django.forms.widgets import ClearableFileInput

class InboundForm(ModelForm):
    class Meta:
        model = Inbound
        fields = '__all__'
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }


class QuantityRangeFilter(admin.SimpleListFilter):
    title = 'Quantity range'
    parameter_name = 'quantity_range'

    def lookups(self, request, model_admin):
        # Define the lookup choices for the filter
        return (
            ('0-100', '0 - 100'),
            ('101-200', '101 - 200'),
            ('201-500', '201 - 500'),
            ('501+', '501 or more'),
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

 


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 10
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
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name','status', 'date_added')
    list_filter = ('name','status__status', 'date_added')
    search_fields = ('name','status__status')
    ordering = ('name','status', 'date_added')
    list_per_page = 10
admin.site.register(Case, CaseAdmin)

@admin.register(Inbound)
class InboundAdmin(admin.ModelAdmin):
    list_display = ('item','donator', 'quantity', 'date','file')
    list_filter = ('item', 'quantity', 'date', QuantityRangeFilter)
    change_list_template = 'admin/change_list.html'
    search_fields = ('item__name','donator__name')
    ordering = ('item', 'quantity', 'date')
    list_per_page = 10

@admin.register(Outbound)
class OutbounddAdmin(admin.ModelAdmin):
    list_display = ('item', 'case' ,'quantity', 'date','file')
    list_filter = ('item', 'quantity', 'case__name','case__status__status', 'date', QuantityRangeFilter)
    change_list_template = 'admin/change_list.html'
    search_fields = ('item__name','case__status__status')
    ordering = ('item','quantity', 'date')
    list_per_page = 10

@admin.register(Available)
class AvailabledAdmin(admin.ModelAdmin):
    list_display = ('item', 'available_quantity')
    list_filter = ('item', 'available_quantity', QuantityRangeFilter)
    change_list_template = 'admin/change_list.html'
    search_fields = ('item__name',)
    ordering = ('item', 'available_quantity')
    list_per_page = 10


