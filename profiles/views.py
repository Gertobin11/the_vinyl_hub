from django.shortcuts import render


def profile(request):
    ''' Function to render a users profile page with
    his default delivery location, Profile pic and info
    about himself '''

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
