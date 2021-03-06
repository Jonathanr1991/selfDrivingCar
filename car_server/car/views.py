from django.shortcuts import render, redirect
from car import Corvette
from django.views.generic import TemplateView
from  django.http import HttpResponse
from time import sleep


class Controller():
   

    def home_view(request, *args, **kwargs):
        return render(request,'dashboard.html', {})

    def go_forward(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('forward')
        print(direction)
        if direction=='forward':
            car.forward()
            sleep(0.5)
            car.release()
        return render(request, 'dashboard.html',{})

    def go_reverse(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('reverse')
        print(direction)
        if direction=="reverse":
            car.reverse()
            sleep(0.5)
            car.release()
        return render(request, 'dashboard.html',{})
        
    def go_reverse_right(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('reverse_right')
        print(direction)
        if direction=="reverse_right":
            car.reverse_right()
            sleep(0.5)
            car.release()
        return render(request, 'dashboard.html',{})
    
    def go_reverse_left(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('reverse_left')
        print(direction)
        if direction=="reverse_left":
            car.reverse_left()
            sleep(0.5)
            car.release()
        return render(request, 'dashboard.html',{})

    def go_forward_right(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('forward_right')
        print(direction)
        if direction=="forward_right":
            car.forward_right()
            sleep(0.5)
            car.release()
        return render(request, 'dashboard.html',{})
    
    def go_forward_left(request):
        car = Corvette.CorvetteController()
        direction = request.POST.get('forward_left')
        print(direction)
        if direction=="forward_left":
            car.forward_left()
            sleep(0.5)
            car.release()
        return render(request, 'dashboard.html',{})


