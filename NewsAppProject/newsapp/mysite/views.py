from django.shortcuts import render
import requests 
# Create your views here.
#API_KEY ='d904768c9eac471b8ed56e8f33ced213'
def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=d904768c9eac471b8ed56e8f33ced213'
        response=requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url =f'https://newsapi.org/v2/top-headlines?country=in&apiKey=d904768c9eac471b8ed56e8f33ced213'
        response = requests.get(url)
        data=response.json()
        articles =data['articles']
    context={
        'articles':articles
    }
    return render(request,'home.html',context)
 
