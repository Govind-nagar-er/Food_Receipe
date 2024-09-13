from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
        {'Name':'Govind', 'age': 25},
        {'Name':'Rahul', 'age': 29},
        {'Name':'Hariom', 'age': 23},
        {'Name':'Payal', 'age': 20},
        {'Name':'Rohit', 'age': 15},
        {'Name':'Raju', 'age': 30}
    ]

    vegetables = ['Aloo', 'Gobii','Palak','kaddu']
    # for i in peoples:
    #     print(i)
    # return HttpResponse('<h1>Hey I am Django Server</h1>')
    return render(request, 'demo/index.html', context= {'page':'Django Tutorial 2024','peoples': peoples, 'vegetables':vegetables})
def contact(request):
    context = {'page':'Contact'}
    return render(request, 'demo/contact.html', context)
def about(request):
    context = {'page':'About'}
    return render(request, 'demo/about.html', context)

def success_page(request):
    return HttpResponse('<h1>Hey this is the success page2</h1>')
