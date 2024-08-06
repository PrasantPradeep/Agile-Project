from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from mental.models import *
from mental.modelss import *
from mental.TweetModel import *
from mental.depression_detection_tweets import *
from mental.em import *
# from mental.em import camclick
from .views import *
import os
from mental.core import *


################################PUBLIC##########################################################################

def home(request):
    return render(request,'public_home.html')

def log(request):
    if 'login' in request.POST:
        uname=request.POST['uname']
        psw=request.POST['pass']
        obj=login.objects.get(username=uname,password=psw)
        if obj:
            request.session['lid']=obj.pk
            if obj.usertype=='admin':
                return HttpResponse("<script>alert('Login Success');window.location='/admin_home'</script>")
            if obj.usertype=='psychatrist':
                ob=psychatrist.objects.get(login=request.session['lid'])
                if ob:
                    request.session['pid']=ob.pk
                    
                    return HttpResponse("<script>alert('Login Success');window.location='/psychatrist_home'</script>")
            elif obj.usertype=='counsilor':
                ob=counsilor.objects.get(login=request.session['lid'])
                if ob:
                    request.session['cid']=ob.pk
                    
                    return HttpResponse("<script>alert('Login Success');window.location='/counsilor_home'</script>")
            elif obj.usertype=='meditation':
                ob=meditation.objects.get(login=request.session['lid'])
                if ob:
                    request.session['mid']=ob.pk
                    
                    return HttpResponse("<script>alert('Login Success');window.location='/meditation_home'</script>")
            elif obj.usertype=='user':
                ob=user.objects.get(login=request.session['lid'])
                if ob:
                    request.session['uid']=ob.pk
                    
                    return HttpResponse("<script>alert('Login Success');window.location='/user_home'</script>")

    return render(request,'login.html')


import os
from django.http import HttpResponse

def user_reg(request):
    if 'submit' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        place = request.POST['place']
        email = request.POST['email']
        uname = request.POST['user']
        passw = request.POST['pass']
        
        lg = login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exists');window.location='/user_reg'</script>")
        else:
            lg = login(username=uname, password=passw, usertype='user')
            lg.save()

            tchr = user(first_name=fname, last_name=lname, place=place, phone=phone, email=email, login_id=lg.pk)
            tchr.save()

            pid = str(tchr.pk)  # Get the primary key (id) of the saved "user" object

            # Create the directory and its parent directories if they do not exist
            trainimages_dir = os.path.join('static', 'trainimages', pid)
            os.makedirs(trainimages_dir, exist_ok=True)

            # Save the images to the newly created directory
            for i in range(1, 4):
                image_key = f'img{i}'
            image = request.FILES.get(image_key)

            if image:
                path = os.path.join("static/trainimages", pid, image.name)
                with open(path, "wb") as f:
                    f.write(image.read())
                    
                    
            enf("static/trainimages/")

        return HttpResponse("<script>alert('Added Successfully');window.location='/user_reg'</script>")

    return render(request, 'user_reg.html')



###################################ADMIN################################################################################

def admin_home(request):
    return render(request,'admin_home.html')  


def admin_manage_psychatrist(request):
    obj=psychatrist.objects.all()
    if 'submit' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        place=request.POST['place']
        email=request.POST['email']
        qua=request.POST['qua']
        uname=request.POST['user']
        passw=request.POST['pass']
        
        lg=login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/admin_manage_psychatrist'</script>")
        else:
            lg=login(username=uname,password=passw,usertype='psychatrist')
            lg.save()
            tchr=psychatrist(first_name=fname,last_name=lname,place=place,phone=phone,email=email,qualification=qua,login_id=lg.pk)
            tchr.save()
            return HttpResponse("<script>alert('Added Successsfully');window.location='/admin_manage_psychatrist'</script>")
    return render(request,'admin_manage_psychatrist.html',{'obj':obj})

