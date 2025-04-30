from django.shortcuts import render
from . import info
import pandas as pd
import os
import pickle
from django.conf import settings
import numpy as np
# Correct full path to the model
model_path = os.path.join(settings.BASE_DIR, 'crop_recomendetion_system', 'models', 'crop_recommendation_model.pkl')
# csv_path = os.path.join(settings.BASE_DIR, 'crop_recomendetion_system', 'models', 'crop_recommendation.csv')


with open(model_path, 'rb') as f:
    model = pickle.load(f)

label_encoder_path = os.path.join(settings.BASE_DIR, 'crop_recomendetion_system', 'models', 'label_encoder.pkl')   

with open(label_encoder_path, 'rb') as f:
    le = pickle.load(f)
def recomend(request):
     if request.method == 'POST':
          nitrogen=float(request.POST.get('Nitrogen'))
          phosphorus=float(request.POST.get('Phosphorus'))
          potassium=float(request.POST.get('Potassium'))
          temperature=float(request.POST.get('Temperature'))
          humidity=float(request.POST.get('Humidity'))
          ph=float(request.POST.get('pH'))
          rainfall=float(request.POST.get('Rainfall'))

          sample_input = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

          predicted_crop_encoded=model.predict(sample_input)
          predicted_crop=le.inverse_transform(predicted_crop_encoded)        
          context={
               'result':predicted_crop[0],
               'details':info.crop_info[predicted_crop[0]],
          }         
          return render(request, 'recomend.html', context)
     return render(request, 'recomend.html')

def home(request):
     return render(request, 'index.html')

def search(request):
     csv_path = os.path.join(settings.BASE_DIR, 'crop_recomendetion_system', 'models', 'crop_recommendation.csv')
    
     if not os.path.exists(csv_path):
        return HttpResponse(f"CSV not found at: {csv_path}", status=500)
     df = pd.read_csv(csv_path)
     crop_names=df['label'].unique()
     crop_search=request.POST.get('crop_inp')
     if request.method == 'POST':
          if crop_search in crop_names:
               crop_details=df[df['label']==crop_search]
               context={
                    'crop_name':crop_search,
                    'Nitrogen':f"{crop_details['N'].mean():2f}",
                    'Phosphorus':f"{crop_details['P'].mean():2f}",
                    'Potassium':f"{crop_details['K'].mean():2f}",
                    'Temperature':f"{crop_details['temperature'].mean():2f}",
                    'Humidity':f"{crop_details['humidity'].mean():2f}",
                    'ph':f"{crop_details['ph'].mean():2f}",
                    'Rainfall':f"{crop_details['rainfall'].mean():2f}",
               }
               return render(request, 'search.html', context)
          else:
               return render(request, 'search.html',data={'error':'Crop not found'})

     return render(request, 'search.html')
