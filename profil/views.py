from django.shortcuts import render
from django.http import JsonResponse
from  profil.models import Profile 

# Create your views here.

def  index(request):
    return render (request  , "index.html")  
    
def  detail(request,  user_id ):
    profile =  Profile.objects.get(id=user_id)
    return render(request ,  "detail.html", {"profile" : profile })
def update_email(request) :
    print request.POST
    
    if request.method == 'POST':
        email=request.POST.get('email')
        profile_id  = request.POST.get('id') 
        print "email : " , email , "id : ", profile_id 

    p = Profile.objects.get(id=1)
    p.adresse_email = email  
    p.save(update_fields = ["adresse_email"])
    return JsonResponse({'email':email})