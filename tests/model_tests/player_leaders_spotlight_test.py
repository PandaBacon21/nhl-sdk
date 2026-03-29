from unittest.mock import MagicMock
from src.models.players.leaders.player_leaders import LeadersTeam
from src.models.players.leaders.player_leaders import LeaderPlayer, GoalieStatLeaders, SkaterStatLeaders
from src.models.players.spotlight import Spotlight


# ==========================================================================
# LEADERS TEAM
# ==========================================================================

def test_leaders_team_from_dict() -> None:
    data = {
        "teamName": {"default": "Edmonton Oilers"},
        "teamAbbrev": "EDM",
        "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
    }
    team = LeadersTeam.from_dict(data)
    assert team.name.default == "Edmonton Oilers"
    assert team.code == "EDM"
    assert "EDM" in team.logo

def test_leaders_team_empty() -> None:
    team = LeadersTeam.from_dict({})
    assert team.name.default is None
    assert team.code is None
    assert team.logo is None

def test_leaders_team_to_dict_uses_str() -> None:
    team = LeadersTeam.from_dict({
        "teamName": {"default": "Edmonton Oilers"},
        "teamAbbrev": "EDM",
        "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
    })
    d = team.to_dict()
    assert d["name"] == "Edmonton Oilers"
    assert d["code"] == "EDM"

def test_leaders_team_to_dict_empty_name_is_empty_string() -> None:
    """str(LocalizedString(None)) returns '' not None."""
    team = LeadersTeam.from_dict({})
    d = team.to_dict()
    assert d["name"] == ""


# ==========================================================================
# LEADER PLAYER (from player_leaders.py, not edge_types.py)
# ==========================================================================

LEADER_PLAYER_DATA = {
    "value": 64,
    "id": "8478402",
    "firstName": {"default": "Connor"},
    "lastName": {"default": "McDavid"},
    "sweaterNumber": 97,
    "position": "C",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
    "teamName": {"default": "Edmonton Oilers"},
    "teamAbbrev": "EDM",
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
}

def test_leader_player_from_dict() -> None:
    player = LeaderPlayer.from_dict(LEADER_PLAYER_DATA)
    assert player.value == 64
    assert player.pid == "8478402"
    assert player.first_name.default == "Connor"
    assert player.last_name.default == "McDavid"
    assert player.number == 97
    assert player.position == "C"
    assert player.team.code == "EDM"

def test_leader_player_empty() -> None:
    player = LeaderPlayer.from_dict({})
    assert player.value is None
    assert player.pid is None
    assert player.first_name.default is None
    assert player.number is None

def test_leader_player_to_dict() -> None:
    player = LeaderPlayer.from_dict(LEADER_PLAYER_DATA)
    d = player.to_dict()
    assert d["value"] == 64
    assert d["id"] == "8478402"
    assert d["first_name"] == "Connor"
    assert d["last_name"] == "McDavid"
    assert d["sweater_number"] == 97
    assert d["team"]["code"] == "EDM"


# ==========================================================================
# SPOTLIGHT
# ==========================================================================

SPOTLIGHT_DATA = {
    "playerId": 8478402,
    "name": {"default": "Connor McDavid"},
    "playerSlug": "connor-mcdavid-8478402",
    "position": "C",
    "sweaterNumber": 97,
    "teamId": "22",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
    "teamTriCode": "EDM",
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
    "sortId": 1,
}

def test_spotlight_from_dict() -> None:
    spotlight = Spotlight.from_dict(SPOTLIGHT_DATA)
    assert spotlight.pid == 8478402
    assert spotlight.name.default == "Connor McDavid"
    assert spotlight.slug == "connor-mcdavid-8478402"
    assert spotlight.position == "C"
    assert spotlight.number == 97
    assert spotlight.team_id == "22"
    assert spotlight.team_code == "EDM"
    assert spotlight.sort_id == 1

def test_spotlight_empty() -> None:
    spotlight = Spotlight.from_dict({})
    assert spotlight.pid is None
    assert spotlight.name.default is None
    assert spotlight.slug is None
    assert spotlight.sort_id is None

