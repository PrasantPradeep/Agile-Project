"""mental_health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('log',views.log,name='log'),
    path('user_reg',views.user_reg,name='user_reg'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('admin_manage_psychatrist',views.admin_manage_psychatrist,name='admin_manage_psychatrist'),
    path('admin_update_psychatrist/<ids>',views.admin_update_psychatrist,name='admin_update_psychatrist'),
    path('admin_delete_psychatrist/<ids>',views.admin_delete_psychatrist,name='admin_delete_psychatrist'),
    path('admin_manage_counsilor',views.admin_manage_counsilor,name='admin_manage_counsilor'),
    path('admin_update_counsilor/<ids>',views.admin_update_counsilor,name='admin_update_counsilor'),
    path('admin_delete_counsilor/<ids>',views.admin_delete_counsilor,name='admin_delete_counsilor'),
    path('admin_manage_meditation',views.admin_manage_meditation,name='admin_manage_meditation'),
    path('admin_update_meditation/<ids>',views.admin_update_meditation,name='admin_update_meditation'),
    path('admin_delete_meditation/<ids>',views.admin_delete_meditation,name='admin_delete_meditation'),
    path('admin_view_request',views.admin_view_request,name='admin_view_request'),
    path('admin_view_test/<ids>',views.admin_view_test,name='admin_view_test'),
    path('admin_make_appointment/<ids>/<id>',views.admin_make_appointment,name='admin_make_appointment'),
     path('admin_view_feedback',views.admin_view_feedback,name='admin_view_feedback'),
    
        
        
        
        
        
        
    path('user_home',views.user_home,name='user_home'),
    path('user_view_request',views.user_view_request,name='user_view_request'),
    path('user_view_appointment',views.user_view_appointment,name='user_view_appointment'),
    path('user_make_payment/<ids>/<amt>',views.user_make_payment,name='user_make_payment'),
    path('user_view_suggested/<ids>',views.user_view_suggested,name='user_view_suggested'),
    path('user_view_awareness',views.user_view_awareness,name='user_view_awareness'),
    path('user_send_feedback',views.user_send_feedback,name='user_send_feedback'),
    path('user_view_test_result',views.user_view_test_result,name='user_view_test_result'),
    path('user_take_test',views.user_take_test,name='user_take_test'),
    path('sentiment',views.sentiment,name='sentiment'),
    path('predict',views.predict,name='predict'),
    path('predictSentiment',views.predictSentiment,name='predictSentiment'),
    path('camera',views.camera,name='camera'),
    path('camclick',views.camclick,name='camclick'),
    path('add_result',views.add_result,name='add_result'),
    path('add_output',views.add_output,name='add_output'),
    path('voice_change',views.voice_change,name='voice_change'),
    path('request_appointment',views.request_appointment,name='request_appointment'),
    path('user_view_payment/<ids>',views.user_view_payment,name='user_view_payment'),
    path('invoice/<amt>/<date>',views.invoice,name='invoice'),
    
    
    
    
    
    
    
    
    
    
    
   
   
   
   
   
   
    path('psychatrist_home',views.psychatrist_home,name='psychatrist_home'),
    path('psychatrist_view_appointment',views.psychatrist_view_appointment,name='psychatrist_view_appointment'),
    path('psychatrist_update_condition/<ids>',views.psychatrist_update_condition,name='psychatrist_update_condition'),
    path('psychatrist_suggest_treatment/<ids>',views.psychatrist_suggest_treatment,name='psychatrist_suggest_treatment'),
    path('psychatrist_view_payment/<ids>',views.psychatrist_view_payment,name='psychatrist_view_payment'),
    path('psychatrist_send_feedback',views.psychatrist_send_feedback,name='psychatrist_send_feedback'),
    path('psy_view_request',views.psy_view_request,name='psy_view_request'),
    
    
    
    
    
    
    path('counsilor_home',views.counsilor_home,name='counsilor_home'),
    path('counsilor_view_appointment',views.counsilor_view_appointment,name='counsilor_view_appointment'),
    path('counsilor_update_condition/<ids>',views.counsilor_update_condition,name='counsilor_update_condition'),
    path('counsilor_suggest_treatment/<ids>',views.counsilor_suggest_treatment,name='counsilor_suggest_treatment'),
    path('counsilor_view_payment/<ids>',views.counsilor_view_payment,name='counsilor_view_payment'),
    path('counsilor_send_feedback',views.counsilor_send_feedback,name='counsilor_send_feedback'),
    
    
    
    
    
    
    path('meditation_home',views.meditation_home,name='meditation_home'),
    path('meditation_view_appointment',views.meditation_view_appointment,name='meditation_view_appointment'),
    path('med_manage_motivation/<ids>',views.med_manage_motivation,name='med_manage_motivation'),
    path('meditation_view_payment/<ids>',views.meditation_view_payment,name='meditation_view_payment'),
    path('meditation_send_feedback',views.meditation_send_feedback,name='meditation_send_feedback'),
    path('meditation_manage_aware',views.meditation_manage_aware,name='meditation_manage_aware'),
    
]