def admin_update_psychatrist(request,ids):
    obj=psychatrist.objects.all()
    ob=psychatrist.objects.get(psychatrist_id=ids)
    if 'update' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        place=request.POST['place']
        email=request.POST['email']
        qua=request.POST['qua']
        ob.first_name=fname
        ob.last_name=lname
        ob.phone=phone
        ob.place=place
        ob.email=email
        ob.qualification=qua
        ob.save()
        return HttpResponse("<script>alert('Updated Successsfully');window.location='/admin_manage_psychatrist'</script>")
    return render(request,'admin_manage_psychatrist.html',{'obj':obj,'ob':ob})
    
def admin_delete_psychatrist(request,ids):
    ob=psychatrist.objects.get(psychatrist_id=ids)
    ob.delete()
    return HttpResponse("<script>alert('Deleted Successsfully');window.location='/admin_manage_psychatrist'</script>")

def admin_manage_counsilor(request):
    obj=counsilor.objects.all()
    if 'submit' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        place=request.POST['place']
        email=request.POST['email']
        qua=request.POST['qua']
        uname=request.POST['user']
        passw=request.POST['pass']
        
        lg=login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/admin_manage_counsilor'</script>")
        else:
            lg=login(username=uname,password=passw,usertype='counsilor')
            lg.save()
            tchr=counsilor(first_name=fname,last_name=lname,place=place,phone=phone,email=email,qualification=qua,login_id=lg.pk)
            tchr.save()
            return HttpResponse("<script>alert('Added Successsfully');window.location='/admin_manage_counsilor'</script>")
    return render(request,'admin_manage_counsilor.html',{'obj':obj})

def admin_update_counsilor(request,ids):
    obj=counsilor.objects.all()
    ob=counsilor.objects.get(counsilor_id=ids)
    if 'update' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        place=request.POST['place']
        email=request.POST['email']
        qua=request.POST['qua']
        ob.first_name=fname
        ob.last_name=lname
        ob.phone=phone
        ob.place=place
        ob.email=email
        ob.qualification=qua
        ob.save()
        return HttpResponse("<script>alert('Updated Successsfully');window.location='/admin_manage_counsilor'</script>")
    return render(request,'admin_manage_counsilor.html',{'obj':obj,'ob':ob})
    
def admin_delete_counsilor(request,ids):
    ob=counsilor.objects.get(counsilor_id=ids)
    ob.delete()
    return HttpResponse("<script>alert('Deleted Successsfully');window.location='/admin_manage_counsilor'</script>")

def admin_manage_meditation(request):
    obj=meditation.objects.all()
    if 'submit' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        place=request.POST['place']
        email=request.POST['email']
        qua=request.POST['qua']
        uname=request.POST['user']
        passw=request.POST['pass']
        
        lg=login.objects.filter(username=uname)
        if lg:
            return HttpResponse("<script>alert('Username Already Exist');window.location='/admin_manage_meditation'</script>")
        else:
            lg=login(username=uname,password=passw,usertype='meditation')
            lg.save()
            tchr=meditation(first_name=fname,last_name=lname,place=place,phone=phone,email=email,qualification=qua,login_id=lg.pk)
            tchr.save()
            return HttpResponse("<script>alert('Added Successsfully');window.location='/admin_manage_meditation'</script>")
    return render(request,'admin_manage_meditation.html',{'obj':obj})

def admin_update_meditation(request,ids):
    obj=meditation.objects.all()
    ob=meditation.objects.get(meditation_id=ids)
    if 'update' in request.POST:
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        place=request.POST['place']
        email=request.POST['email']
        qua=request.POST['qua']
        ob.first_name=fname
        ob.last_name=lname
        ob.phone=phone
        ob.place=place
        ob.email=email
        ob.qualification=qua
        ob.save()
        return HttpResponse("<script>alert('Updated Successsfully');window.location='/admin_manage_meditation'</script>")
    return render(request,'admin_manage_meditation.html',{'obj':obj,'ob':ob})
    
