from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw
import face_recognition
import os

# Create your views here.
def home(request):

    return render(request, 'index.html')

def detect(request):

    if request.method == 'POST' and request.FILES['fileToUpload']:
        myfile = request.FILES['fileToUpload']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #print("Image saved in media")

        # code for detecting faces in uploaded image

        image = face_recognition.load_image_file(settings.BASE_DIR + os.sep + uploaded_file_url)
        face_locations = face_recognition.face_locations(image)

        if len(face_locations) == 0:
            context = {'dflag': 'no',
                        'imgURL': uploaded_file_url
                        }
            return render(request, 'detect.html', context= context)

        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for face_location in face_locations:
            top, right, bottom, left = face_location
            d.rectangle(((left,top),(right,bottom)),  outline='red')
            
        pil_image.save(settings.BASE_DIR + os.sep + uploaded_file_url)

        context = {'dflag': 'yes',
        'imgURL': uploaded_file_url
        }
        return render(request, 'detect.html', context= context)

    return render(request, 'detect.html')

def features(request):

    if request.method == 'POST' and request.FILES['fileToUpload']:

        myfile = request.FILES['fileToUpload']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        #print("Image saved in media")

        # code for detecting facial features in uploaded image

        image = face_recognition.load_image_file(settings.BASE_DIR + os.sep + uploaded_file_url)
        face_landmarks_list = face_recognition.face_landmarks(image)

        if len(face_landmarks_list) == 0:
            context = {'dflag': 'no',
                        'imgURL': uploaded_file_url
                        }
            return render(request, 'features.html', context= context)

        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)

        for face_landmarks in face_landmarks_list:

            # Let's trace out each facial feature in the image with a line!
            for facial_feature in face_landmarks.keys():
                d.line(face_landmarks[facial_feature], width=3)
            
        pil_image.save(settings.BASE_DIR + os.sep + uploaded_file_url)

        context = {'dflag': 'yes',
        'imgURL': uploaded_file_url
        }
        return render(request, 'features.html', context= context)

    return render(request, 'features.html')

def compare(request):

    if request.method == 'POST' and request.FILES['fileToUpload1'] and request.FILES['fileToUpload2']:

        myfile1 = request.FILES['fileToUpload1']
        myfile2 = request.FILES['fileToUpload2']

        fs = FileSystemStorage()
        filename1 = fs.save(myfile1.name, myfile1)
        filename2 = fs.save(myfile2.name, myfile2)

        uploaded_file_url1 = fs.url(filename1)
        uploaded_file_url2 = fs.url(filename2)
        #print("Image saved in media")

        # code for comparing faces in uploaded image

        image1 = face_recognition.load_image_file(settings.BASE_DIR + os.sep + uploaded_file_url1)
        face_encoding1 = face_recognition.face_encodings(image1)[0]

        image2 = face_recognition.load_image_file(settings.BASE_DIR + os.sep + uploaded_file_url2)
        face_encoding2 = face_recognition.face_encodings(image2)[0]

        results = face_recognition.compare_faces([face_encoding1], face_encoding2)
        
        try:
            if results[0] == True:
                context = {'dflag': 'yes',
                            'imgURL1': uploaded_file_url1,
                            'imgURL2': uploaded_file_url2
                            }
            else:
                context = {'dflag': 'no',
                            'imgURL1': uploaded_file_url1,
                            'imgURL2': uploaded_file_url2
                            }

            return render(request, 'compare.html', context= context)

        except:
            context = {'dflag': 'no',
                            'imgURL1': uploaded_file_url1,
                            'imgURL2': uploaded_file_url2
                            }

            return render(request, 'compare.html', context= context)

    return render(request, 'compare.html')