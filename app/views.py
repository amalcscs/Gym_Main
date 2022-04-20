import os
import random
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

def login(request):
    Trainer = designation.objects.get(designation="Trainer")
    Trainee = designation.objects.get(designation="Trainee")
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'SuperAdmin_index')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Trainer.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tnr_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Tnr_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'Trainer_dashboard.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Trainee.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Tne_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['Tne_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'Trainee_index.html',{'mem1':mem1})
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)
    return render(request,'login.html')

def Trainer_index(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        return render(request, 'Trainer_index.html',{'mem':mem})   
    else:
        return redirect('/')

def Trainer_dashboard(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        return render(request,'Trainer_dashboard.html',{'mem':mem})   
    else:
        return redirect('/')

def Trainer_Trainees_card(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        Traine = designation.objects.get(designation='Trainee')
        Act_count=user_registration.objects.filter(designation=Traine).filter(status="active").filter(Trainer_id=Tnr_id).count()
        Res_count=user_registration.objects.filter(designation=Traine).filter(status="resign").count()
        return render(request,'Trainer_Trainees_card.html',{'mem':mem,'Act_count':Act_count,'Res_count':Res_count})   
    else:
        return redirect('/')

def Trainer_Current_Trainees_table(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        des=designation.objects.get(designation="Trainee")
        traine=user_registration.objects.filter(designation_id=des.id).filter(Trainer_id=Tnr_id).filter(status="active")
        return render(request,'Trainer_Current_Trainees_table.html',{'mem':mem,'traine':traine})   
    else:
        return redirect('/')

def Trainer_Current_Trainees_profile(request,id):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        nam=user_registration.objects.filter(id=id)
        return render(request,'Trainer_Current_Trainee_profile.html',{'mem':mem,'nam':nam})
    else:
        return redirect('/')

def Trainer_Previous_Trainees_table(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        des=designation.objects.get(designation="Trainee")
        traine=user_registration.objects.filter(designation_id=des.id).filter(Trainer_id=Tnr_id).filter(status="resign")
        return render(request,'Trainer_Previous_Trainees_table.html',{'mem':mem,'traine':traine})
    else:
        return redirect('/')

def Trainer_Previous_Trainees_profile(request,id):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        nam=user_registration.objects.filter(id=id)
        return render(request,'Trainer_Previous_Trainee_profile.html',{'mem':mem,'nam':nam})
    else:
        return redirect('/')

def Trainer_Accsetting(request):
    if 'Tnr_id' in request.session:
        if request.session.has_key('Tnr_id'):
            Tnr_id = request.session['Tnr_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Tnr_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=Tnr_id)
            abc.fullname = request.POST.get('name')
            abc.dateofbirth = request.POST.get('dateofbirth')
            abc.gender = request.POST.get('gender')
            abc.email = request.POST.get('email')
            abc.mobile = request.POST.get('mobile')
            abc.alternativeno = request.POST.get('alt_no')
            abc.pincode = request.POST.get('pincode')
            abc.district = request.POST.get('district')
            abc.idproof = request.FILES['id_proof']
            abc.state = request.POST.get('state')
            abc.country = request.POST.get('country')
            abc.permanentaddress1 = request.POST.get('address1')
            abc.permanentaddress2 = request.POST.get('address2')
            abc.permanentaddress3 = request.POST.get('address3')
            abc.height = request.POST.get('height')
            abc.weight = request.POST.get('weight')
            abc.save()
            msg_success = "Accounts changed successfully"
            return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})
        return render(request,'Trainer_Accsetting.html',{'mem':mem})
    else:
        return redirect('/')

def Trainer_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})

def Trainer_Changepwd(request,id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})

        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('Trainer_Accsetting')

    
def Trainee_index(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        return render(request, 'Trainee_index.html',{'mem1':mem1})   
    else:
        return redirect('/')

def SuperAdmin_index(request):
    return render(request,'SuperAdmin_index.html')

def SuperAdmin_Accountsett(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        users = User.objects.filter(id=SAdm_id)
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'SuperAdmin_Accountsett.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'SuperAdmin_Accountsett.html', {'msg_error': msg_error})
        return render(request, 'SuperAdmin_Accountsett.html', {'users': users})
    else:
        return redirect('/')

def SuperAdmin_logout(request):
    request.session.flush()
    return redirect("/")

def Trainee_Accsetting(request):
    if 'Tne_id' in request.session:
        if request.session.has_key('Tne_id'):
            Tne_id = request.session['Tne_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=Tne_id)
        if request.method == 'POST':
            abb = user_registration.objects.get(id=Tne_id)
            abb.fullname = request.POST.get('name')
            abb.dateofbirth = request.POST.get('dateofbirth')
            abb.gender = request.POST.get('gender')
            abb.email = request.POST.get('email')
            abb.mobile = request.POST.get('mobile')
            abb.alternativeno = request.POST.get('alt_no')
            abb.pincode = request.POST.get('pincode')
            abb.district = request.POST.get('district')
            abb.idproof = request.FILES['id_proof']
            abb.state = request.POST.get('state')
            abb.country = request.POST.get('country')
            abb.permanentaddress1 = request.POST.get('address1')
            abb.permanentaddress2 = request.POST.get('address2')
            abb.permanentaddress3 = request.POST.get('address3')
            abb.height = request.POST.get('height')
            abb.weight = request.POST.get('weight')
            abb.save()
            msg_success = "Accounts changed successfully"
            return render(request, 'Trainee_Accsetting.html', {'msg_success': msg_success})
        return render(request,'Trainee_Accsetting.html',{'mem1':mem1})
    else:
        return redirect('/')

def Trainee_Profile_Imagechange(request,id):
    if request.method == 'POST':
        ab = user_registration.objects.get(id=id)
        ab.photo = request.FILES['files']
        ab.save()
        msg_success = "Profile Picture changed successfully"
        return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})

def Trainee_Changepwd(request,id):
    if request.method == 'POST':
        ac = user_registration.objects.get(id=id)
        oldps = request.POST['currentPassword']
        newps = request.POST['newPassword']
        cmps = request.POST.get('confirmPassword')
        if oldps != newps:
            if newps == cmps:
                ac.password = request.POST.get('confirmPassword')
                ac.save()
                msg_success = "Password changed successfully"
                return render(request, 'Trainer_Accsetting.html', {'msg_success': msg_success})
        elif oldps == newps:
            messages.add_message(request, messages.INFO, 'Current and New password same')
        else:
            messages.info(request, 'Incorrect password same')

        return redirect('Trainee_Accsetting')
    

def Trainee_logout(request):
    if 'Tne_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def Trainer_logout(request):
    if 'Tnr_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')
    

def Registration(request):
    if request.method == 'POST':
        acc = user_registration()
        acc.fullname = request.POST['name']
        acc.dateofbirth = request.POST['dateofbirth']
        acc.gender = request.POST['gender']
        acc.email = request.POST['email']
        acc.mobile = request.POST['mobile']
        acc.alternativeno = request.POST['alt_no']
        acc.pincode = request.POST['pincode']
        acc.district = request.POST['district']
        acc.idproof = request.FILES['id_proof']
        acc.photo = request.FILES['pic']
        acc.state = request.POST['state']
        acc.country = request.POST['country']
        acc.permanentaddress1 = request.POST['address1']
        acc.permanentaddress2 = request.POST['address2']
        acc.permanentaddress3 = request.POST['address3']
        acc.height = request.POST['height']
        acc.weight = request.POST['weight']
        acc.joiningdate = datetime.now()
        acc.save()
        msg_success = "Registration successfully Check Your Registered Mail"
        return render(request, 'Registration.html', {'msg_success': msg_success})
    return render(request,'Registration.html')   
    