from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from change_lives_app1.models import Signup,Contact,Registration
from django.conf import settings
import stripe
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutt(request):
    return render(request,'about.html')

def contactt(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('sub')
        text=request.POST.get('textarea')
        
        contact=Contact(name=name,email=email,ph_no=phone,subject=subject,message=text)
        contact.save()

        if contact is not None:
            messages.success(request,"your data has been saved securly")
            return redirect('index')
        
    return render(request,'contact.html')

def loginn(request):
    if request.method=='POST':
        user=request.POST.get('user_login')
        password=request.POST.get('password_login')
        print(password)
        user =authenticate(username=user
                           ,password=password)
        
        if user is not None:
            login(request,user)
            return render(request,'success.html')
        else:
            return redirect('about')
    return render(request,'index.html')
        
def logoutt(request):
    logout(request)
    return redirect('index')

def signupp(request):
    if request.method=='POST':
        user=request.POST.get('userr')
        email=request.POST.get('emaill')
        password=request.POST.get('password')
        
        # signupp=Signup(user=user,email=email,password=password)\
        myuser=User.objects.create(username=user,email=email)
        myuser.set_password(password)
        
        if myuser is not None:
            login(request,myuser)
        # signupp.save()
            myuser.save()
        messages.success(request,"your data has been saved")
    return render(request,'payment.html')

def success(request):
    return render(request,'success.html')   
        
    
# old payment method


# def payment(request):
#     stripe.api_key=settings.STRIPE_PRIVATE_KEY
#     session=stripe.checkout.Session.create(payment_method_types=['card'],
#             line_items=[{
#                 'price':'price_1Mn3zNSB9lTxkE9Qe0S0uTun',
#                 'quantity':1,
#             }],
#             mode='payment',
#             success_url=request.build_absolute_uri(reverse('contact')),
#             cancel_url=request.build_absolute_uri(reverse('index')),)
#     context={
#         'session_id':session.id,
#         'stripe_public_key':settings.STRIPE_PUBLIC_KEY
#         }
#     return render(request,'payment.html',context)

def registrationn(request):
    if request.method=="POST":
        name=request.POST.get('name')
        registration_no=request.POST.get('registration_no')
        phone_no=request.POST.get('phone_no')
        state=request.POST.get('state')
        document=request.POST.get('document')
        email=request.POST.get('email_regist')
        password=request.POST.get('password_regist')
        author_name=request.POST.get('author_name')
        
        registration=Registration(name=name,registration_no=registration_no,phone_no=phone_no,state=state,document=document,email=email,password=password,author_name=author_name)
        registration.save()
        
        if registration is not None:
            messages.success(request,'Your registration is succefully completed!!')
            return render(request,'index.html')
        else:
            return render(request,'about.html')
        
    return render(request,'registration.html')
    
    
    
def payment(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    if request.method == "POST":
            amount = int(request.POST["amount"]) 
                #Create customer
            try:
                customer = stripe.Customer.create(
			                           email=request.POST.get("email"),
			                           name=request.POST.get("full_name"),
			                           description="Test donation",
                                    source=request.POST['stripeToken']
			                           )

            except stripe.error.CardError as e:
                return HttpResponse("<h1>There was an error charging your card:</h1>"+str(e))     

            except stripe.error.RateLimitError as e:
                     # handle this e, which could be stripe related, or more generic
                return HttpResponse("<h1>Rate error!</h1>")

            except stripe.error.InvalidRequestError as e:
                return HttpResponse("<h1>Invalid requestor!</h1>")

            except stripe.error.AuthenticationError as e:  
                return HttpResponse("<h1>Invalid API auth!</h1>")

            except stripe.error.StripeError as e:  
                return HttpResponse("<h1>Stripe error!</h1>")

            except Exception as e:  
                pass  



                #Stripe charge 
            charge = stripe.PaymentIntent.create(
                       customer=customer,
			              amount=int(amount)*100,
			              currency='inr',
			              description="Test donation"
                     ) 
            transRetrive = stripe.PaymentIntent.retrieve(
                           charge["id"],
                           api_key="sk_test_51Mn3vTSB9lTxkE9QXNVfmKrpK2Biav5SxinzixgQOgxXjkODLvjCYBiCkhJctdE0G6i3HTU0rPqzcan1GtJiQOUx001bFFtbDl"
                        )
            charge.save() # Uses the same API Key.
            return redirect("success")

                   


    return render(request, "payment.html")