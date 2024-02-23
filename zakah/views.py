from django.shortcuts import redirect, render
from .models import Case, Home, MonthPay
# Create your views here.

def home(request):
    home_data = Home.objects.last()
    context = {
        "home_data" : home_data,
    }
    return render(request,'zakah/home.html',context)
    # return render(request,'zakah/home.html')

def addmonth(request,pk):
    case = Case.objects.get(id=pk)
    notes = request.POST.get("notes")
    file = request.FILES.get('monthfile')
    MonthPay.objects.create(case=case,file=file,notes=notes)
    return redirect('admin:zakah_case_changelist')



