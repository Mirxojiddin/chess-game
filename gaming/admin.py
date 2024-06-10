from django.contrib import admin
from gaming.models import Country, Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "games_played"]


admin.site.register(Country)
admin.site.register(Player, PlayerAdmin)
