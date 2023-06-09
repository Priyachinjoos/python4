from django.http import HttpResponse
from django.shortcuts import render
from . models import Travel

# Create your views here.
def demo(request):
    obj=Travel.objects.all()

    return render(request,"index.html",{'result':obj})
# def function(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     result1=x+y
#     result2=x-y
#     result3=x*y
#     result4=x/y

    # return render(request,"about.html",{'result1':result1,'result2':result2,'result3':result3,'result4':result4})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse ("hi am contact")
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse ("this is thanks page, thanks for watching")