from django.db import models

class login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=225)
    password=models.CharField(max_length=225)
    usertype=models.CharField(max_length=225)
    

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)


class psychatrist(models.Model):
    psychatrist_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)
    
   
class counsilor(models.Model):
    counsilor_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)


class meditation(models.Model):
    meditation_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=225)
    last_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    phone=models.CharField(max_length=225)
    email=models.CharField(max_length=225)
    qualification=models.CharField(max_length=225)
    
    
class requestz(models.Model):
    request_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    appointment_for=models.ForeignKey(login,on_delete=models.CASCADE)
    details=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    
class appointment(models.Model):
    appointment_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    appointment_for=models.ForeignKey(login,on_delete=models.CASCADE)
    details=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    amount=models.CharField(max_length=225)
    app_date_time=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    
class motivation(models.Model):
    motivation_id=models.AutoField(primary_key=True)
    appointment=models.ForeignKey(appointment,on_delete=models.CASCADE)
    classes=models.CharField(max_length=225)
    details=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    status=models.CharField(max_length=225)
    
class updation(models.Model):
    updation_id=models.AutoField(primary_key=True)
    appointment=models.ForeignKey(appointment,on_delete=models.CASCADE)
    details=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class test(models.Model):
    test_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    test=models.CharField(max_length=225)
    result=models.CharField(max_length=225)
    
class payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    appointment=models.ForeignKey(appointment,on_delete=models.CASCADE)
    amount=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class suggested_tratment(models.Model):
    suggested_tratment_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    appointment=models.ForeignKey(appointment,on_delete=models.CASCADE)
    treatment=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    details=models.CharField(max_length=225)
    
class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class awareness(models.Model):
    awareness_id=models.AutoField(primary_key=True)
    meditation=models.ForeignKey(meditation,on_delete=models.CASCADE)
    details=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class result(models.Model):
    result_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    result1=models.CharField(max_length=225)
    result2=models.CharField(max_length=225)
    result3=models.CharField(max_length=225)
    result4=models.CharField(max_length=225)
    
class emot(models.Model):
    emotion_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    emotions=models.CharField(max_length=225)
    emotions_score=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class ratings(models.Model):
    rating_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    ratings=models.CharField(max_length=225)
    date=models.CharField(max_length=225)
    
class output_result(models.Model):
    output_result_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    output=models.CharField(max_length=225)
    date=models.CharField(max_length=225)