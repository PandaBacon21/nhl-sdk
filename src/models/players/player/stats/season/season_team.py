"""
SEASON STAT TEAM
"""

from ......core.utilities import LocalizedString

class SeasonTeam: 
    """
    Team information for a player in a given season.

    Provides access to the player's team during the season, including
    common and full team names, wrapped in LocalizedString for
    multi-language support.

    Instances of this class are accessed via `Season.team`.
    """
    def __init__(self, data: dict): 
        """
        Parameters
        ----------
        data : dict
            Raw season data containing team fields as returned in Player data
            by the NHL API.
        """
        self.common_name: LocalizedString | None = LocalizedString(data.get("teamCommonName"))
        self.name: LocalizedString | None = LocalizedString(data.get("teamName"))