from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .models import Mensaje
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'core/index.html')


def listar(request):
        lista_proyectos= Mensaje.objects.all()
        data={
             "lista_proyectos": lista_proyectos,
        } 
        return render(request,'core/ListarProyectos.html',data)

@login_required
def home_view(request):
    return render(request, 'core/base.html')

  
def iniciarsesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/ListarProyectos')
        else:
            return render(request, 'core/Listarproyectos.html')
    else:
        return render(request, 'core/iniciarsesion.html')
    
@login_required 
def logout_view(request):
        logout(request)
        return redirect('/iniciarsesion')

def nuevo_proyecto(request):
    return render(request, 'core/nuevo_proyecto.html')

def agregar_proyecto(request):
        if(request.POST):
            proyecto= request.POST['txtproyecto']
            tematica= request.POST['cboTematica']
            estudiantes=request.POST['txtestudiante']
            info=request.POST['txtinfo']  
            profe=request.POST['txtprofe']

            mensaje=Mensaje()
            mensaje.Nombree=proyecto
            mensaje.alumno=estudiantes
            mensaje.tipo=tematica
            mensaje.profesor=profe
            mensaje.informacion=info

            mensaje.save()

        return render(request,'core/nuevo_proyecto.html')