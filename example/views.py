# example/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        # PEGA OS VALORES DO FORM
        meta_str = request.POST.get('meta')
        economia_str = request.POST.get('economia')

        try:
        # CONVERTER EM NUMERO
            meta = float(meta_str)
            economia = float(economia_str)

            if (meta != 0) or (economia != 0):
                res =  float(meta) / float(economia)
                resultado = f'Levará {res} meses até atingir a meta!'
            else:
                resultado = 'Os valores não podem ser zero.'

            if economia > meta:
                resultado = 'A economia não pode ser maior que a meta.'

        except ValueError:
            resultado = 'Insira apenas números.'

        return render(request, 'index.html', {'resultado': resultado})

    return render(request, 'index.html')