def admin_delete_meditation(request,ids):
    ob=counsilor.objects.get(meditation_id=ids)  
    ob.delete()
    return HttpResponse("<script>alert('Deleted Successsfully');window.location='/admin_manage_meditation'</script>")

def admin_view_request(request):
    obj = requestz.objects.all()
    return render(request, 'admin_view_request.html', {'obj': obj})


def admin_view_test(request,ids):
    obj=test.objects.filter(user_id=ids)
    
    return render(request,'admin_view_test.html',{'obj':obj})

def admin_make_appointment(request,ids,id):
    if 'submit' in request.POST:
        details=request.POST['details']
        amount=request.POST['amount']
        app_date_time=request.POST['dat']
        


        ab=appointment(details=details,date=timezone.now(),amount=amount,app_date_time=app_date_time,status='pending',user_id=ids,appointment_for_id=id)
        ab.save()
        return HttpResponse("<script>alert('Appointment made');window.location='/admin_view_request'</script>")
    return render(request,'admin_make_appointment.html')

def admin_view_feedback(request):
    obj=feedback.objects.all()
    return render(request,'admin_view_feedback.html',{'obj':obj})   


####################################USERS#######################################################################################################

def user_home(request):
    return render(request,'user_home.html')

def user_view_test_result(request):
    obj=test.objects.filter(user_id=request.session['uid'])
    
    return render(request,'user_view_test_result.html',{'obj':obj})


def user_view_request(request):
    obj=requestz.objects.filter(user_id=request.session['uid'])
    return render(request,'user_view_request.html',{'obj':obj})

def user_view_appointment(request):
    obj=appointment.objects.filter(user_id=request.session['uid'])
    return render(request,'user_view_appointment.html',{'obj':obj})

def user_make_payment(request,ids,amt):
    if 'submit' in request.POST:
        amt=request.POST['amt']
        obj=payment(amount=amt,date=timezone.now(),appointment_id=ids)
        obj.save()
        return HttpResponse("<script>alert('payment completed');window.location='/user_view_appointment'</script>")

    return render(request,'user_make_payment.html',{'amt':amt})

def user_view_payment(request,ids):
    pd=payment.objects.filter(appointment_id=ids)
    return render(request,'user_view_payment.html',{'pd':pd})

def invoice(request,amt,date):
    obj=user.objects.get(user_id=request.session['uid'])
    return render(request,'invoice.html',{'obj':obj,'amt':amt,'date':date})








def user_view_suggested(request,ids):
    try:

        obj=suggested_tratment.objects.filter(appointment_id=ids)
        return render(request,'user_view_suggested.html',{'obj':obj})
    except:
        return render(request,'user_view_suggested.html')



def user_view_awareness(request):
    obj=awareness.objects.all()
    return render(request,'user_view_awareness.html',{'obj':obj})



def user_send_feedback(request):
    obj=feedback.objects.filter(login_id=request.session['lid'])
    if 'submit' in request.POST:
        feed=request.POST['feed']
        ab=feedback(feedback=feed,date=timezone.now(),login_id=request.session['lid'])
        ab.save()
        return HttpResponse("<script>alert('Feedback sended');window.location='/user_send_feedback'</script>")
    
    return render(request,'user_send_feedback.html',{'obj':obj})

def user_take_test(request):
    return render(request,'index1.html')


def sentiment(request):
    return render(request,"sentiment.html")


