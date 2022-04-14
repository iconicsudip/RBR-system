import json
from urllib.robotparser import RequestRate
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from rmmain.models import Booking, Customer, Location,Manager, Room, Roomtype, Slotdelay, Timing
from django.contrib.auth.decorators import login_required
from datetime import date, datetime , timedelta
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        try:
            ismanager = Manager.objects.get(username=request.user)
            context = {
                'ismanager' : "Manager"
            }
            return render(request,"home.html",context)
        except:
            iscustomer = Customer.objects.get(username= request.user)
            context = {
                'iscustomer' : "Customer"
            }
            return render(request,"home.html",context)
    else:
        return render(request,"home.html")

def cancelbook(request):
    #bookidcheckemail
    if request.user.is_authenticated:
        if(request.method == "POST"):
            if(request.POST['checkemail']):
                try:
                    customer = Customer.objects.get(email=request.POST['checkemail'])
                    if(str(customer) == str(request.user)):
                        change_booking = Booking.objects.get(pk=request.POST['bookid'])
                        print(change_booking.valid)
                        change_booking.valid = False
                        change_booking.save()
                        return redirect('bookings')
                    else:
                        messages.error(request,"Username of this email id and your username not matched ,please check your email id once.")
                        return redirect('bookings')
                except:
                    messages.error(request,"Wrong email id")
                    return redirect('bookings')
            else:
                messages.error(request,"Empty fields.")
                return redirect('bookings')
        else:
            return redirect('bookings')    
    else:
        messages.error(request,"You have to login first")
        return redirect('customer_login')
    return redirect('bookings')

def bookdelete(request,id):
    bookedroom = Booking.objects.get(pk=id)
    #print(bookedroom)
    bookedroom.delete()
    return redirect('bookings')

def bookings(request):
    if request.user.is_authenticated:
        #print(request.user)
        booking_list = Booking.objects.filter(customer=Customer.objects.get(username=request.user))
        #print(booking_list)
        context = {
            'booking_list':booking_list
        }
        return render(request,'customer_bookings.html',context)
    else:
        messages.error(request,"You have to login first")
        return redirect('customer_login')

def bookroom(request,user,id):
    if request.user.is_authenticated:
        context = {
            'id':id
        }
        return render(request,'bookroom.html',context)
    else:
        messages.error(request,"Login first")
        return redirect('customer_login')
def check(request,id):
    if request.user.is_authenticated:
        if(request.method == "POST"):
            if(request.POST.get('startdate') and request.POST.get('enddate')):
                if(str(request.POST.get('startdate'))<str(date.today())):
                    messages.error(request,"You can only book room from today not before today.")
                    return redirect('bookroom',user=request.user,id=id)
                else:
                    stdt = request.POST.get('startdate')
                    endt = request.POST.get('enddate')
                    manager = Room.objects.get(pk=id).manager
                    minimumgap = Slotdelay.objects.get(manager = manager).bookbefore
                    l1 = stdt.split("-")
                    l2 = str(date.today() + timedelta(days=minimumgap)).split("-")
                    b1 = date(int(l1[0]), int(l1[1]), int(l1[2]))
                    b2 = date(int(l2[0]), int(l2[1]), int(l2[2]))
                    if(b1>b2):
                        messages.error(request,"You can only book room before "+str(minimumgap)+" day/days")
                        return redirect('bookroom',user=request.user,id=id)
                    else:
                        return redirect('bookroom',user=request.user,id=id)
            else:
                messages.error(request,"Empty fields.")
                return redirect('bookroom',user=request.user,id=id)
        else:
            return redirect('bookroom',user=request.user,id=id)
    else:
        messages.error(request,"You have to login first")
        return redirect('customer_login')    
def search(request):
    if request.user.is_authenticated:
        if(request.method == "POST"):
            if(request.POST['location']):
                try:
                    l = Location.objects.get(city =str(request.POST['location']).capitalize())
                    location = Room.objects.filter(location = l)
                    print(location)
                    if(len(location)>0):
                        context = {
                            'allrooms':location
                        }
                        return render(request,'customer_dashboard.html',context)
                    else:
                        messages.error(request,"Rooms are not present in this location")
                        return redirect('customer_dashboard',user=request.user)
                except:
                    messages.error(request,"Rooms are not present in this location")
                    return redirect('customer_dashboard',user=request.user)
            else:
                messages.error(request,"Empty fields.")
                return redirect('customer_dashboard',user=request.user)
        else:
            return redirect('customer_dashboard',user=request.user)
    else:
        messages.error(request,"Login first")
        return redirect('customer_login')

