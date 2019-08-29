from django.db.models import Q

from django.shortcuts import render
from .models import ProductDataModel
from .forms import InsertForm,UpdateForm,DeleteForm
from  django.http.response import HttpResponse

def index_view(request):
    return render(request,'index.html')

def insert_view(request):
    if request.method=='POST':
        iform=InsertForm(request.POST)
        if iform.is_valid():
            prodct_id_v=request.POST.get('product_id_f')
            product_name_v=request.POST.get('product_name_f')
            product_color_v=request.POST.get('product_color_f')
            product_cost_v=request.POST.get('product_cost_f')

            data=ProductDataModel(product_id=prodct_id_v,product_name=product_name_v,
                                  product_color=product_color_v,product_cost=product_cost_v)
            data.save()
            iform=InsertForm()
            return render(request,'insert.html',{'iform':iform})
        else:
            return HttpResponse('Invalid Data')
    else:
        iform=InsertForm()
        return render(request,'insert.html',{'iform':iform})

def retrieve_view(request):
    products=ProductDataModel.objects.all().order_by('product_id')
    return render(request,'retrieve.html',{'products':products})

def update_view(request):
    if request.method=='POST':
        uform=UpdateForm(request.POST)
        if uform.is_valid():
            product_id_v=request.POST.get('product_id_f')
            product_cost_v=request.POST.get('product_cost_f')

            product_ids=ProductDataModel.objects.all()
            pdata=ProductDataModel.objects.filter(product_id=product_id_v)
            if pdata:
                pdata.update(product_cost=product_cost_v)
                ufrom=UpdateForm()
                return render(request,'update.html',{'ufrom':ufrom})
            else:
                return HttpResponse('Invalid Product ID')
    else:
        uform=UpdateForm()
        return render(request,'update.html',{'ufrom':uform})

def delete_view(request):
    if request.method=='POST':
        ddata=DeleteForm(request.POST)
        if ddata.is_valid():
            product_id_v=request.POST.get('product_id_f')
            pdata=ProductDataModel.objects.filter(product_id=product_id_v)
            if pdata:
                pdata.delete()
                dform = DeleteForm()
                return render(request, 'delete.html', {'dfrom': dform})
            else:
                return HttpResponse('Invalid Product ID')
        else:
            return HttpResponse('Invalid Data')
    else:
        dform=DeleteForm()
        return render(request,'delete.html',{'dfrom':dform})
