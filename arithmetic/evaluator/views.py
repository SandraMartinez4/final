from django.shortcuts import render

def home(request):
    result1 = None
    result2 = None
    error = None

    if request.method == 'POST':
        try:
            x = float(request.POST.get('x'))
            y = float(request.POST.get('y'))
            result1 = x * x  # Ejemplo: cuadrado de X
            result2 = x + y - 2  # Ejemplo: suma menos 2

        except Exception as e:
            error = f"Error: {e}"

    return render(request, 'evaluator/index.html', {
        'result1': result1,
        'result2': result2,
        'error': error
    })

