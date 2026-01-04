from django.shortcuts import render
from django.http import HttpResponse,Http404

users = [
    {"name":"shadi",
     "lastname":"mehnati",
     "city":"teh",
     "phone":"0900",
     },
    {"name":"mahshad",
     "lastname":"mehnati",
     "city":"golpa",
     "phone":"0901",
     },
    {"name":"davood",
     "lastname":"mehnati",
     "city":"esf",
     "phone":"0902",
     },  
    { "name":"soghra",
     "lastname":"zare",
     "city":"esf",
     "phone":"0913",
     }
]
def userlist(request):
    return render(request,'accounts/userlist.html', context={'userlist': users})
def profile(request, username):
    for user in users:
        if user['username']==username:
            return render(request,'accounts/profile.html',context={"users": user})
    return Http404('this user not exist')