"""
FUNCTIONS FOR RETRIEVING GAME DATA FROM API-WEB.NHLE.COM/
"""

from ...core.config import V
from ...core.transport import _call_api_get

# ==========================================================================
# SCHEDULE
# ==========================================================================

def _get_daily_scores_now() -> dict: 
    """
    Retrieve daily scores as of the current moment
    """
    endpoint = f"{V}/score/now"
    scores: dict = _call_api_get(endpoint=endpoint)
    return scores

def _get_daily_scores(date: str) -> dict: 
    """
    Retrieve daily scores by date
    date: YYYY-MM-DD
    """
    endpoint = f"{V}/score/{date}"
    scores: dict = _call_api_get(endpoint=endpoint)
    return scores

def _get_scoreboard_now() -> dict: 
    """
    Retrieve the overall scoreboard as of the current moment
    """
    endpoint = f"{V}/scoreboard/now"
    scoreboard: dict = _call_api_get(endpoint=endpoint)
    return scoreboard

# ==========================================================================
# WHERE TO WATCH
# ==========================================================================

def _get_streams() -> dict: 
    """
    Retrieve information about streaming options
    """
    endpoint = f"{V}/where-to-watch"
    scoreboard: dict = _call_api_get(endpoint=endpoint)
    return scoreboard

# ==========================================================================
# GAME EVENTS
# ==========================================================================

def _get_play_by_play(game_id: int) -> dict: 
    """
    Retrieve play-by-play information for a specific game
    game_id: unique game ID
    """
    endpoint = f"{V}/gamecenter/{game_id}/play-by-play"
    play_by_play: dict = _call_api_get(endpoint=endpoint)
    return play_by_play

def _get_game_landing(game_id: int) -> dict: 
    """
    Retrieve landing information for a specific game
    game_id: unique game ID
    """
    endpoint = f"/{V}/gamecenter/{game_id}/landing"
    landing: dict = _call_api_get(endpoint=endpoint)
    return landing

def _get_boxscore(game_id: int) -> dict: 
    """
    Retrieve boxscore information for a specific game
    game_id: unique game ID
    """
    endpoint = f"{V}/gamecenter/{game_id}/boxscore"
    boxscore: dict = _call_api_get(endpoint=endpoint)
    return boxscore
    
def _get_game_story(game_id: int) -> dict:
    """
    Retrieve game story information for a specific game
    game_id: unique game ID
    """
    endpoint = f"{V}/wsc/game-story/{game_id}"
    game_story: dict = _call_api_get(endpoint=endpoint)
    return game_story

# ==========================================================================
# NETWORK
# ==========================================================================

def _get_tv_schedule_now() -> dict:
    """
    Retrieve the current TV schedule
    """
    endpoint = f"{V}/network/tv-schedule/now"
    schedule: dict= _call_api_get(endpoint=endpoint)
    return schedule

def _get_tv_schedule(date: str) -> dict:
    """
    Retrieve the TV schedule for a specific date
    date: YYYY-MM-DD
    """
    endpoint = f"{V}/network/tv-schedule/{date}"
    schedule: dict = _call_api_get(endpoint=endpoint)
    return schedule
    
# ==========================================================================
# PARTNER ODDS
# ==========================================================================

def _get_odds(country_code: str) -> dict:
    """
    Retrieve odds for games in a specific country as of the current moment
    country_code: official country code
    """
    endpoint = f"{V}/partner-game/{country_code}/now"
    odds: dict = _call_api_get(endpoint=endpoint)
    return odds

# ==========================================================================
# PLAYOFFS
# ==========================================================================

def _get_playoff_carousel(season: int) -> dict:
    """
    Retrieve an overview of each playoff series
    season: YYYYYYYY
    """
    endpoint = f"{V}/playoff-series/carousel/{season}/"
    carousel: dict = _call_api_get(endpoint=endpoint)
    return carousel

def _get_playoff_series(season: int, series_letter: str) -> dict:
    """
    Retrieve the schedule for a specific playoff series
    season: YYYYYYYY
    series_letter: "A" or "B" or "C" ...
    """
    endpoint = f"{V}/schedule/playoff-series/{season}/{series_letter}/"
    series: dict = _call_api_get(endpoint=endpoint)
    return series
    
def _get_playoff_bracket(year: int) -> dict:
    """
    Retrieve the schedule for a specific playoff series
    year: YYYY
    """
    endpoint = f"{V}/playoff-bracket/{year}"
    bracket: dict = _call_api_get(endpoint=endpoint)
    return bracket

