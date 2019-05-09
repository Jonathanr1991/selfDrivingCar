from django.shortcuts import render, redirect
from car import CorvetteController
from django.views.generic import TemplateView
from  django.http import HttpResponse



class Controller():
    car = CorvetteController()

    def home_view(request, *args, **kwargs):
        return render(request,'dashboard.html', {})

    def go_foward(request):
        direction = request.POST.get('foward')
        print(direction)
        if direction=='foward':
            car.foward()
        return render(request, 'dashboard.html',{})

    def go_back(request):
        direction = request.POST.get('back')
        print(direction)
        if direction=="back":
            car.reverse()
        return render(request, 'dashboard.html',{})
        
    def go_right(request):
        direction = request.POST.get('right')
        print(direction)
        if direction=="right":
            car.right()
        return render(request, 'dashboard.html',{})
    
    def go_left(request):
        direction = request.POST.get('left')
        print(direction)
        if direction=="left":
            car.foward()
        return render(request, 'dashboard.html',{})

