"""
Tests for TeamEdgeLandingResult and related models.
"""
from nhl_sdk.models.teams.edge.team_landing.team_landing_result import (
    TeamEdgeLandingResult, TeamEdgeLandingLeaders, TeamEdgeLeaderTeam,
    LandingSogAreaDetail, TeamShotAttemptLeader, TeamBurstsLeader,
    TeamDistanceLeader, TeamHighDangerSOGLeader, TeamZoneTimeLeader,
)


LANDING_RESPONSE = {
    "seasonsWithEdgeStats": [
        {"id": 20242025, "gameTypes": [2, 3]},
        {"id": 20232024, "gameTypes": [2, 3]},
    ],
    "leaders": {
        "shotAttemptsOver90": {
            "team": {
                "id": 22,
                "commonName": {"default": "Oilers"},
                "placeNameWithPreposition": {"default": "Edmonton", "fr": "d'Edmonton"},
                "abbrev": "EDM",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/EDM_dark.svg",
                },
                "slug": "edmonton-oilers-22",
                "wins": 48,
                "losses": 29,
                "otLosses": 5,
            },
            "attempts": 136,
        },
        "burstsOver22": {
            "team": {
                "id": 21,
                "commonName": {"default": "Avalanche"},
                "placeNameWithPreposition": {"default": "Colorado", "fr": "du Colorado"},
                "abbrev": "COL",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/COL_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/COL_dark.svg",
                },
                "slug": "colorado-avalanche-21",
                "wins": 49,
                "losses": 29,
                "otLosses": 4,
            },
            "bursts": 212,
        },
        "distancePer60": {
            "team": {
                "id": 13,
                "commonName": {"default": "Panthers"},
                "placeNameWithPreposition": {"default": "Florida", "fr": "de la Floride"},
                "abbrev": "FLA",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/FLA_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/FLA_dark.svg",
                },
                "slug": "florida-panthers-13",
                "wins": 47,
                "losses": 31,
                "otLosses": 4,
            },
            "distanceSkated": {"imperial": 9.3410, "metric": 15.0322},
        },
        "highDangerSOG": {
            "team": {
                "id": 22,
                "commonName": {"default": "Oilers"},
                "placeNameWithPreposition": {"default": "Edmonton", "fr": "d'Edmonton"},
                "abbrev": "EDM",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/EDM_dark.svg",
                },
                "slug": "edmonton-oilers-22",
                "wins": 48,
                "losses": 29,
                "otLosses": 5,
            },
            "sog": 714,
            "shotLocationDetails": [
                {"area": "Behind the Net", "sog": 20, "rank": 5},
                {"area": "Low Slot", "sog": 603, "rank": 3},
            ],
        },
        "offensiveZoneTime": {
            "team": {
                "id": 12,
                "commonName": {"default": "Hurricanes"},
                "placeNameWithPreposition": {"default": "Carolina", "fr": "de la Caroline"},
                "abbrev": "CAR",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/CAR_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/CAR_dark.svg",
                },
                "slug": "carolina-hurricanes-12",
                "wins": 47,
                "losses": 30,
                "otLosses": 5,
            },
            "zoneTime": 0.4605141,
        },
        "neutralZoneTime": {
            "team": {
                "id": 25,
                "commonName": {"default": "Stars"},
                "placeNameWithPreposition": {"default": "Dallas", "fr": "de Dallas"},
                "abbrev": "DAL",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/DAL_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/DAL_dark.svg",
                },
                "slug": "dallas-stars-25",
                "wins": 50,
                "losses": 26,
                "otLosses": 6,
            },
            "zoneTime": 0.1873355,
        },
        "defensiveZoneTime": {
            "team": {
                "id": 12,
                "commonName": {"default": "Hurricanes"},
                "placeNameWithPreposition": {"default": "Carolina", "fr": "de la Caroline"},
                "abbrev": "CAR",
                "teamLogo": {
                    "light": "https://assets.nhle.com/logos/nhl/svg/CAR_light.svg",
                    "dark": "https://assets.nhle.com/logos/nhl/svg/CAR_dark.svg",
                },
                "slug": "carolina-hurricanes-12",
                "wins": 47,
                "losses": 30,
                "otLosses": 5,
            },
            "zoneTime": 0.3545412,
        },
    },
}


