from flask import session
import keras
import cv2
from keras.models import model_from_json
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
from mental.model_manager import *

import face_recognition
import pickle
from django.utils import timezone
from mental.core import rec_face_image
from django.db.models import Avg
from mental.models import *
from django.http import request
import tensorflow as tf
from django.shortcuts import render, HttpResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image





def camclick(uid):
    res2=""
    tf.keras.backend.clear_session()
    model = model_from_json(open(r"C:\Users\pcpra\OneDrive\Desktop\AI AND ML\mental_health\model\facial_expression_model_structure.json", "r").read())
    model.load_weights(r'C:\Users\pcpra\OneDrive\Desktop\AI AND ML\mental_health\model\facial_expression_model_weights.h5')  # load weights


    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    
    face_cascade = cv2.CascadeClassifier(r'C:\Users\pcpra\OneDrive\Desktop\AI AND ML\mental_health\model\haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    # i=0
    while(True):
        ret, img = cap.read()

        # img = cv2.imread('../11.jpg')
        cv2.imwrite("ss.jpg",img)
        # i=i+1
        print("################### :::::::::::: ",img)


        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #print(faces) #locations of detected faces
        emotion=None
        
        

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to main image

            detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
            detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
            detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48

            img_pixels = image.img_to_array(detected_face)
            img_pixels = np.expand_dims(img_pixels, axis = 0)

            img_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]
            
                
            predictions = model.predict(img_pixels) #store probabilities of 7 expressions
            cv2.imwrite("ss.jpg",img_pixels)
            #find max indexed array 0: angry, 1:disgust, 2:fear, 3:happy, 4:sad, 5:surprise, 6:neutral
            max_index = np.argmax(predictions[0])

            emotion = emotions[max_index]
            cv2.putText(img,emotion,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

            
                #Save just the rectangle faces in SubRecFaces
            sub_face = img[y:y+h, x:x+w]

            FaceFileName = "static/test.jpg" #Saving the current image from the webcam for testing.
            print("FaceFileName : ",FaceFileName)
            

            cv2.imwrite(FaceFileName, sub_face)

            # import time
            # while True:
            #     time.sleep(10)
            #     # print("10 seconds has passed")

                # break
            val=rec_face_image(FaceFileName)
            print("VAL............",val)
            print("user",val)
            str1=""
            print(":::::::::::::::::::::::::::::::::::::::::::::")
            for ele in val:  
                str1 = ele
                print(str1)
                val=str1.replace("'","")
                print("val : ",val)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@ : ",val)
                res=user.objects.get(user_id=val)
                print("###############")
                
                print("############1")
                
                if res:
                    # session['aid']=id1
                    print("###############2")
                    # session['uid']=val
                    if emotion=='happy':
                        q1=emot(user_id=val,emotions=emotion,emotions_score=5,date=timezone.now())
                        q1.save()
                    elif emotion=='neutral':
                        q1=emot(user_id=val,emotions=emotion,emotions_score=4,date=timezone.now())
                        q1.save()
                    elif emotion=='angry':
                        q1=emot(user_id=val,emotions=emotion,emotions_score=2,date=timezone.now())
                        q1.save()
                    else:
                        q1=emot(user_id=val,emotions=emotion,emotions_score=1,date=timezone.now())
                        q1.save()

                    
                    res2 = emot.objects.filter(user_id=val).aggregate(avgc=Avg('emotions_score'))['avgc']
                    print(res2,'/////////////ssssssssssssssssssssssssssssssssssss')
                    
                            
                    
                        
            print (emotion)
            print("*****************************************************")
                

        if cv2.waitKey(1):
            cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
         
            break

        # kill open cv things
    cap.release()
    cv2.destroyAllWindows()
    tf.keras.backend.clear_session()
            # 	pass
    return res2



def rec_face_image(imagepath):
    print("hy...........",imagepath)

    data = pickle.loads(open('faces.pickles', "rb").read())
    print("DATA : ",data)

    # load the input image and convert it from BGR to RGB
    image = cv2.imread(imagepath)
    print("image : ", image)
    h,w,ch=image.shape
    print("CH : ",ch)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("RGB : ",rgb)

    # detect the (x, y)-coordinates of the bounding boxes corresponding
    # to each face in the input image, then compute the facial embeddings
    # for each face
    print("[INFO] recognizing faces...")
    boxes = face_recognition.face_locations(rgb,
        model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    print("encodings : ",encodings)

    # initialize the list of names for each face detected
    names = []

    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
            encoding,tolerance=0.4)
        print("matches : ",matches)
        name = "Unknown"

        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:

                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            print(counts, " rount ")
            # determine the recognized face with the largest number of
            # votes (note: in the event of an unlikely tie Python will
            # select first entry in the dictionary)
            if len(counts) == 1:
                name = max(counts, key=counts.get)
            else:
                name = "-1"
        # update the list of names
        # if name not in names:
        if name != "Unknown":
            names.append(name)
    return names


# ////////////////////////////////////////////////////////

# camclick()

