from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fixture, Team, UserType
from .forms import *

@login_required
def index(request):
    # Redirect based on role in UserType model
    user_type = UserType.objects.filter(user=request.user).first()
    
    if user_type:
        if user_type.user_type == 'admin':
            return redirect('admin_dashboard')
        elif user_type.user_type == 'teamplayer':
            return redirect('coach_dashboard')
        elif user_type.user_type == 'viewer':
            return redirect('player_dashboard')
    
    fixtures = Fixture.objects.all().order_by('match_date')
    return render(request, 'index.html', {'fixtures': fixtures})

def fixture_detail(request, fixture_id):
    fixture = get_object_or_404(Fixture, pk=fixture_id)
    return render(request, 'fixture_detail.html', {'fixture': fixture})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    players = team.player_set.all()
    return render(request, 'team_detail.html', {'team': team, 'players': players})

@login_required
def admin_dashboard(request):
    # Only users with admin role can access this page
    user_type = UserType.objects.filter(user=request.user).first()
    if not user_type or user_type.user_type != 'admin':
        return redirect('index')

    # Fetching all models for display in the admin dashboard
    sports = Sport.objects.all()
    teams = Team.objects.all()
    venues = Venue.objects.all()
    fixtures = Fixture.objects.all().order_by('match_date')
    players = Player.objects.all()

    return render(request, 'admin_dashboard.html', {
        'sports': sports,
        'teams': teams,
        'venues': venues,
        'fixtures': fixtures,
        'players': players
    })

@login_required
def coach_dashboard(request):
    # Only users with teamplayer role can access this page
    user_type = UserType.objects.filter(user=request.user).first()
    if not user_type or user_type.user_type != 'teamplayer':
        return redirect('index')

    # Coach-specific logic here (e.g., manage fixtures, players)
    return render(request, 'coach_dashboard.html')

@login_required
def player_dashboard(request):
    # Only users with viewer role can access this page
    user_type = UserType.objects.filter(user=request.user).first()
    if not user_type or user_type.user_type != 'viewer':
        return redirect('index')

    # Player-specific logic here (e.g., view fixtures, player stats)
    return render(request, 'sports/player_dashboard.html')
@login_required
def add_sport(request):
    if request.method == 'POST':
        form = SportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = SportForm()
    return render(request, 'add_sport.html', {'form': form})

@login_required
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TeamForm()
    return render(request, 'add_team.html', {'form': form})

@login_required
def add_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = VenueForm()
    return render(request, 'add_venue.html', {'form': form})

@login_required
def add_fixture(request):
    if request.method == 'POST':
        form = FixtureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FixtureForm()
    return render(request, 'add_fixture.html', {'form': form})

@login_required
def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = PlayerForm()
    return render(request, 'add_player.html', {'form': form})
def home(request):
    fixtures = Fixture.objects.all().order_by('match_date')
    return render(request,"index.html",{'fixtures': fixtures})