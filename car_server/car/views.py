from django.shortcuts import render
from car import CorvetteController


class Controller():
    car = CorvetteController()

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