def test_landing_result_from_dict() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    assert isinstance(result, TeamEdgeLandingResult)
    assert isinstance(result.leaders, TeamEdgeLandingLeaders)
    assert len(result.seasons_with_edge) == 2


def test_landing_seasons() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    assert result.seasons_with_edge[0].id == 20242025
    assert result.seasons_with_edge[0].game_types == [2, 3]
    assert result.seasons_with_edge[1].id == 20232024


def test_shot_attempt_leader() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    leader = result.leaders.shot_attempts_over_90
    assert isinstance(leader, TeamShotAttemptLeader)
    assert leader.attempts == 136
    assert isinstance(leader.team, TeamEdgeLeaderTeam)
    assert leader.team.id == 22
    assert leader.team.abbrev == "EDM"


def test_bursts_leader() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    leader = result.leaders.bursts_over_22
    assert isinstance(leader, TeamBurstsLeader)
    assert leader.bursts == 212
    assert leader.team.id == 21
    assert leader.team.abbrev == "COL"


def test_distance_leader() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    leader = result.leaders.distance_per_60
    assert isinstance(leader, TeamDistanceLeader)
    assert leader.team.id == 13
    assert leader.distance_skated.imperial == 9.3410
    assert leader.distance_skated.metric == 15.0322


def test_high_danger_sog_leader() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    leader = result.leaders.high_danger_sog
    assert isinstance(leader, TeamHighDangerSOGLeader)
    assert leader.team.id == 22
    assert leader.sog == 714
    assert len(leader.shot_location_details) == 2
    assert isinstance(leader.shot_location_details[0], LandingSogAreaDetail)
    assert leader.shot_location_details[0].area == "Behind the Net"
    assert leader.shot_location_details[0].sog == 20
    assert leader.shot_location_details[0].rank == 5


def test_zone_time_leaders() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    assert isinstance(result.leaders.offensive_zone_time, TeamZoneTimeLeader)
    assert result.leaders.offensive_zone_time.team.id == 12
    assert result.leaders.offensive_zone_time.zone_time == 0.4605141
    assert result.leaders.neutral_zone_time.team.id == 25
    assert result.leaders.neutral_zone_time.zone_time == 0.1873355
    assert result.leaders.defensive_zone_time.team.id == 12
    assert result.leaders.defensive_zone_time.zone_time == 0.3545412


def test_team_leader_team_fields() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    team = result.leaders.shot_attempts_over_90.team
    assert team.common_name.default == "Oilers"
    assert team.place_name_with_preposition.default == "Edmonton"
    assert team.logo_light == "https://assets.nhle.com/logos/nhl/svg/EDM_light.svg"
    assert team.logo_dark == "https://assets.nhle.com/logos/nhl/svg/EDM_dark.svg"
    assert team.slug == "edmonton-oilers-22"
    assert team.wins == 48
    assert team.losses == 29
    assert team.ot_losses == 5


def test_team_leader_team_localized_fr() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    team = result.leaders.distance_per_60.team
    assert team.place_name_with_preposition.get_locale("fr") == "de la Floride"


def test_landing_empty_response() -> None:
    result = TeamEdgeLandingResult.from_dict({})
    assert result.seasons_with_edge == []
    assert isinstance(result.leaders, TeamEdgeLandingLeaders)


def test_landing_to_dict() -> None:
    result = TeamEdgeLandingResult.from_dict(LANDING_RESPONSE)
    d = result.to_dict()
    assert isinstance(d, dict)
    assert "seasons_with_edge" in d
    assert "leaders" in d
    assert d["leaders"]["shot_attempts_over_90"]["attempts"] == 136
    assert d["leaders"]["high_danger_sog"]["sog"] == 714