def predict(request):
    if request.method =="POST":
        q1 = int(request.POST['a1'])
        q2 = int(request.POST['a2'])
        q3 = int(request.POST['a3'])
        q4 = int(request.POST['a4'])
        q5 = int(request.POST['a5'])
        q6 = int(request.POST['a6'])
        q7 = int(request.POST['a7'])
        q8 = int(request.POST['a8'])
        q9 = int(request.POST['a9'])
        q10 = int(request.POST['a10'])
        print('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')

        values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        model = Model()
        classifier = model.svm_classifier()
        prediction = classifier.predict([values])
        print(prediction[0],'////////////2222222222222211111111111111111333333333333333')
        if prediction[0] == 0:
                result = 'Your Depression test result : No Depression'
                request.session['r1']=prediction[0] 
                return HttpResponse("<script>window.location='/sentiment'</script>")
        if prediction[0] == 1:
                result = 'Your Depression test result : Mild Depression'
                request.session['r1']=prediction[0] 
                return HttpResponse("<script>window.location='/sentiment'</script>")
        if prediction[0] == 2:
                result = 'Your Depression test result : Moderate Depression'
                request.session['r1']=prediction[0] 
                return HttpResponse("<script>window.location='/sentiment'</script>")
                
        if prediction[0] == 3:
                result = 'Your Depression test result : Moderately severe Depression'
                request.session['r1']=prediction[0] 
                return HttpResponse("<script>window.location='/sentiment'</script>")
                
        if prediction[0] == 4:
                result = 'Your Depression test result : Severe Depression'
                request.session['r1']=prediction[0]  
                
    return HttpResponse("<script>window.location='/sentiment'</script>")
            
        

def predictSentiment(request):
   
    
    message = request.POST['form10']
    pm = process_message(message)
    result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
    request.session['r2']=result

    return HttpResponse("<script>window.location='/voice_change'</script>")


def camera(request):
    # id1=request.args['id1']
    uid=request.session['uid']
    tf.keras.backend.clear_session()
    
    q=camclick(uid)
    print("$$$$$$$$$$$$$$$$$$$ : ",q)
    tf.keras.backend.clear_session()
    
     
    request.session['r3']=q
    return HttpResponse("<script>window.location='/add_result'</script>")


def voice_change(request):
    data={}
    if 'submit' in request.POST:
        message=request.POST['sen']
        print("****************************** :::")
        print(message)
        pm = process_message(message)
        result = DepressionDetection.classify(pm, 'bow') or DepressionDetection.classify(pm, 'tf-idf')
        request.session['r4']=result
        return HttpResponse("<script>window.location='/camera'</script>")
    return render(request,'upload_voice.html')



def add_result(request):
    result1=request.session.get('r1')
    result2=request.session.get('r2')
    result3=request.session.get('r3')
    result4=request.session.get('r4')
    print(result3,":::::::::::::::::: ??????????????????? ")
    
    try:
        obj=result.objects.get(user_id=request.session['uid'])
        if obj:
            obj.result1=result1
            obj.result2=result2
            obj.result3=result3
            obj.result4=result4
            obj.save()
            return HttpResponse("<script>window.location='/add_output'</script>")
    except:
        q=result(user_id=request.session['uid'],result1=result1,result2=result2,result3=result3,result4=result4)
        q.save()
        return HttpResponse("<script>window.location='/add_output'</script>")
                
                
