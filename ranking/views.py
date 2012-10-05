# Create your views here.

from ranking.models import Team, Match, Season
from ranking.forms import MatchForm, UserForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect(reverse(index))

def index(request):
  teams = Team.objects.all().order_by('-score')
  matches = Match.objects.all().order_by('-round')
  d = dict(teams=teams, matches=matches, request=request)
  form = None
  if request.POST:
    form = UserForm(request.POST)
    if not form.errors:
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None and user.is_staff:
          auth.login(request, user)
          request.user = user
          return HttpResponseRedirect(reverse(index))
        d.update(auth_failed=True)
  else:
    if request.user.is_anonymous():
      form = UserForm()
  if form: d.update(form=form)
  return render_to_response('index.html', d, 
                            context_instance=RequestContext(request))

def add(request):
  pass

def update(request, pk):
  match = get_object_or_404(Match, pk=pk)
  if request.POST:
    form = MatchForm(request.POST)
    if not form.errors:
      cleaned_data = form.cleaned_data;
      match.host_score = cleaned_data['host_score']
      match.visitor_score = cleaned_data['visitor_score']
      match.finished = True
      update_team_info(match)
      match.save()
      match.host.save()
      match.visitor.save()
      return HttpResponseRedirect(reverse(index))
  else:  
    form = MatchForm()
  d = dict(match=match, form=form)
  return render_to_response('update_form.html', d, 
                            context_instance=RequestContext(request))
  
def update_team_info(match):
  match.host.matches += 1
  match.visitor.matches += 1
  match.host.conceded += match.visitor_score
  match.host.goal += match.host_score
  match.visitor.goal += match.visitor_score
  match.visitor.conceded += match.host_score
  match.host.goal_diff = match.host.goal - match.host.conceded
  match.visitor.goal_diff = match.visitor.goal - match.visitor.conceded
  
  
  if match.host_score > match.visitor_score:
    match.host.won += 1
    match.host.score += 3
    match.visitor.lost += 1
  elif match.host_score < match.visitor_score:
    match.visitor.won += 1
    match.visitor.score += 3
    match.host.lost += 1
  else:
    match.host.draw += 1
    match.visitor.draw += 1
    match.host.score += 1
    match.visitor.score += 1