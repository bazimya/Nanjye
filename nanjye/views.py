from django.shortcuts import render, redirect
from .forms import ProfileForm, PaymentForm
from .models import product,image,welcomeimages
import requests
import random

def index(request):
   
   imgWelcome =welcomeimages.objects.all()

   return render(request, 'index.html',{'imgWelcome':imgWelcome})
def search_results(request ):

    if 'article' in request.GET and request.GET["product"]:
        print(search_term)
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
   data = {}
   if request.method == "POST":
      #Get the posted form
      MyPaymentForm = PaymentForm(request.POST, request.FILES)
      print(MyPaymentForm.is_valid())
      if MyPaymentForm.is_valid():
         # workers = workers()
         data['amount'] = MyPaymentForm.cleaned_data["amount"]
         data['phonenumber'] = MyPaymentForm.cleaned_data["phonenumber"]
         data['clienttime'] = "1556616823718"
         data['action'] = "liquidate"
         data['action'] = "deposit"
         data['appToken'] = "9563d7e60dc40e0315bc"
         data['hash'] = random.randint(0,1000000)
         # workers.save()
         payload = data
         print(payload)
         url = "https://uplus.rw/bridge/"
         requests.post(url, data=payload)
         return redirect('welcome')
   else:
      MyPaymentForm = PaymentForm() 
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
   if request.method == "POST":
      #Get the posted form
      MyPaymentForm = PaymentForm(request.POST, request.FILES)
      print(MyPaymentForm.is_valid())
      if MyPaymentForm.is_valid():
         # workers = workers()
         data['amount'] = MyPaymentForm.cleaned_data["amount"]
         data['phonenumber'] = MyPaymentForm.cleaned_data["phonenumber"]
         data['clienttime'] = MyPaymentForm.cleaned_data["clienttime"]
         data['action'] = "deposit"
         data['appToken'] = "9563d7e60dc40e0315bc"
         data['hash'] = random.randstr(0,1000000)
         # workers.save()
         payload = data
         print(payload)
         url = "https://uplus.rw/bridge/"
         requests.post(url, data=payload)
         return redirect('welcome')