def slotrange(request):
    if request.user.is_authenticated:
        if(request.method == "POST"):
            if(request.POST['slotdelay'] and request.POST['bookbefore']):
                usr =Manager.objects.get(username=request.user)
                slot_range = Slotdelay.objects.get(manager = usr)
                slot_range.slotrange = request.POST['slotdelay']
                slot_range.bookbefore = request.POST['bookbefore']
                slot_range.save()
                print(slot_range)
                return redirect('manager_dashboard',user=request.user)
            else:
                messages.error(request,"Empty fields.")
                return redirect('manager_dashboard',user=request.user)
        else:
            return redirect('manager_dashboard',user=request.user)
    else:
        return redirect('manager_login')
def roomedit(request,user,id):
    if request.user.is_authenticated:
        if(request.method == "POST"):
            if(request.POST.get('eroomtype') and request.POST['ecapacity'] and request.POST['eprice'] and request.POST.get('estatus') and request.POST.get('elocation') and request.POST['eaddress']):
                new_data = Room.objects.get(pk=id)
                new_data.roomtype = Roomtype.objects.get(roomtype=request.POST.get('eroomtype'))
                new_data.capacity = request.POST['ecapacity']
                new_data.price = request.POST['eprice']
                new_data.status = request.POST.get('estatus')
                new_data.location = Location.objects.get(city=request.POST.get('elocation'))
                new_data.address = request.POST['eaddress']
                new_data.save()
                new_time = Timing.objects.get(roomid = id)
                new_time.smonday = request.POST.get('smonday')
                new_time.emonday = request.POST.get('emonday')
                new_time.stuesday = request.POST.get('stuesday')
                new_time.etuesday = request.POST.get('etuesday')
                new_time.swednesday = request.POST.get('swednesday')
                new_time.ewednesday = request.POST.get('ewednesday')
                new_time.sthursday = request.POST.get('sthursday')
                new_time.ethursday = request.POST.get('ethursday')
                new_time.sfriday = request.POST.get('sfriday')
                new_time.efriday =request.POST.get('efriday')
                new_time.ssaturday = request.POST.get('ssaturday')
                new_time.esaturday = request.POST.get('esaturday')
                new_time.ssunday = request.POST.get('ssunday')
                new_time.esunday = request.POST.get('esunday')
                new_time.save()
                return redirect('manager_dashboard',user=request.user)
            else:
                all_roomtypes = Roomtype.objects.all()
                locations = Location.objects.all()
                prev_data = Room.objects.get(pk=id)
                bookrange = Timing.objects.get(roomid = id)
                context = {
                    'alltypes':all_roomtypes,
                    'alllocations' : locations,
                    'prev_data' : prev_data,
                    'room_id':id,
                    'bookrange':bookrange
                }
                return render(request,'roomedit.html',context)
        else:
            all_roomtypes = Roomtype.objects.all()
            locations = Location.objects.all()
            prev_data = Room.objects.get(pk=id)
            bookrange = Timing.objects.get(roomid = id)
            print(bookrange.smonday)
            context = {
                'alltypes':all_roomtypes,
                'alllocations' : locations,
                'prev_data' : prev_data,
                'room_id':id,
                'bookrange':bookrange
            }
            return render(request,'roomedit.html',context)
    else:
        return redirect('manager_login')
def roomdelete(request,id):
    room_instance = Room.objects.get(id=id)
    print(room_instance)
    room_instance.delete()
    return redirect('manager_dashboard',user=request.user)
def addroom(request):
    if(request.method == 'POST'):
        if(request.POST.get('roomtype') and request.POST['capacity'] and request.POST['price'] and request.POST.get('status') and request.POST.get('location') and request.POST['address']):
            roomtype = request.POST.get('roomtype')
            capacity = request.POST['capacity']
            price = request.POST['price']
            status = request.POST.get('status')
            location = request.POST.get('location')
            address = request.POST['address']
            mnumber = Manager.objects.get(username=request.user).pnumber
            print(mnumber)
            room = Room(
                manager = Manager.objects.get(username = request.user),
                roomtype = Roomtype.objects.get(roomtype=roomtype),
                capacity=capacity,
                price = price,
                status = status,
                location = Location.objects.get(city=location),
                address = address,
                mnumber=mnumber
            )
            room.save()
            timing = Timing(
                manager = Manager.objects.get(username = request.user),
                roomid = Room.objects.latest('id')
            )
            timing.save()
            return redirect('manager_dashboard',user=request.user)
        else:
            messages.error(request,"Empty fields.")
            return redirect('manager_dashboard',user=request.user)
    else:
        return redirect('manager_dashboard',user=request.user)
