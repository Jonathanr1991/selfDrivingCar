from django.shortcuts import render, redirect
from car import CorvetteController
from django.views.generic import TemplateView
from  django.http import HttpResponse



class Controller():
    car = CorvetteController()

    def home_view(request, *args, **kwargs):
        return render(request,'car/dashboard.html', {})

    def go_foward(request):
        direction = request.POST.get('foward')
        print(direction)
        if direction=='foward':
            car.foward()
        return render(request, 'dashboard.html',{})

    def go_back(request):
        direction = request.POST.get('Back')
        print(direction)
        if direction=="Back":
            car.reverse()
        return render(request, 'dashboard.html',{})
        
    def go_right(request):
        direction = request.POST.get('Right')
        print(direction)
        if direction=="Right":
            car.right()
        return render(request, 'dashboard.html',{})
    
    def go_left(request):
        direction = request.POST.get('Left')
        print(direction)
        if direction=="Left":
            car.foward()
        return render(request, 'dashboard.html',{})

