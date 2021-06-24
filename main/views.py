from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    request.session['truck'] = request.POST['truck_name']
    request.session['region'] = request.POST['region']
    request.session['special'] = request.POST['special']

    return redirect('/truck_dash')


def dashboard(request):
    context = {
        'truck': request.session['truck'],
        'region': request.session['region'],
        'special': request.session['special']
    }
    return render(request, 'truck.html', context)
