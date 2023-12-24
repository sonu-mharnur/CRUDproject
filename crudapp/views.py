
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import UserData

# Create your views here.
def index(request):
    # userdata = [{'fullname': 'SAKEEB SHEIKH', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'},
    # {'fullname': 'AMOL PATIL', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'},
    # {'fullname': 'VAIBHAV S', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'},
    # {'fullname': 'SHIVANI S', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'}]

    alldata = UserData.objects.all()

    return render(request, 'index.html', context={'data': alldata})

def register(request):
    return render(request, 'register.html')

def registeruser(request):
    if request.POST:
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        username = request.POST['username']
        inputPassword = request.POST['inputPassword']
        confirmpassword = request.POST['confirmpassword']

        print(fullname, email, contact, address, username, inputPassword, confirmpassword)

        if inputPassword==confirmpassword :
            obj = UserData(fullname=fullname, emailid=email, contact=contact, address=address, username=username, password=inputPassword)
            obj.save()

            alldata = UserData.objects.all()
            return render(request, 'index.html', context={'data': alldata, 'flag':'success'})
        else:
            return render(request, 'register.html', {'flag':'invalid'})

    return render(request, 'register.html')

def deleteme(request, id):
    obj = UserData.objects.get(id=id)
    obj.delete()

    alldata = UserData.objects.all()
    return render(request, 'index.html', context={'data': alldata, 'flag':'success'})

def editme(request, id):
    if request.POST:
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']

        obj = UserData.objects.get(id=id)
        obj.fullname = fullname
        obj.emailid = email
        obj.contact = contact
        obj.address = address

        obj.save()

        alldata = UserData.objects.all()
        return render(request, 'index.html', context={'data': alldata})


    obj = UserData.objects.get(id=id)

    return render(request, 'edit.html', context={'data': obj})


def searchdata(request):

    if request.POST:
        if 'fullname' in request.POST:
            searchtext = request.POST['searchtext']
            print(request.POST['fullname'])
            fullname=True
            
            filteredobjs = UserData.objects.filter(fullname__contains=searchtext)
   
            return render(request, 'index.html', context={'data': filteredobjs})
    
    alldata = UserData.objects.all()
    return render(request, 'index.html', context={'data': alldata})