# sports/forms.py
from django import forms
from .models import Sport, Team, Venue, Fixture, Player

class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = ['name']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'coach', 'sport']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location', 'capacity']

class FixtureForm(forms.ModelForm):
    class Meta:
        model = Fixture
        fields = ['sport', 'team_home', 'team_away', 'venue', 'match_date', 'result']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'team', 'position', 'age']
