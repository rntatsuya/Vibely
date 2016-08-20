from django.shortcuts import render

def profile(request):
    context = {
        'message': 'You are not logged in.'
    }
    return render(request, 'testapp/profile.html', context)
