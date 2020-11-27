from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expert
from .forms import search_drop_down, EditExpert
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

def edit_profile(request):
    if request.method == "POST":
        form = edit_profile(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = edit_profile(request)
            return render(request, 'editexpert.html', {'form': form})

def index(request):
    search = search_drop_down()
    return render(request, "search.html", {
            "form": search
        })

def display_expert(request, pk):
    # pk is search string, want to search by last name (for now)
    expert = Expert.objects.get(pk=pk)
    results = {
        'expert': expert
    }
    return render(request, "display_expert.html", results)


def search_results(request):
    search_for = request.POST
    # POST returns dict value, need to search db by type for value specified, then
    # iterate through results, putting first+lastName into listbox and record ID

    form = None
    if search_for['search_by'] == 'name':
        query_results = Expert.objects.all().filter(lastName__contains=search_for['search_term'])
    if search_for['search_by'] == 'skill':
        query_results = Expert.objects.all().filter(techSkills__contains=search_for['search_term'])
    if search_for['search_by'] == 'class':
        query_results = Expert.objects.all().filter(courseWork__contains=search_for['search_term'])
    if search_for['search_by'] == 'organization':
        query_results = Expert.objects.all().filter(organization__contains=search_for['search_term'])

    # TODO handle no results, probably in search_results.html body
    results = {
        'query': query_results
    }

    return render(request, "search_results.html", results)

def edit(request, pk):
    try:
        data_to_edit = get_object_or_404(Expert, id= pk)
    except Exception:
        raise Http404('No entry')
    if request.method == 'POST':
        form = EditExpert(request.POST, instance=data_to_edit)

        if form.is_valid():
            form.save()
            return display_expert(request, pk)
    else:
        form = EditExpert(instance=data_to_edit)
        context = {
            'form': form
        }
        return render(request, 'editexpert.html', context)

class AddExpert(CreateView):
    model = Expert
    fields = ['firstName', 'lastName', 'avatar', 'organization', 'techSkills',
              'courseWork', 'gitRepo', 'linkedIn', 'twitter', 'email']
    template_name = 'expertFinder/expert_form.html'
    # success_url = reverse_lazy('expertFinder:search')

class EditExport(UpdateView):
    model = Expert
    fields = ['firstName', 'lastName', 'organization', 'techSkills',
              'courseWork', 'gitRepo', 'linkedIn', 'twitter', 'email']
    template_name = 'expertFinder/edit_expert.html'
    success_url = reverse_lazy('expertFinder:search')
