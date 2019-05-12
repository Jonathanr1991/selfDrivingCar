from django.shortcuts import render, redirect
from car import Corvette
from django.views.generic import TemplateView
from  django.http import HttpResponse
from car import testcam



class Controller():
   

    def home_view(request, *args, **kwargs):
        camera= testcam.cam()
        camera.start()
        return render(request,'dashboard.html', {})

    def go_foward(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('foward')
        print(direction)
        if direction=='foward':
            car.forward()
        return render(request, 'dashboard.html',{})

    def go_back(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('back')
        print(direction)
        if direction=="back":
            car.reverse()
        return render(request, 'dashboard.html',{})
        
    def go_right(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('right')
        print(direction)
        if direction=="right":
            car.right()
        return render(request, 'dashboard.html',{})
    
    def go_left(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('left')
        print(direction)
        if direction=="left":
            car.left()
        return render(request, 'dashboard.html',{})

