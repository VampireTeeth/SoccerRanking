from django.db import models

# Create your models here.
class Season(models.Model):
  name = models.CharField(max_length=100)
  
  def __unicode__(self):
    return self.name 
 
class Team(models.Model):
  rank = models.IntegerField(default=0)
  name = models.CharField(max_length=100)
  won = models.IntegerField(default=0)
  draw = models.IntegerField(default=0)
  lost = models.IntegerField(default=0)
  goal = models.IntegerField(default=0)
  conceded = models.IntegerField(default=0)
  goal_diff = models.IntegerField(default=0)
  score = models.IntegerField(default=0)
  season = models.ForeignKey(Season)
  
  
  def __unicode__(self):
    return self.name
  
 
class Match(models.Model):
  season = models.ForeignKey(Season)
  round = models.IntegerField()
  host = models.ForeignKey(Team, related_name='host_id')
  visitor = models.ForeignKey(Team, related_name='visitor_id')
  host_score = models.IntegerField(default=0)
  visitor_score = models.IntegerField(default=0)
  finished = models.BooleanField(default=False)
  
  def __unicode__(self):
    if self.finished:
      return unicode('%s %d:%d %s' % ( self.host.name, 
                                        self.host_score, 
                                        self.visitor_score, 
                                        self.visitor.name))
      
    return unicode('%s VS %s' % (self.host.name, self.visitor.name))

