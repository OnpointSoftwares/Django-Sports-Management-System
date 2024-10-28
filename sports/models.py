from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class UserType(models.Model):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('teamplayer', 'Team Player'),
        ('viewer', 'Viewer'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

class Venue(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    team_home = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    team_away = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    result = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.team_home} vs {self.team_away}'

class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class MatchStat(models.Model):
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)

    def __str__(self):
        return f'Stats for {self.player} in {self.fixture}'