def add_output(request):
    import random
    from datetime import date
    obj=result.objects.get(user_id=request.session['uid'])   
    re1 = float(obj.result1)
    re2 = float(obj.result2)
    re3 = float(obj.result3)
    re4 = float(obj.result4)
    print("re1:", re1, "\nre2:", re2, "\nre3:", re3, "\nre4:", re4)
    
    # if re1 == 4 and re4 == 3 and re2 == 1 and re3 <=1:
    #         v = 'Severe Depression'
    # elif re1 == 4 and re4 == 3 and re2 == 0 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4 and re4 == 3 and re2 == 0 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4 and re4 == 2 and re2 == 1 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4 and re4 == 2 and re2 == 1 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4 and re4 == 2 and re2 == 0 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4 and re4 == 2 and re2 == 0 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4 and re4 == 1 and re2 == 1 and re3 <=1:
    #     v = 'Severe Depression'
    # elif re1 == 4.0 and re4 == 1.0 and re2 ==1.0 and re3 <= 3.0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 1 and re2 == 1 and re3 <= 3.0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 1 and re2 == 0 and re3 <= 3.0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 1 and re2 == 0 and re3 <= 3.0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 0 and re2 == 1 and re3 <= 3.0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 4 and re2 == 1 and re3 <= 3.0:
    #     v = 'No Depression'
    # elif re1 == 4 and re4 == 4 and re2 == 1 and re3 >=4.0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 4 and re2 == 0 and re3 >=4.0:
    #     v = 'No Depression'
    # elif re1 == 4 and re4 == 4 and re2 == 0 and re3 >=4.0:
    #     v = 'No Depression'
    # elif re1 == 4 and re4 == 4 and re2 == 0 and re3 >=4.0:
    #     v = 'No Depression'    
    # elif re1 == 3 and re4 == 4 and re2 == 1 and re3 >=4.0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 1 and re3 <=2:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 <=2:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 <=2:
    #     v = 'Moderate Depression'    
    # elif re1 == 3 and re4 == 4 and re2 == 1 and re3 <=2:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 1 and re3 <=2:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 <=2:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 1 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 1 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 0 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 0 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 1 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 1 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 0 and re3 <=2:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
    #     v = 'Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
    #     v = 'Severe Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Severe Depression'
    # elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 1 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 2 and re4 == 0 and re2 == 1 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 2 and re4 == 0 and re2 == 0 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 4 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 3 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 3 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 2 and re2 == 1 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 2 and re2 == 0 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 1 and re2 == 1 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 1 and re4 == 1 and re2 == 0 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 0 and re4 == 4 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 0 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 0 and re4 == 3 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 0 and re4 == 3 and re2 == 0 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 0 and re4 == 2 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 0 and re4 == 2 and re2 == 0 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 0 and re4 == 1 and re2 == 1 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 1:
    #     v = 'No Depression'
    # elif re1 == 0 and re4 == 1 and re2 == 0 and re3 == 0:
    #     v = 'No Depression'
    # elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 1:
    #     v = 'No Depression'
    # elif re1 == 0 and re4 == 0 and re2 == 1 and re3 == 0:
    #     v = 'No Depression'
    # elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 1:
    #     v = 'No Depression'
    # elif re1 == 0 and re4 == 0 and re2 == 0 and re3 == 0:
    #     v = 'No Depression' 
    # elif re1 == 4 and re4 == 0 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 4 and re4 == 0 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 3:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 3 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 2 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 1 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 1:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 1 and re2 == 0 and re3 == 0:
    #     v = 'Moderate Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 1 and re3 == 0:
    #     v = 'Mild Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 1:
    #     v = 'Mild Depression'
    # elif re1 == 3 and re4 == 0 and re2 == 0 and re3 == 0:
    #     v = 'Mild Depression'

    # elif re1 == 2 and re4 == 4 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 4 and re2 == 0 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 3 and re2 == 0 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 2 and re2 == 0 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 1:
    #     v = 'Moderately Severe Depression'
    # elif re1 == 2 and re4 == 1 and re2 == 1 and re3 == 0:
    #     v = 'Moderately Severe Depression'
    if re1 >= 4 and re4 >=1 and re2 >=1 and re3 >= 3:
        v = 'Severe Depression'
    elif re1 >= 4 and re4 >=1 and re2 >=1 and re3 <= 3:
        v= 'moderate'
    
    elif re1 >=2 and re4 >=0 and re2 >= 1 and re3 == 1:
        v= "Mild Depression"
    elif re1 >=1 and re4 >=1 and re2 >=1  and re3 >= 3:
        v = 'No Depression' 
    else:
        v = 'No Depression'

    
    # try: 
    #     ab=output_result.objects.get(user_id=request.session['uid'],date=date.today())
    #     if ab:
    #         ab.output=v
    #         ab.save()
    #         if ab.output == 'Severe Depression':
                
    #             import random

    #             # Get all objects from the queryset
    #             all_objects = psychatrist.objects.all()

    #             # Get a random sample of size 'sample_size'
    #             sample_size = 1  # Replace this with the desired sample size
    #             random_sample = random.sample(list(all_objects), sample_size)

    #             # Print the login_id of the first object in the random_sample
    #             if random_sample:
    #                 print("login_id:", random_sample[0].login_id)
    #                 qry=requestz(appointment_for_id=random_sample[0].login_id,details='Severe Depression',date=date.today(),status='pending',user_id=request.session['uid'])
    #                 qry.save()
    #                 return HttpResponse("<script>alert('Thank you');window.location='/user_home'</script>")
    #             else:
    #                 print("No random sample available.")
            
                
    #         elif ab.output == 'Moderate Depression':
    #             import random

    #             # Get all objects from the queryset
    #             all_objects = counsilor.objects.all()

    #             # Get a random sample of size 'sample_size'
    #             sample_size = 1  # Replace this with the desired sample size
    #             random_sample = random.sample(list(all_objects), sample_size)

    #             # Print the login_id of the first object in the random_sample
    #             if random_sample:
    #                 print("login_id:", random_sample[0].login_id)
    #                 qry=requestz(appointment_for_id=random_sample[0].login_id,details='Moderate Depression',date=date.today(),status='pending',user_id=request.session['uid'])
    #                 qry.save()
    #                 return HttpResponse("<script>alert('Thank you ');window.location='/'</script>")
    #             else:
    #                 print("No random sample available.")
                    
                    
                    
    #         elif ab.output == 'Mild Depression':
    #             import random

    #             # Get all objects from the queryset
    #             all_objects = meditation.objects.all()

    #             # Get a random sample of size 'sample_size'
    #             sample_size = 1  # Replace this with the desired sample size
    #             random_sample = random.sample(list(all_objects), sample_size)

    #             # Print the login_id of the first object in the random_sample
    #             if random_sample:
    #                 print("login_id:", random_sample[0].login_id)
    #                 qry=requestz(appointment_for_id=random_sample[0].login_id,details='Mild Depression',date=date.today(),status='pending',user_id=request.session['uid'])
    #                 qry.save()
    #                 return HttpResponse("<script>alert('Thank you');window.location='/'</script>")
    #             else:
    #                 print("No random sample available.")
                    
                    
    #         return HttpResponse("<script>alert('Thank you ');window.location='/'</script>")
    # except:
    #     ob=output_result(output=v,date=date.today(),user_id=request.session['uid'])
    #     ob.save()
    #     if ob.output == 'Severe Depression':
            
    #         import random

    #         # Get all objects from the queryset
    #         all_objects = psychatrist.objects.all()

    #         # Get a random sample of size 'sample_size'
    #         sample_size = 1  # Replace this with the desired sample size
    #         random_sample = random.sample(list(all_objects), sample_size)

    #         # Print the login_id of the first object in the random_sample
    #         if random_sample:
    #             print("login_id:", random_sample[0].login_id)
    #             qry=requestz(appointment_for_id=random_sample[0].login_id,details='Severe Depression',date=date.today(),status='pending',user_id=request.session['uid'])
    #             qry.save()
    #         else:
    #             print("No random sample available.")
           
                
    #     elif ob.output == 'Moderate Depression':
    #         import random

    #         # Get all objects from the queryset
    #         all_objects = counsilor.objects.all()

    #         # Get a random sample of size 'sample_size'
    #         sample_size = 1  # Replace this with the desired sample size
    #         random_sample = random.sample(list(all_objects), sample_size)

    #         # Print the login_id of the first object in the random_sample
    #         if random_sample:
    #             print("login_id:", random_sample[0].login_id)
    #             qry=requestz(appointment_for_id=random_sample[0].login_id,details='Moderate Depression',date=date.today(),status='pending',user_id=request.session['uid'])
    #             qry.save()
    #         else:
    #             print("No random sample available.")
                
                
                
    #     elif ob.output == 'Mild Depression':
    #         import random

    #         # Get all objects from the queryset
    #         all_objects = meditation.objects.all()

    #         # Get a random sample of size 'sample_size'
    #         sample_size = 1  # Replace this with the desired sample size
    #         random_sample = random.sample(list(all_objects), sample_size)

    #         # Print the login_id of the first object in the random_sample
    #         if random_sample:
    #             print("login_id:", random_sample[0].login_id)
    #             qry=requestz(appointment_for_id=random_sample[0].login_id,details='Mild Depression',date=date.today(),status='pending',user_id=request.session['uid'])
    #             qry.save()
    #         else:
    #             print("No random sample available.")
                
            
    return HttpResponse("<script>alert('Thank you for completing the test');window.location='/'</script>")
    
