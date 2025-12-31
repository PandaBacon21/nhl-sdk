"""
Players Collection
"""

from typing import Optional
from datetime import datetime

from ..resources.api_web import players
from .player import Player

class Players: 
    
    def get(self, pid: int) -> "Player": 
        return Player(player_id=pid)





def main() -> None: 
    players = Players()
    # player = players.get(pid=8477492)
    player = players.get(pid=8478550)
    print(player)
    print(f"Player last name: {player.bio.last_name}")
    print(f"Current Team: {player.bio.team.name}")
    print(f"Weight in pounds: {player.bio.weight.weight_lbs} lbs")
    print(f"Player draft year: {player.bio.draft.year}")
    print(f"Player home city: {player.bio.birth_details.city}")
    print(f"Player home state/Province: {player.bio.birth_details.state_province}")
    print(f"In Hockey Hall of Fame: {player.bio.legacy.in_HHOF}")
    print(f"Is actively playing: {player.bio.is_active}")


if __name__ == "__main__": 
    main()