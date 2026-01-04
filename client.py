"""
NHL CLIENT
"""

from .services import Players, Teams

class NhlClient:
    def __init__(self): 
        self.players = Players
        self.teams = Teams



# Currently only for testing purposes
def main() -> None: 
    nhl = NhlClient()
    players = nhl.players()

    player = players.get(pid=8477492) # MacKinnon
    # player = players.get(pid=8478550) # Panarin
    # player = players.get(pid=8451101) # Sakic

    print(player)
    print(f"Player first name: {player.bio.first_name.get_locale("cs")}")
    print(f"Player last name: {player.bio.last_name}")
    print(f"Current Team: {player.bio.team}")
    print(f"Weight: {player.bio.weight.weight_lbs}")
    print(f"Height: {player.bio.height}")
    print(f"Player draft year: {player.bio.draft.year}")
    print(f"Player home city: {player.bio.birth_details.city}")
    print(f"Player home state/Province: {player.bio.birth_details.state_province}")
    print(f"In Hockey Hall of Fame: {player.bio.legacy.in_HHOF}")
    print(f"In top 100 All Time: {player.bio.legacy.in_top_100_all_time}")
    print(f"Is actively playing: {player.bio.is_active}")
    print(f"Player headshot: {player.bio.media.headshot}")
    print("")
    badges = player.bio.legacy.badges
    print("Player Badges:")
    for badge in badges: 
        print(badge)
    awards = player.bio.legacy.awards
    print("")
    print("Player Awards:")
    for award in awards:
        print(award)


if __name__ == "__main__": 
    main()