def request_appointment(request,re):
    
    qs=output_result.objects.all()
    
    obj=login.objects.filter(usertype=re)
    
    return render(request,'user_send_request',{'obj',obj},{'qs':qs})
    
    
    
    
    
               
        

##############################PSYCHATRIST###############################################################################

def psychatrist_home(request):
    return render(request,'psychatrist_home.html')


def psychatrist_view_appointment(request):
    obj=appointment.objects.filter(appointment_for_id=request.session['lid'])
    return render(request,'psychatrist_view_appointment.html',{'obj':obj})

def psy_view_request(request):
    obj=requestz.objects.filter(appointment_for_id=request.session['lid'])
    return render(request,'psy_view_request.html',{'obj':obj})

def psychatrist_update_condition(request,ids):
    obj=updation.objects.filter(appointment_id=ids)
    if 'submit' in request.POST:
        details=request.POST['details']
        ab=updation(details=details,date=timezone.now(),appointment_id=ids)
        ab.save()
        return HttpResponse("<script>alert('condition updated');window.location='/psychatrist_update_condition"+'/'+str(ids)+"'</script>")

    
    return render(request,'psychatrist_update_condition.html',{'obj':obj})

def psychatrist_suggest_treatment(request,ids):
    obj=suggested_tratment.objects.filter(appointment_id=ids)
    if 'submit' in request.POST:
        treat=request.POST['treat']
        details=request.POST['details']
        ab=suggested_tratment(treatment=treat,date=timezone.now(),details=details,login_id=request.session['lid'],appointment_id=ids)
        ab.save()
        return HttpResponse("<script>alert('treatment suggested');window.location='/psychatrist_suggest_treatment"+'/'+str(ids)+"'</script>")
    
    return render(request,'psychatrist_suggest_treatment.html',{'obj':obj})