def test_spotlight_to_dict() -> None:
    spotlight = Spotlight.from_dict(SPOTLIGHT_DATA)
    d = spotlight.to_dict()
    assert d["player_id"] == 8478402
    assert d["name"] == "Connor McDavid"
    assert d["slug"] == "connor-mcdavid-8478402"
    assert d["position"] == "C"
    assert d["sweater_number"] == 97
    assert d["team_code"] == "EDM"
    assert d["sort_id"] == 1

def test_spotlight_to_dict_name_uses_str() -> None:
    """to_dict uses str(name) which returns '' for missing, not None."""
    spotlight = Spotlight.from_dict({})
    d = spotlight.to_dict()
    assert d["name"] == ""


# ==========================================================================
# GOALIE LEADERS
# ==========================================================================

GOALIE_LEADER_ENTRY = {
    "value": 30,
    "id": "8478048",
    "firstName": {"default": "Andrei"},
    "lastName": {"default": "Vasilevskiy"},
    "sweaterNumber": 88,
    "position": "G",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/TBL/8478048.png",
    "teamName": {"default": "Tampa Bay Lightning"},
    "teamAbbrev": "TBL",
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/TBL_light.svg",
}

def test_goalie_stat_leaders_from_dict() -> None:
    data = {
        "wins": [GOALIE_LEADER_ENTRY],
        "shutouts": [GOALIE_LEADER_ENTRY],
        "savePctg": [GOALIE_LEADER_ENTRY],
        "goalsAgainstAverage": [GOALIE_LEADER_ENTRY],
    }
    leaders = GoalieStatLeaders(data=data)
    assert len(leaders.wins) == 1
    assert leaders.wins[0].last_name.default == "Vasilevskiy"
    assert len(leaders.shutouts) == 1
    assert len(leaders.save_pctg) == 1
    assert len(leaders.goals_against_avg) == 1

def test_goalie_stat_leaders_empty() -> None:
    leaders = GoalieStatLeaders(data={})
    assert leaders.wins == []
    assert leaders.shutouts == []
    assert leaders.save_pctg == []
    assert leaders.goals_against_avg == []


# ==========================================================================
# SKATER LEADERS
# ==========================================================================

SKATER_LEADER_ENTRY = {
    "value": 64,
    "id": "8478402",
    "firstName": {"default": "Connor"},
    "lastName": {"default": "McDavid"},
    "sweaterNumber": 97,
    "position": "C",
    "headshot": "https://assets.nhle.com/mugs/nhl/20232024/EDM/8478402.png",
    "teamName": {"default": "Edmonton Oilers"},
    "teamAbbrev": "EDM",
    "teamLogo": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
}

def test_skater_stat_leaders_from_dict() -> None:
    data = {
        "goals": [SKATER_LEADER_ENTRY],
        "goalsSh": [SKATER_LEADER_ENTRY],
        "goalsPp": [SKATER_LEADER_ENTRY],
        "assists": [SKATER_LEADER_ENTRY],
        "points": [SKATER_LEADER_ENTRY],
        "plusMinus": [SKATER_LEADER_ENTRY],
        "penaltyMins": [SKATER_LEADER_ENTRY],
        "faceoffLeaders": [SKATER_LEADER_ENTRY],
        "toi": [SKATER_LEADER_ENTRY],
    }
    leaders = SkaterStatLeaders(data=data)
    assert len(leaders.goals) == 1
    assert leaders.goals[0].last_name.default == "McDavid"
    assert len(leaders.assists) == 1
    assert len(leaders.points) == 1
    assert len(leaders.goals_sh) == 1
    assert len(leaders.goals_pp) == 1
    assert len(leaders.plus_minus) == 1
    assert len(leaders.penalty_min) == 1
    assert len(leaders.faceoff_leaders) == 1
    assert len(leaders.toi) == 1

def test_skater_stat_leaders_empty() -> None:
    leaders = SkaterStatLeaders(data={})
    assert leaders.goals == []
    assert leaders.assists == []
    assert leaders.points == []
    assert leaders.toi == []
