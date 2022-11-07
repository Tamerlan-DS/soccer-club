from django.shortcuts import render,redirect

def MainView(request):
    context = {

    }
    return render(request,'front/index.html',context)

def MatchesView(request):
    context = {

    }
    return render(request,'front/matches.html',context)

def PlayersView(request):
    context = {

    }
    return render(request,'front/players.html',context)

def AboutUsView(request):
    context = {

    }
    return render(request,'front/blog.html',context)

def ContactsView(request):
    context = {

    }
    return render(request,'front/contact.html',context)