# Create your views here.

from ranking.models import Team, Match, Season
from django.shortcuts import render_to_response

def index(request):
  teams = Team.objects.all().order_by('-score')
  d = dict(teams=teams)
  return render_to_response('index.html', d)

def add(request):
  pass

def update(request):
  pass