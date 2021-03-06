from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)

def signup1(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['contact']
        e = request.POST['email']
        p = request.POST['pwd']
        r = request.POST['role']
        try:
            user = User.objects.create_user(username=e,password=p,first_name=f,last_name=l)
            Signup.objects.create(user=user,contact=c,role=r)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'signup.html', d)

def Logout(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    d = {'data':data, 'user':user}
    return render(request, 'profile.html', d)

@login_required
def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user = user)
    error = False
    if request.method == 'POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        c=request.POST['contact']
        u=request.POST['username']
        user.first_name = f
        user.last_name = l
        data.contact = c
        user.username = u
        user.save()
        data.save()
        error=True
    d = {'data':data, 'user':user, 'error':error}
    return render(request, 'edit_profile.html', d)

@login_required
def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method == 'POST':
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c==n:
            u = User.objects.get(username__exact = request.user.username)
            u.set_password(n)
            u.save()
            error="no"
        else:
            error="yes"
    d={'error':error}
    return render(request, 'changepassword.html',d)

@login_required
def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        b = request.POST['branch']
        s = request.POST['subject']
        n = request.FILES['notesfile']
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=u,uploadingdate=date.today(),branch=b,subject=s,notesfile=n,filetype=f,description=d,status="pending")
        
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request, 'upload_notes.html', d)


def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_admin.html', d)

@staff_member_required(login_url='/login_admin/')
def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    p = Notes.objects.filter(status="pending").count()
    a = Notes.objects.filter(status="Accept").count()
    r = Notes.objects.filter(status="Reject").count()
    all = Notes.objects.all().count()
    d = {'p':p,'a':a,'r':r,'all':all}
    return render(request, 'admin_home.html',d)

@login_required
def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(status="Accept")
    
    d = {'notes':notes}
    return render(request, 'view_mynotes.html',d)

@staff_member_required(login_url='/login_admin/')
def delete_mynotes(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')

@staff_member_required(login_url='/login_admin/')
def view_users(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    users = Signup.objects.all()
    
    d = {'users':users}
    return render(request, 'view_users.html',d)

@staff_member_required(login_url='/login_admin/')
def delete_user(request,pid):
    if not request.user.is_staff:
        return redirect('view_users')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('view_users')

@staff_member_required(login_url='/login_admin/')
def pending_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')

    notes = Notes.objects.filter(status="pending")
    
    d = {'notes':notes}
    return render(request, 'pending_notes.html',d)

@staff_member_required(login_url='/login_admin/')
def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')

    notes = Notes.objects.filter(status="Accept")
    
    d = {'notes':notes}
    return render(request, 'accepted_notes.html',d)

@staff_member_required(login_url='/login_admin/')
def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')

    notes = Notes.objects.filter(status="Reject")
    
    d = {'notes':notes}
    return render(request, 'rejected_notes.html',d)

@staff_member_required(login_url='/login_admin/')
def all_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')

    notes = Notes.objects.all()
    
    d = {'notes':notes}
    return render(request, 'all_notes.html',d)

@staff_member_required(login_url='/login_admin/')
def assign_status(request,pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        s = request.POST['status']
        try:
            notes.status = s
            notes.save()
            error="no"
        except:
            error="yes"
    d={'notes':notes,'error':error}
    return render(request, 'assign_status.html', d)

@login_required
def delete_notes(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('all_notes')