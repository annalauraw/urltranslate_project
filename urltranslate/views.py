from django.shortcuts import render


def translate_url(request):
    context = {"available_languages": ["en", "de"]}
    return render(request, "urltranslate/welcome.html", context)