def psychatrist_view_payment(request,ids):
    obj=payment.objects.filter(appointment_id=ids)
    return render(request,'psychatrist_view_payment.html',{'obj':obj})   


def psychatrist_send_feedback(request):

    obj=feedback.objects.filter(login_id=request.session['lid'])
    if 'submit' in request.POST:
        feed=request.POST['feed']
        ab=feedback(feedback=feed,date=timezone.now(),login_id=request.session['lid'])
        ab.save()
        return HttpResponse("<script>alert('Feedback sended');window.location='/psychatrist_send_feedback'</script>")
    
    return render(request,'psychatrist_send_feedback.html',{'obj':obj})
    

#################################COUNCILOR##############################################################################

def counsilor_home(request):
    return render(request,'counsilor_home.html')


def counsilor_view_appointment(request):
    obj=appointment.objects.filter(appointment_for_id=request.session['lid'])
    return render(request,'counsilor_view_appointment.html',{'obj':obj})

def counsilor_update_condition(request,ids):
    obj=updation.objects.filter(appointment_id=ids)
    if 'submit' in request.POST:
        details=request.POST['details']
        ab=updation(details=details,date=timezone.now(),appointment_id=ids)
        ab.save()
        return HttpResponse("<script>alert('condition updated');window.location='/psychatrist_update_condition"+str(ids)+"'</script>")

    
    return render(request,'counsilor_update_condition.html',{'obj':obj})

