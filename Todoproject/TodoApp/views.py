from django.shortcuts import render,redirect
import requests

# Create your views here.
def Home(request):
    data=None
    cat=None
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        cat=list(set(product['category'] for product in data['products']))
        print(data)
    return render(request,'index.html',{'cat':cat,'data':data})   


def Details(request,id):
    data=None
    urls='https://dummyjson.com/products/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
    return render(request,'details.html',{'data':data})  



def smart(request,cat):
    a=[]
    print(cat)
    urls='https://dummyjson.com/products/'+str(id)
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        for i in data['products']:
            if cat in i['category']:
                a.append(i)
        print(a)        
    return render(request,'smart.html',{'data':a})  