def addlocation(request):
    if(request.method == "POST"):
        if(request.POST['city'] and request.POST['state'] and request.POST['country']):
            city = str(request.POST['city']).capitalize()
            state = str(request.POST['state']).capitalize()
            country = str(request.POST['country']).capitalize()
            print(city,state,country)
            check_state = [x[0] for x in Location.objects.filter(country=country).values_list('state').all()]
            if(state in list(check_state)):
                #print(list(check_state))
                check_city = [x[0] for x in Location.objects.filter(state=state).values_list('city').all()]
                if(city in list(check_city)):
                    print(list(check_city))
                    messages.error(request,"This location is already exists")
                    return redirect('manager_dashboard',user=request.user)
                else:
                    location = Location(
                        city = city,
                        state = state,
                        country = country
                    )
                    location.save()
                    return redirect('manager_dashboard',user=request.user)
            else:
                location = Location(
                    city = city,
                    state = state,
                    country = country
                )
                location.save()
                return redirect('manager_dashboard',user=request.user)
        else:
            messages.error(request,"Empty fields.")
            return redirect('manager_dashboard',user=request.user)
    else:
        return redirect('manager_dashboard',user=request.user)
def addroomtype(request):
    if request.method == "POST":
        if(request.POST['roomtype']):
            check_roomtype=Roomtype.objects.filter(roomtype=request.POST['roomtype']).values_list('roomtype').first()
            if(check_roomtype!=None):
                print(check_roomtype)
                messages.error(request,"This room type is already exists")
                return redirect('manager_dashboard',user=request.user)
            else:
                new_roomtype = Roomtype(
                    roomtype = request.POST['roomtype']
                )
                new_roomtype.save()
                return redirect('manager_dashboard',user=request.user)
        else:
            return redirect('manager_dashboard',user=request.user)
    else:
        return redirect('manager_dashboard',user=request.user)

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='customer_login')
def customer_dashboard(request,user):
    if request.user.is_authenticated:
        one = Customer.objects.filter(username=request.user).values_list('email',flat=True).first()
        print(one)
        two = User.objects.filter(username=user).values_list('email',flat=True).first()
        if one == two:
            return render(request,'customer_dashboard.html')
        else:
            auth.logout(request)
            return redirect('home')
    else:
        return redirect('customer_login')

@login_required(login_url='manager_login')
def manager_dashboard(request,user):
    if request.user.is_authenticated:
        one = Manager.objects.filter(username=request.user).values_list('email',flat=True).first()
        two = User.objects.filter(username=user).values_list('email',flat=True).first()
        if one == two:
            all_roomtypes = Roomtype.objects.all()
            locations = Location.objects.all()
            usr =Manager.objects.get(username=request.user)
            rooms = Room.objects.filter(manager=usr)
            slot_range = Slotdelay.objects.get(manager = usr)
            print(slot_range)
            context = {
                'alltypes':all_roomtypes,
                'alllocations' : locations,
                'rooms' : rooms,
                'slot_range':slot_range
            }
            return render(request,'manager_dashboard.html',context)
        else:
            auth.logout(request)
            return redirect('home')
    else:
        return redirect('manager_login')

def customer_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['email'] and request.POST['password']:
                try:
                    one = Customer.objects.filter(email = request.POST['email']).values_list('email',flat=True).first()
                    two = User.objects.filter(email=request.POST['email']).values_list('email',flat=True).first()
                    print(one," ",two)
                    if(one == two):
                        user = User.objects.get(email=request.POST['email'])
                        try:
                            check_user = auth.authenticate(request,username=user,password =request.POST['password'] )
                            if check_user is not None:
                                auth.login(request,user)
                                messages.success(request, "You are successfully logged in now, you can see your dashboard")
                                print("LOL")
                                return redirect('customer_dashboard',user=request.user)
                            else:
                                messages.error(request, "Invalid Credentials,Please try again")
                                return redirect("customer_login")
                        except:
                            return render(request,'customer_login.html',{'error': "Invalid credentials."})
                    else:
                        return render(request,'customer_login.html')
                except User.DoesNotExist:
                    return render(request, 'customer_login.html', {'error': "User doesn't exists."})        
            else:
                return render(request, 'customer_login.html', {'error': "Empty field occurs."})
        else:
            return render(request,'customer_login.html')
    else:
        return render(request,'customer_login.html')