def counsilor_suggest_treatment(request,ids):
    obj=suggested_tratment.objects.filter(appointment_id=ids)
    if 'submit' in request.POST:
        treat=request.POST['treat']
        details=request.POST['details']
        ab=suggested_tratment(treatment=treat,date=timezone.now(),details=details,login_id=request.session['lid'],appointment_id=ids)
        ab.save()
        return HttpResponse("<script>alert('treatment suggested');window.location='/psychatrist_suggest_treatment"+str(ids)+"'</script>")
    
    return render(request,'counsilor_suggest_treatment.html',{'obj':obj})

def counsilor_view_payment(request,ids):
    obj=payment.objects.filter(appointment_id=ids)
    return render(request,'counsilor_view_payment.html',{'obj':obj})   


def counsilor_send_feedback(request):

    obj=feedback.objects.filter(login_id=request.session['lid'])
    if 'submit' in request.POST:
        feed=request.POST['feed']
        ab=feedback(feedback=feed,date=timezone.now(),login_id=request.session['lid'])
        ab.save()
        return HttpResponse("<script>alert('Feedback sended');window.location='/counsilor_send_feedback'</script>")
    
    return render(request,'counsilor_send_feedback.html',{'obj':obj})

###########################MEDITATION########################################################################################

def meditation_home(request):
    return render(request,'meditation_home.html')


def meditation_view_appointment(request):
    obj=appointment.objects.filter(appointment_for_id=request.session['lid'])
    return render(request,'meditation_view_appointment.html',{'obj':obj})

def med_manage_motivation(request,ids):
    obj=motivation.objects.filter(appointment_id=ids)
    if 'submit' in request.POST:
        classes=request.POST['class']
        details=request.POST['details']
        date=request.POST['date']
        ab=motivation(classes=classes,details=details,date=date,status='active',appointment_id=ids)
        ab.save()
        return HttpResponse("<script>alert('Motivation Added suggested');window.location='/med_manage_motivation"+str(ids)+"'</script>")
    
    return render(request,'med_manage_motivation.html',{'obj':obj})


def meditation_view_payment(request,ids):
    obj=payment.objects.filter(appointment_id=ids)
    return render(request,'meditation_view_payment.html',{'obj':obj}) 

def meditation_send_feedback(request):
    
    obj=feedback.objects.filter(login_id=request.session['lid'])
    if 'submit' in request.POST:
        feed=request.POST['feed']
        ab=feedback(feedback=feed,date=timezone.now(),login_id=request.session['lid'])
        ab.save()
        return HttpResponse("<script>alert('Feedback sended');window.location='/meditation_send_feedback'</script>")
    
    return render(request,'meditation_send_feedback.html',{'obj':obj})


def meditation_manage_aware(request):
    obj=awareness.objects.filter(meditation_id=request.session['mid'])
    if 'submit' in request.POST:
        details=request.POST['details']
        place=request.POST['place']
        date=request.POST['date']
        ab=awareness(details=details,place=place,date=date,meditation_id=request.session['mid'])
        ab.save()
        return HttpResponse("<script>alert('awareness added');window.location='/meditation_manage_aware'</script>")
    return render(request,'meditation_manage_aware.html',{'obj':obj})

def meditation_update_condition(request,ids):
    obj=updation.objects.filter(appointment_id=ids)
    if 'submit' in request.POST:
        details=request.POST['details']
        ab=updation(details=details,date=timezone.now(),appointment_id=ids)
        ab.save()
        return HttpResponse("<script>alert('condition updated');window.location='/meditation_update_condition"+str(ids)+"'</script>")


