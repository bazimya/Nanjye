from django.shortcuts import render
from .forms import ProfileForm
from .models import product,image,welcomeimages

def index(request):
   user= product.objects.all()
   imgWelcome =welcomeimages.objects.all()

   return render(request, 'index.html',{'user':user,'imgWelcome':imgWelcome})
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
         workers.profile = MyProfileForm.cleaned_data["profile"]
        
         workers.save()
         saved = True
   else:
      MyProfileForm = Profileform()
		
   return render(request, 'saved.html', locals())
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})

def capenter(request):

   images_ofproduct=image.objects.all()
   print(images_ofproduct)

   return render(request,"capentry.html",{'images_ofproduct':images_ofproduct})