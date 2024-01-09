from django.shortcuts import render, redirect
from django.contrib.auth import login
from .form import Registro


# Front page
def front(request):
    return render (request, 'core/front.html')

#funcao de registro
def registro(request):
    if request.method == 'POST':
        form = Registro(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')

    else:
        form = Registro()

    return render(request, 'core/registro.html',{'form':form})