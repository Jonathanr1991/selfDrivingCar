from django.shortcuts import render, redirect
from car import Corvette
from django.views.generic import TemplateView
from  django.http import HttpResponse



class Controller():
    car = Corvette.CorvetteController()

    def home_view(request, *args, **kwargs):
        return render(request,'dashboard.html', {})

    def go_foward(request, self):
        direction = request.POST.get('foward')
        print(direction)
        if direction=='foward':
            self.car.foward(self)
        return render(request, 'dashboard.html',{})

    def go_back(request, self):
        direction = request.POST.get('back')
        print(direction)
        if direction=="back":
            self.car.reverse(self)
        return render(request, 'dashboard.html',{})
        
    def go_right(request, self):
        direction = request.POST.get('right')
        print(direction)
        if direction=="right":
            self.car.right(self)
        return render(request, 'dashboard.html',{})
    
    def go_left(request, self):
        direction = request.POST.get('left')
        print(direction)
        if direction=="left":
            self.car.foward(self)
        return render(request, 'dashboard.html',{})

