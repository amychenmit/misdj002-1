from django.shortcuts import render

from .models import Note
def index(request):
    list = Note.objects.order_by('seq')
    context = {'list': list}
    return render(request, 'note/index.html', context)