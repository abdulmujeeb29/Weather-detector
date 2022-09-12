from django.shortcuts import render
from django.http import HttpResponse
import json 
import urllib.request  

# Create your views here.
def index(request):
    if request.method== 'POST' :
        Country=request.POST['Country']
        request_url=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+Country+'&appid=a9c0805ff9b9abfb69d1e1a5b18e215d').read()
        json_data=json.loads(request_url) 
        data = {
            "country_code" :str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon']) + ' ' +
            str(json_data ['coord'] ['lat']),
            "temp" : str(json_data['main'][ 'temp']) + 'k',
            "pressure" :str(json_data['main']['pressure']),
            "humidity": str(json_data ['main']['humidity']),
        }


    else:
        data ={} 
        Country=''


    return render(request,'index.html',{'Country':Country , 'data':data})
    


 