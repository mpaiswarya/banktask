# from django.shortcuts import render, redirect, get_object_or_404
#
# from .forms import PersonCreationForm
# from .models import Person,Branch
#
#
# def person_create_view(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         data="completed"
#     return render(request, 'form.html', {'form': form})
#
#
# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'form.html', {'form': form})
#
