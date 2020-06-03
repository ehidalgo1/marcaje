from datetime import date, datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .models import Marcaje
import json

# Create your views here.
def login(request):
    if request.POST:
        response_data = {'status' : 0, 'result' : ''}
        try:
            usuario = request.POST['usuario']
            password = request.POST['password']
            user = authenticate(request, username=usuario, password=password)
            #buscando usuario
            if user is not None:
                request.session['usuario_sesion'] = user.username
                auth_login(request, user)
                response_data['status'] = 200
                response_data['result'] = 'success'
            else:
                response_data['status'] = 100
                response_data['result'] = 'not found'
        except:
            response_data['status'] = 500
            response_data['result'] = 'internal server error'        
        return JsonResponse(response_data)
    return render(request, 'login.html')

def registro(request):
    if request.POST:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['usuario']
        password = request.POST['password']
        user = User.objects.create_user(email.lower(), email.lower(), password)
        user.first_name = nombre.lower()
        user.last_name = apellido.lower()
        user.save()
        return redirect('login')
    return render(request, 'registro.html')

def marcaje(request):
    if request.user.is_authenticated:
        if request.POST:
            usuario = request.user.username
            fecha = date.today()
            hora = datetime.now().time()
            tipo = request.POST['tipo']
            marca = None
            try:
                marca = Marcaje.objects.get(fecha=fecha, usuario=usuario)
            except:
                marca = None
            response_data = {
                'status' : 200,
                'result' : 'success',
                'type' : '',
                'hora' : hora.strftime("%H:%M"),
                'message' : ''
            }
            if marca is None:
                if tipo == "entrada":
                    marca = Marcaje(fecha=fecha, entrada=hora, salida=None, usuario=usuario)
                    response_data['tipo'] = tipo
                else:
                    response_data['status'] = 300
                    response_data['result'] = 'not complete'
                    response_data['message'] = 'Debe marcar primero la entrada'

            else:
                if marca.entrada is not None and marca.salida is not None:
                    response_data['status'] = 300
                    response_data['result'] = 'failed'
                    response_data['message'] = 'Usted ya ha completado las marcas del dia'
                else:
                    if tipo == "salida":
                        if marca.salida is None:
                            marca.salida = hora
                            response_data['tipo'] = tipo
            marca.save()
            return JsonResponse(response_data)
        fecha = date.today()
        usuario = request.user.username
        try:
            marca = Marcaje.objects.get(fecha=fecha, usuario=usuario)
        except:
            marca = None
        #declarando para saber si existe marca del dia
        data_marca = {
            'usuario' : request.user.first_name.upper()+" "+request.user.last_name.upper(),
            'entrada' : None,
            'salida' : None
        }
        if marca is not None:
            data_marca['entrada'] = marca.entrada
            data_marca['salida'] = marca.salida
            # return JsonResponse(data_marca)
        context = {'marca' : data_marca}
        return render(request, 'marcaje.html', context)
    return redirect('login')

def marcas(request):
    if request.user.is_authenticated:
        usuario = request.user.username
        lista_marcajes = Marcaje.objects.filter(usuario=usuario)
        context = {'lista_marcajes':lista_marcajes}
        return render(request, 'marcas.html', context)
    else:
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('login')
    