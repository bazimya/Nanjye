from django.shortcuts import render, redirect
from .forms import ProfileForm, Payment
from .models import product,image,welcomeimages,PaymentForm

def index(request):
   
   imgWelcome =welcomeimages.objects.all()

   return render(request, 'index.html',{'imgWelcome':imgWelcome})

def contact(request):
    imgWelcome =welcomeimages.objects.all()

    return render(request, 'contact.html',{'imgWelcome':imgWelcome})
def smartphone(request):
    imgWelcome =welcomeimages.objects.all()
    return render(request,"smartphone.html",{'imgWelcome':imgWelcome})
def article(request,article_id):
    try:
        article = welcomeimages.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})