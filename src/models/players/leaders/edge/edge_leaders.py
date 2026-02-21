"""
NHL PLAYER EDGE DATA
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod


if TYPE_CHECKING:
    from nhl_stats.src.client import NhlClient

class EdgeLeaders(ABC): 
    def __init__(self, client: NhlClient) -> None: 
        self._client = client

    @abstractmethod
    def landing(self) -> Landing:
        ...

    # @abstractmethod
    # def top_10(self) -> dict: 
    #     ...


class SkaterEdgeLeaders(EdgeLeaders):
    def __init__(self, client: NhlClient) -> None: 
        super().__init__(client=client)

    def landing(self) -> Landing:
        # Add skater landing logic
        data = self._client._api.api_web.call_nhl_edge_skaters.get_skater_landing()
        landing = Landing(data=data.data)
        return landing

    # def top_10(self) -> dict: 
    #     # Add skater top 10 logic
    #     pass
    #     # getSkaterDistanceTop10
    #     # getSkaterSpeedTop10
    #     # getSkaterZoneTimeTop10
    #     # getShotSpeedTop10
    #     # getShotLocationTop10

    
    
# class GoalieEdgeLeaders(EdgeLeaders):
#     def __init__(self, client: NhlClient) -> None: 
#         super().__init__(client=client)

#     def landing(self) -> Landing:
#         # Add goalie landing logic
#         pass

#     def top_10(self) -> dict: 
#         # Add goalie top 10 logic
#         pass
    

class Landing: 
    def __init__(self, data: dict) -> None: 
        self.seasons_with_edge: list = [season for season in data.get("seasonsWithEdgeStats") or []]
        self.leaders: LandingLeaders = LandingLeaders(data.get("leaders") or {})



class LandingLeaders:
    def __init__(self, data: dict) -> None:
        self.hardest_shot: dict  | None = data.get("hardestShot")
        self.max_skating_speed: dict | None = data.get("maxSkatingSpeed")
        self.total_distance_skated: dict | None= data.get("totalDistanceSkated")
        self.high_danger_sog: dict | None = data.get("highDangerSOG")
        self.offensive_zone_time: dict | None = data.get("offensiveZoneTime")
        self.defensive_zone_time: dict | None = data.get("defensiveZoneTime")

