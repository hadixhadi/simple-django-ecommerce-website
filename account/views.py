from django.shortcuts import render , HttpResponse , redirect
from .forms import registerForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def register(request):
     form = registerForm()

     if request.method == 'POST':

            form = registerForm(request.POST)

            if form.is_valid(): 

                form.save()
                return redirect('store')
            else:
                 return HttpResponse('for is not valid')
     else:
        context = {'form':form}
        return render(request, 'account/registeration/register.html', context=context)
    