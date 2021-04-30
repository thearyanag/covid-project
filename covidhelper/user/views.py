from django.http import request
import itertools
from django.http import HttpResponse
# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import *

def IndexView(request):
    if request.method == "POST":
        user=request.POST['user']
        city=request.POST['city']
        beds=request.POST['bed']
        ventilator=request.POST['ventilator']
        icu=request.POST['icu']
        oxygen=request.POST['oxygen']
        tests=request.POST['tests']
        fabiblu=request.POST['fabiblu']
        remdesivir=request.POST['remdesivir']
        favipiravir=request.POST['favipiravir']
        plasma=request.POST['plasma']
        food=request.POST['food']
        tocilizumab=request.POST['tocilizumab']
        passer=dict(itertools.islice(request.POST.items(),1,len(request.POST)+1))
        
        if(user == 'P'):
            return render(request , 'user/index.html' , {'values':passer})

        if(user == 'R'):
            posts=PostDetails.objects.filter(city__contains=city)
            q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=None
            final=None
            count=0
            if beds=='True':
                print("Hey")
                q1=posts.filter(bed=True)
            if oxygen=='True':
                print("Hey")
                q2=posts.filter(oxygen=True)
            if ventilator=='True':
                print("Hey")
                q3=posts.filter(ventilator=True)
            if tests=='True':
                print("Hey")
                q4=posts.filter(tests=True)           
            if fabiblu=='True':
                print("Hey")
                q5=posts.filter(fabiflu=True)
            if remdesivir=='True':
                print("Hey")
                q6=posts.filter(remdesivir=True)
            if favipiravir=='True':
                print("Hey")
                q7=posts.filter(favipiravir=True)
            if tocilizumab=='True':
                print("Hey")
                q8=posts.filter(tocilizumab=True) 
            if plasma=='True':
                print("Hey")
                q9=posts.filter(plasma=True)
            if food=='True':
                print("Hey2")
                q10=posts.filter(food=True) 
            if(q1==None and q2==None and q3 == None and q4==None and q5==None and q6 == None and q7 == None and q8 == None and q9 == None and q10 ==None):
                final={'stat' : '404'}
            else:
                if(q1 != None):
                    if count==0:
                        final=q1
                        count=count+1
                    else:
                        final=final | q1  
                    print(final)                    
                if(q2 != None):
                    if count==0:
                        final=q2
                        count=count+1
                    else:
                        final=final | q2
                    print(final)                    
                if(q3 != None):
                    if count==0:
                        final=q3
                        count=count+1
                    else:
                        final=final | q3
                if(q4 != None):
                    if count==0:
                        final=q4
                        count=count+1
                    else:
                        final=final | q4                       
                if(q5 != None):
                    if count==0:
                        final=q5
                        count=count+1
                    else:
                        final=final | q5
                if(q6 != None):
                    if count==0:
                        final=q6
                        count=count+1
                    else:
                        final=final | q6
                if(q7 != None):
                    if count==0:
                        final=q7
                        count=count+1
                    else:
                        final=final | q7                       
                if(q8 != None):
                    if count==0:
                        final=q8
                        count=count+1
                    else:
                        final=final | q8
                if(q9 != None):
                    if count==0:
                        final=q9
                        count=count+1
                    else:
                        final=final | q9                                   
                if(q10 != None):
                    if count==0:
                        final=q10
                        count=count+1
                    else:
                        final=final | q10                                    
        if not final: final=False
        return render(request , 'user/index.html' , {'values' : passer , 'posts' : final})

    if request.method == 'GET':
        passer={'user' : 'R'}
        return render(request , 'user/index.html' , {'values' :passer } )

def Thanks(request):
    city=request.POST['city']
    beds=request.POST['bed']
    ventilator=request.POST['ventilator']
    icu=request.POST['icu']
    oxygen=request.POST['oxygen']
    tests=request.POST['tests']
    icu=request.POST['icu']
    fabiblu=request.POST['fabiblu']
    remdesivir=request.POST['remdesivir']
    favipiravir=request.POST['favipiravir']
    plasma=request.POST['plasma']
    food=request.POST['food']
    tocilizumab=request.POST['tocilizumab']
    contactname=request.POST['contactperson']
    contactinfo=request.POST['contactdetails']
    if "@" in contactinfo:
        PostDetails.objects.create(city=city , bed=beds , ventilator=ventilator , icu=icu , oxygen=oxygen , tests=tests , fabiflu=fabiblu , remdesivir=remdesivir , favipiravir=favipiravir , plasma=plasma , food=food , tocilizumab=tocilizumab , contactperson=contactname , mailid=contactinfo).save()    
    else:
        PostDetails.objects.create(city=city , bed=beds , ventilator=ventilator , icu=icu , oxygen=oxygen , tests=tests , fabiflu=fabiblu , remdesivir=remdesivir , favipiravir=favipiravir , plasma=plasma , food=food , tocilizumab=tocilizumab , contactperson=contactname , phone=contactinfo).save()    

    return HttpResponse("<h1>Thanks for your contribution</h1>")