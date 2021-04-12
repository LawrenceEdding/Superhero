from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Hero
from .forms import HeroForm


# Create your views here.


def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    hero = Hero.objects.filter(pk=hero_id).get()
    context = {
        'hero': hero
    }
    return render(request, 'heroes/detail.html', context)


def create(request):
    context = {}
    form = HeroForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    context['form'] = form
    return render(request, 'heroes/create.html', context)


def delete(request, hero_id):
    context = {}
    hero = Hero.objects.filter(pk=hero_id).get()
    hero.delete()
    context['hero'] = hero
    return render(request, 'heroes/delete.html', context)


def update(request, hero_id):
    context = {}
    hero = Hero.objects.get(pk=hero_id)
    form = HeroForm(request.POST, instance=hero)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    context['form'] = form
    return render(request, 'heroes/update.html', context)
