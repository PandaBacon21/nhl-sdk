"""
Players Space
"""

from typing import Optional, Literal
from datetime import datetime

from ..resources.api_web import players
from ..models.player import Player

class Players: 
    PlayerType = Literal["skater", "goalie"]
    StatType = Literal["goals", "goalsSh", "goalsPp", "assists", "points", "plusMinus", "faceOffLeaders", "penaltyMins", "toi"]
    
    def get(self, pid: int) -> "Player": 
        """Get player info for a specific player"""
        return Player(player_id=pid)


    # def get_stat_leaders(self, player_type: PlayerType, category: StatType | None = None, season: Optional[int] = None, 
    #                   game_type: Optional[int] = None, limit: Optional[int] = None) -> dict: 
    #     """
    #     Get stat leaders
        
    #     If 'season' is included, 'gametype' must also be included, and vice versa. 
    #     player_type: PlayerType
    #     category: Optional[str] = StatType
    #     season: Optional[int] = YYYYYYYY format
    #     game_type: Optional[int] = 2 (regular season), 3 (playoff)
    #     limit: Optional[int] = default = top 5, -1 returns all
    #     """
    #     if (season is None) ^ (game_type is None):
    #         raise ValueError(f"season and game_type must be either provided together or omitted together")
        


    



def main() -> None: 
    players = Players()
    # player = players.get(pid=8477492) # MacKinnon
    # player = players.get(pid=8478550) # Panarin
    player = players.get(pid=8451101) # Sakic

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