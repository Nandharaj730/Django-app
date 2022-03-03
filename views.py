from urllib import response
from django.shortcuts import render
from nandhaapp.form import fillForm
from django.http import HttpRequest, HttpResponse
from nandhaapp.models import Employee 
import csv

def getFile(request):
    emp = Employee.objects.all()
    response = HttpResponse(content_type = 'text/pdf')
    response['Content-Disposition'] = 'attachment ; filename = "csvfile.pdf"'
    writer = csv.writer(response)

    for employee in emp:
        print([employee.id , employee.eid , employee.name , employee.school])
        writer.writerow([employee.id , employee.eid , employee.name , employee.school])
    
    return response


def sayHello(request):
    print(request.POST.get('eid'))
    print(request.POST.get('name'))
    print(request.POST.get('school'))

    emp = Employee()
    emp.eid = request.POST.get('eid')
    emp.name = request.POST.get('name')
    emp.school = request.POST.get('school')
    emp.save()

    return HttpResponse('good bye...!')
    
def Forms(request):
    if(request.method == 'POST'):
        fill = fillForm()

        sayHello(request)
        return render(request , 'hello.html',{'form':fill})
    else:
        fill = fillForm();
        return render(request , 'hello.html',{'form':fill})

def index(request):
    return render(request , 'index.html')