def manager_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['memail'] and request.POST['mpassword']:
                try:
                    one = Manager.objects.filter(email = request.POST['memail']).values_list('email',flat=True).first()
                    two = User.objects.filter(email=request.POST['memail']).values_list('email',flat=True).first()
                    print(one," ",two)
                    if(one == two):
                        user = User.objects.get(email=request.POST['memail'])
                        try:
                            check_user = auth.authenticate(request,username=user,password =request.POST['mpassword'] )
                            if check_user is not None:
                                auth.login(request,user)
                                messages.success(request, "You are successfully logged in now, you can see your dashboard")
                                print("LOL")
                                return redirect('manager_dashboard',user=request.user)
                            else:
                                messages.error(request, "Invalid Credentials,Please try again")
                                return redirect("manager_login")
                        except:
                            return render(request,'manager_login.html',{'error': "Invalid credentials."})
                    else:
                        return render(request,'manager_login.html')
                except User.DoesNotExist:
                    return render(request, 'manager_login.html', {'error': "User doesn't exists."})        
            else:
                return render(request, 'manager_login.html', {'error': "Empty field occurs."})
        else:
            return render(request,'manager_login.html')
    else:
        return render(request,'manager_login.html')

def customer_register(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            if request.POST['password'] == request.POST['password2']:
                if(request.POST['username'] and request.POST['email'] and request.POST['password']):
                    try:
                        user = User.objects.get(email=request.POST['email'])
                        return render(request,'customer_register.html',{'error':"User already exists"})
                    except User.DoesNotExist:
                        username = request.POST['username']
                        email = request.POST['email']
                        password = request.POST['password']
                        user = User.objects.create_user(
                            username = username,
                            email = email,
                            password = password,
                        )
                        user.save()
                        auth.authenticate(request,email=email,password =password)
                        check_user = User.objects.get(email=request.POST['email'])
                        auth.login(request, check_user)
                        print(request.user)
                        customer = Customer(username=request.user,name=request.POST['fullname'],email=email)
                        customer.save()
                        messages.success(
                            request, "You are successfully logged in now, you can see your dashboard")
                        return redirect('home')
                else:
                    return render(request, 'customer_register.html', {'error': "Empty fields exist"})
            else:
                return render(request, 'customer_register.html', {'error': "Password Don't Match"})
        else:
            return render(request,"customer_register.html")
    else:
        messages.success(request, "You have to sign up")
        return render(request,"customer_register.html")

def manager_register(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            if request.POST['mpassword'] == request.POST['mpassword2']:
                if(request.POST['musername'] and request.POST['memail'] and request.POST['mpassword'] and request.POST['mnumber']):
                    try:
                        user = User.objects.get(email=request.POST['memail'])
                        return render(request,'manager_register.html',{'error':"User already exists"})
                    except User.DoesNotExist:
                        username = request.POST['musername']
                        email = request.POST['memail']
                        password = request.POST['mpassword']
                        try:
                            user = User.objects.create_user(
                                username = username,
                                email = email,
                                password = password,
                            )
                            user.save()

                        except:
                            print("USER")
                            return render(request,'manager_register.html',{'error':"User already exist on this username"})
                        auth.authenticate(request,email=email,password =password)
                        check_user = User.objects.get(email=request.POST['memail'])
                        auth.login(request, check_user)
                        print(request.user)
                        manager = Manager(username=request.user,name=request.POST['mfullname'],email=email,pnumber=request.POST['mnumber'])
                        manager.save()
                        slot_range = Slotdelay(
                            manager = Manager.objects.get(username=request.user)
                        )
                        slot_range.save()
                        messages.success(
                            request, "You are successfully logged in now, you can see your dashboard")
                        return redirect('home')
                else:
                    return render(request, 'manager_register.html', {'error': "Empty fields exist"})
            else:
                return render(request, 'manager_register.html', {'error': "Password Don't Match"})
        else:
            return render(request,"manager_register.html")
    else:
        messages.success(request, "You have to sign up")
        return render(request,"manager_register.html")

