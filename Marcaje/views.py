from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from Marcaje.models import Usuario,Marcaje
from datetime import date,datetime
import json

# Create your views here.
def login(request):
    if request.POST:
        response_data = {'status' : 0,'result' : ''}
        try:
            usuario=request.POST['usuario']
            password=request.POST['password']
            user=None
            try:
                user=Usuario.objects.get(usuario=usuario, password=password)
            except Usuario.DoesNotExist:
                response_data['status'] = 100
                response_data['result'] = 'not found'
            if user is not None:
                response_data['status'] = 200
                response_data['result'] = 'success'
        except:
            response_data['status'] = 500
            response_data['result'] = 'internal server error'        
        return JsonResponse(response_data)
    return render(request,'login.html')

def get_registro(request):
    if request.POST:
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        usuario=request.POST.get('usuario')
        password=request.POST.get('password')
        User=Usuario(nombre=nombre.upper(),apellido=apellido.upper(),usuario=usuario.lower(),password=password,token=Generar_token.execute())
        User.save()
        return redirect('home')
    return render(request, 'registro.html')

def get_marcaje(request):
    if request.POST:
        id = request.session['usuario_sesion']
        fecha = date.today()
        hora = datetime.now().time()
        tipo = request.POST.get('tipo')
        usuario = Usuario.objects.get(id=id)
        marca = Marcaje(fecha=fecha,hora=hora,tipo=tipo,usuario=usuario)
        marca.save()
    return render(request, 'marcaje.html')

def get_marcas(request):
    lista_marcajes = Marcaje.objects.all()
    context = {'lista_marcajes':lista_marcajes}
    return render(request,'marcas.html', context)
    