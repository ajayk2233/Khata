from django.shortcuts import render,redirect


def about(request):
    return render(request,'about.html')

def previous_url(request):
    previous = request.META.get('HTTP_REFERER')
    print(previous)
    return redirect(previous)