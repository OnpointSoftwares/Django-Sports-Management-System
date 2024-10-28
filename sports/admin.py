from django.contrib import admin
from .models import Sport, Team, Venue, Fixture, Player, MatchStat,UserType
admin.site.register(UserType)
admin.site.register(Sport)
admin.site.register(Team)
admin.site.register(Venue)
admin.site.register(Fixture)
admin.site.register(Player)
admin.site.register(MatchStat)
