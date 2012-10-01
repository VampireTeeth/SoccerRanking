'''
Created on Oct 1, 2012

@author: steven
'''

from django.contrib import admin
from ranking.models import Team, Season, Match

class TeamAdmin(admin.ModelAdmin):
  fields = ['name', 'season']
  
class SeasonAdmin(admin.ModelAdmin):
  pass

class MatchAdmin(admin.ModelAdmin):
  list_display = ['season', 'round', 'host', 'visitor', 'host_score', 'visitor_score', 'finished']
  fields = ['season', 'round', 'host', 'visitor']


admin.site.register(Team, TeamAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Match, MatchAdmin)