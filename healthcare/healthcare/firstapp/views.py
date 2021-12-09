from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib import messages
from firstapp.models import Doctors
import tensorflow as tf
from tensorflow.keras.models import load_model
from .forms import *
import pickle
import os
from skimage.io import imread
import cv2
from django.http import HttpResponse
from PIL import Image
from io import StringIO,BytesIO
import numpy as np
from keras import models   


# Create your views here.
def register(request):
    if request.method=="POST":
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']
        if password==re_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is already exists')
                return redirect('register')
            else:
                urs=User.objects.create_user(first_name=f_name,last_name=l_name,username=username,email=email,password=password)
                urs.save();
                messages.info(request,'Successfully registered')
                return redirect('guesthome')
        else:
            messages.info(request,'Password and Retype password is not matching')
            return redirect('register')
            
    else:
        return render(request, 'guesthome.html')

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username =username, password = password)
            if user is not None:
                auth.login(request,user)
                request.session['uid'] = user.id
                if user. is_superuser==0:
                    return redirect("home_doctor")

                  

                else:
                    return redirect("admin")


            else:
                messages.info(request,'Username and password is not matching')   
                return render(request,'guesthome.html')
        else:
             return render(request,"guesthome.html")
    else:
        return redirect(request,"signout")

def home(request):
    return render(request,'home.html')
def patientRegistration(request):
    return render(request,'p_registration.html')

def signout(request):
    logout(request)
    return render(request,'guesthome.html')
def home_doctor(request):
    return render(request,'home_doctor.html')
def index(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio.html')

def patientRegistration(request):
    if request.method == "POST":
        p_name = request.POST['Name']
        t_no = request.POST['TokenNo']
        age = request.POST['Age']
        gender = request.POST['gender']
        phone = request.POST['PhoneNo']
        Description = request.POST['Description']
        d_id = request.session['uid']
        usr =PatientRegistration.objects.create(patientName=p_name, t_nNo=t_no, patientAge=age, Gender=gender, phoneNo=phone, doct_id=d_id, discription=Description)
        usr.save();
        messages.info(request, 'Successfully registered')
        return redirect('home_doctor')
    else:
        return render(request, 'p_registration.html')

#admin page
def admin(request):
    return render(request, 'admin.html')
def view_doctors(request):
    details = User.objects.filter(is_staff=0)
    return render(request, 'view_doctors.html', {'details':details})
def view_patients(request):
    d_id = request.session['uid']
    details = PatientRegistration.objects.filter(doct_id=d_id)
    return render(request, 'view_patient.html', {'details': details})

def admin_view_patients(request):
    d_id = request.GET.get('d_id')
    details = PatientRegistration.objects.filter(doct_id=d_id)
    return render(request, 'admin_view_patient.html', {'details': details})


def doctorregister(request):
    #p_id = request.GET.get('d_id')
    #if p_id != "":

    if request.method=="POST":
        D_name=request.POST['name']
        D_address=request.POST['address']
        D_gender=request.POST['gender']
        D_qualification=request.POST['qualifiction']
        D_email=request.POST['email']
        D_password=request.POST['password']
        re_password=request.POST['re_password']
        if D_password==re_password:
            if User.objects.filter(email=D_email).exists():
                messages.info(request,'email is already exists')
                return redirect('doctorregister')
            else:
                usr=Doctors.objects.create(D_name=D_name,D_address=D_address,D_gender=D_gender,D_qualification=D_qualification,D_email=D_email,D_password=D_password)
                usr.save();
                messages.info(request,'Successfully registered')
                return redirect('doctorregister')
        else:
            messages.info(request,'Password and Retype password is not matching')
            return redirect('doctorregister')
            
    else:
        return render(request, 'D_registration.html')

#image upload...
def valuedisplay(request):
    p_id = request.GET.get('p_id')
    print(p_id)
    return HttpResponse(p_id)
def hotel_image_view(request):

    p_id = request.GET.get('p_id')
    request.session['p_id'] = p_id

    if request.method == 'POST':

        form = XrayUploadForm(request.POST, request.FILES)

  
        if form.is_valid():

            form.save()
            model = load_model('D:/PERSONAL/mainproject/healthcare/healthcare/model/pnemonia_o6.h5')
            class_names = os.listdir('D:/PERSONAL/mainproject/healthcare/healthcare/model/test')
            # img1= cv2.imread('C:/Users/Jose/BroAlex/mysite1/static/images/')
            obj = XrayUpload.objects.last()
            field_object = XrayUpload._meta.get_field('xray_image')

            field_value = field_object.value_from_object(obj)
            img = imread(field_value)

            img = cv2.resize(img, (180, 180))

            img_resized = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            # img_resized = Image.fromarray(img, 'RGB')
            # img_array = np.array(img_resized)
            img_array = np.expand_dims(img_resized, 0)
            y_pred = model.predict(img_array)
            score = tf.nn.softmax(y_pred[0])
            print(score)
            if np.max(score) > 0.01:
                name = class_names[np.argmax(score)]
                print(np.max(score))
                print(name)
                p_id = request.session['p_id']

                usr = XrayUpload.objects.create(patient_id=p_id, xray_image=field_value, result=name)
                usr.save();
                if name == 'PNEUMONIA':
                    obj = XrayUpload.objects.last()
                    return render(request, 'pneumonia.html', {'XrayUpload': obj})

                else:
                    return render(request, 'normal.html')

        return HttpResponse(name)



          # return redirect('success') 
    else: 
        form = XrayUploadForm()
    return render(request, 'images.html', {'form': form})
  
  
def success(request): 
    return HttpResponse('successfully uploaded')
def status_update(request):
    userid = request.Get('id')
    return HttpResponse(userid)



def failed(request):
    return HttpResponse('you nee the permission from the ADMIN')

#image view.....
def display_hotel_images(request): 
  
    if request.method == 'GET':
        p_id = request.GET.get('p_id')
  
        # getting all the objects of hotel. 
        obj = XrayUpload.objects.filter(patient_id=p_id)
        return render(request, 'view_images.html',{'XrayUpload' : obj})

#........................................
def guesthome(request):
    return render(request,'guesthome.html')
def readmore(request):
    return render(request,'single.html')

