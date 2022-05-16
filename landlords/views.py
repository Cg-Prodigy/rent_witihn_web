from django.shortcuts import render

# Create your views here.


def HomePage(request):
    context={'title':'HomePage', 'heading':'Welcome Page'}
    return render(request,'index.html',context)


def LoginSignUp(request):
    context={
        'title':'Login/Sign-Up page',
        'heading':'Login and SignUp Page'
    }
    return render(request,'landlords/login_sign.html',context)