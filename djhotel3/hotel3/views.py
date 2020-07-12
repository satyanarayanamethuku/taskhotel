from django.shortcuts import render
from .models import Register,Platinum
from random import *
from django.http import HttpResponse
from .forms import PlatinumForm
from django.db.models import Q
# Create your views here.


def reg(request):
    if request.method=='POST':
<<<<<<< HEAD
        print("test")
=======
        print("hey!!!")
>>>>>>> 824f68c4286fb40407515eccbb285fe17b422762
        n=''
        for i in range(0,4):
            n=n+str(randint(0,9))
        Booking1_id=n
        
        Customer_name=request.POST['t1']
        Username=request.POST['t2']
        Password=request.POST['t3']
        Membership_type=request.POST['t4']
       
        user=Register(Booking1_id=Booking1_id, Customer_name=Customer_name, Password=Password, Membership_type=Membership_type,Username=Username)
        user.save()
       
        return render(request, 'reg.html', {"msg":"your booking_id is and please note down", "msg1":user.Booking_id})
    return render(request, 'reg.html')


def login(request):
    if request.method=='POST':
        Username=request.POST['t2']
        Password=request.POST['t3']
        try:
             dbuser=Register.objects.get(Username=Username, Password=Password)
             if dbuser:
                if dbuser.Membership_type=='premium':
                     return render(request,'hotel.html')
                else:
                    return render(request,'sucess.html')
             
        except Register.DoesNotExist:
            return render(request, 'login.html',{"msg":"UserName and Password Does Not Match"})
    return render(request, 'login.html')

       
        # try:
        #     dbuser=Register.objects.get(Username=Username, Password=Password)
        #     if dbuser.Membership_type=='premium':
        #         return render(request,'hotel.html')
        #     elif dbuser.Membership_type=='non-premium':
        #         return render(request,'sucess.html')
        # except dbuser.DoesNotExist:
        #     return HttpResponse("UserName and Password Does Not Match")

    




        
        
    

def platinum(request):
    form=PlatinumForm()
    if request.method=='POST':
        form=PlatinumForm(request.POST)
        if form.is_valid():
            n=''
            for i in range(0,4):
                n=n+str(randint(0,9))    
            Booking_id=n
            User=form.cleaned_data['User']
            Check_In=form.cleaned_data['Check_In']
            Check_Out=form.cleaned_data['Check_Out']
            Room_number=form.cleaned_data['Room_number']
            Room_type=form.cleaned_data['Room_type']
            user=Platinum(Booking_id=Booking_id, User=User, Check_In=Check_In, Check_Out=Check_Out,Room_number=Room_number,Room_type=Room_type)
            user.save()
            return render(request, 'search.html')
    return render(request, 'platinum.html',{'form':form})


# def platinum(request):
#     form=PlatinumForm()
#     if request.method=='POST':
#         form=PlatinumForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request,'platinum.html',{'form':form})

# def display(request,id):
#     form=Platinum.objects.get(id=id)
    # return render(request,'display.html',{'form':form})

def display(request):
    query=request.GET['q']
    object_list=Platinum.objects.filter(Q(id__icontains=query) | Q(Room_number__icontains=query))
    return render(request,'display.html', {'form':object_list, 'data':'Premium'})






# try:
        #     dbuser=Register.objects.get(Username=Username, Password=Password)

        # except:
        #     if dbuser.Membership_type=='premium':
        #         return render(request,'hotel.html')
        #     elif dbuser.Membership_type=='non-premium':
        #         return render(request,'sucess.html')

        # except dbuser.DoesNotExist:
        #     return HttpResponse("UserName and Password Does Not Match")
    



        # elif dbuser.Membership_type=='':
        #     return render(request, 'login.html',{"msg":"UserName and Password Does Not Match"})






        # except dbuser.DoesNotExist:
        #     return HttpResponse("UserName and Password Does Not Match")
        #     # return render(request, 'login.html',{"msg":"UserName and Password Does Not Match"})


        # if not dbuser:
        #     return HttpResponse("login fail")
        # else:
        #     return render(request,'hotel.html',{'form':dbuser.Membership_type})








