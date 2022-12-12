from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from miportafolio.models import Usuario
from miportafolio.forms import LoginUser, RegistrarUser


from datetime import datetime
# Create your views here.

class index_view(View):
    template_get = 'index.html'
    def get(self, request):
        context = {'name': 'Alex'}
        return render(request, self.template_get, context)

    def post(self, request):
        return HttpResponse('Soy POST de index_view')

class registrarse_view(View):
    def get(self, request):
        registro = RegistrarUser()
        context = {'form': registro}
        return render(request, 'registrarse.html', context)
    
    def post(self, request): 
        usuario = RegistrarUser(request.POST)    
        if usuario.is_valid():
            f = Usuario(nombre=request.POST.get('nombre'),user_name=request.POST.get('user_name'),
            password=request.POST.get('password'))
            f.save()  
            # login = LoginUser()
            # context = {'form': login}
            nv_usuario = RegistrarUser() 
            context = {'form': nv_usuario,"mensaje":"ok"}
            return render(request, 'registrarse.html', context)

# class form_view(View):
#     template_get = 'form.html'
#     template_post = 'Hola soy POST de form_view'

#     def get(self, request):
#         formulario = InputForm()
#         context = {'form': formulario}

#         return render(request, self.template_get, context)

#     def post(self, request):
#         form = InputForm(request.POST)
#         if form.is_valid():
#             request.session['hora_entrada'] = str(form.cleaned_data['hora_entrada'])

#             return redirect('aula_view', aula=form.cleaned_data['aula'])


class login_view(View):
    def get(self, request):
        login = LoginUser()
        context = {'form': login}
        return render(request, 'login.html', context)

    def post(self, request): 
        formulario = LoginUser(request.POST)    
        if request.method == "POST":
             if formulario.is_valid():
                nom = request.POST.get('user_name')
                pas = request.POST.get('password')
                comprobarLogin = Usuario.objects.filter(user_name = nom, password = pas).values()
                if comprobarLogin:
                    print(comprobarLogin[0])
                    request.session["estadoSesion"] = True
                    request.session["idUsuario"] = comprobarLogin[0]['id']
                    request.session["nombre"] = comprobarLogin[0]['nombre']
                    return redirect('/miportafolio/')
                else:
                    context = {'form': formulario,"mensaje":"Error de Usuario y/o Contraseña"}
                    return render(request, "login.html", context)

        else:
            datos = {'r2' : "no se puede procesar la solicitud"}
            return render(request, "login.html", datos)


class miportafolio_view(View):
    template_get = 'miportafolio.html'
    def get(self, request):
        print(request.session.get('idUsuario'))
        context = {'name': 'Alex'}
        return render(request, self.template_get, context)

    def post(self, request):
        return HttpResponse('Soy POST de index_view')