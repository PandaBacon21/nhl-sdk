"""
Teams Space
"""

from resources.api_web import teams


class Teams: 
    def __init__(self, team_code: str): 
        self.code = team_code