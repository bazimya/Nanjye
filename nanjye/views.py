from django.shortcuts import render, redirect
from .forms import ProfileForm, Payment
from .models import product,image,welcomeimages,PaymentForm
import requests
import random
import pyrebase
from django.contrib import auth

from firebase_admin import db




config = {
  'apiKey': "AIzaSyAnVD-q-m4uZyu_KPVNALfqKlbS_X8GP8U",
  'authDomain': "truckerapk.firebaseapp.com",
  'databaseURL': "https://truckerapk.firebaseio.com",
  'projectId': "truckerapk",
  'storageBucket': "truckerapk.appspot.com",
  'messagingSenderId': "826080710457",
  'appId': "1:826080710457:web:441f70cdc2cfa7be"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
 
def signin(request):
   # sigin firbase
   return render(request,'sigin.html')
def postsign(request):
   email = request.POST.get('name')
   paswd = request.POST.get('password')
   # Get a database reference to our posts
   ref = db.reference('server/saving-data/fireblog/DriversInformation')

   # Read the data at the posts reference (this is a blocking operation)
 
   try:
      user = authe.sign_in_with_email_and_password(email,paswd)
    
      
   except:
      message = "invalid cerediantials"
      return render(request,"sigin.html",{"msg":message})
      session_id=user['idToken']

      request.session['uid']=str(session_id)


   return render(request,'fromfirebase.html',{'email':email})

def signup(request):
   return render(request,'registeration.html')

def postsignup(request):

    fname=request.POST.get('fname')
    Phone=request.POST.get('Phone')
    email=request.POST.get('email')
    passw=request.POST.get('pswd')

   
    
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        print(uid)
      
        data={"email":email,"fname":fname,"Phone":Phone,}
        database.child("DriversInformation").child(uid).set(data)
        name = database.child('DriversInformation').child(a).child('fname').get().val()
      
        idtoken =request.session['uid']
        a= auth.get_account_info(idtoken)
        a = a['users']
        a = a[0]
        a = a['localId']
        print("info"+str(a))

    except:
        message="Unable to create account try again"
        return render(request,"registeration.html",{"messg":message})
        

    
    return render(request,"sigin.html")



def logout(request):
   auth.logout(request)
   return render(request,'sigin.html')
   # fire base only
def index(request):
   
   imgWelcome =welcomeimages.objects.all()

   return render(request, 'index.html',{'imgWelcome':imgWelcome})
def search_results(request ):

    if 'article' in request.GET and request.GET["product"]:
       
        search_term = request.GET.get("article")

        searched_articles = product.search_by_title(search_term)
 
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})


def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyProfileForm = ProfileForm(request.POST, request.FILES)
      
      if MyProfileForm.is_valid():
         workers = workers()
         workers.fname = MyProfileForm.cleaned_data["fname"]
         workers.lname = MyProfileForm.cleaned_data["lname"]
         workers.phone = MyProfileForm.cleaned_data["phone"]
         workers.NID_PASSPORT = MyProfileForm.cleaned_data["NID_PASSPORT"]
         workers.location = MyProfileForm.cleaned_data["location"]
         workers.profilProfileforme = MyProfileForm.cleaned_data["profile"]
         # Profileform
         workers.save()
         saved = TrueProfileform
   else:
      MyProfileForm = Profileform()
		
   return render(request, 'saved.html', locals())
def article(request,id):
   articles = product.objects.get(pk = id)
   MyPaymentForm = Payment() 
   return render(request,"all-news/article.html", {"articles":articles, "MyPaymentForm":MyPaymentForm})

def capenter(request):

   images_ofproduct=image.objects.all()
   print(images_ofproduct)

   return render(request,"capentry.html",{'images_ofproduct':images_ofproduct})
def productwe(request):
   return render(request,"product.html")

def SavePayment(request):
   saved = False
   data = {}
   hashed = random.randint(0,1000000)
   if request.method == "POST":
      #Get the posted form
      MyPaymentForm = Payment(request.POST, request.FILES)
      # print(MyPaymentForm.is_valid())
      if MyPaymentForm.is_valid():
         # workers = workers()
         payment = MyPaymentForm.save(commit=False)
         data['amount'] = payment.amount
         data['phonenumber'] = payment.phonenumber
         data['clienttime'] = '1556616823718'
         data['action'] = "deposit"
         data['appToken'] = "9563d7e60dc40e0315bc"
         data['hash'] = hashed
         payment.transaction_code = hashed
         # print(data)
         payment.save()
         print(payment.id)
         PaymentForm.objects.filter(id=payment.id).first()
         payload = data
         url = "https://uplus.rw/bridge/"
         requests.post(url, data=payload)
         return redirect('welcome')