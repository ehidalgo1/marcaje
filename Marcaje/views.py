from django.shortcuts import render,redirect
from Marcaje.models import Usuario,Marcaje
from datetime import date,datetime

# Create your views here.
def get_home(request):
    if request.POST:
        usuario=request.POST.get('usuario')
        password=request.POST.get('password')
        user = Usuario.objects.get(usuario=usuario,password=password)
        if user:
            request.session['usuario_sesion'] = user.id
            return redirect('marcaje')
    return render(request,'index.html')

def get_registro(request):
    if request.POST:
        nombre=request.POST.get('nombre')
        apellido=request.POST.get('apellido')
        usuario=request.POST.get('usuario')
        password=request.POST.get('password')
        User=Usuario(nombre=nombre.upper(),apellido=apellido.upper(),usuario=usuario.lower(),password=password)
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