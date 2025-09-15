from django.shortcuts import render

def cal():
  x = 1
  y = 2
  return x + y

def say_hello(request):
  cal()
  return render(request, 'hello.html', {'name': 'Akmal', 'x': cal()})