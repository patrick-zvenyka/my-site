from django.shortcuts import render

def handler400(request, exception=None):
    return render(request, 'errorhandlers/400.html', status=400)

def handler403(request, exception=None):
    return render(request, 'errorhandlers/403.html', status=403)

def handler404(request, exception=None):
    return render(request, 'errorhandlers/404.html', status=404)

def handler500(request):
    return render(request, 'errorhandlers/500.html', status=500)
