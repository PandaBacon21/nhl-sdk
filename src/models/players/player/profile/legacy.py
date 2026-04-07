# Moved to models/players/player/achievements/achievements.py
from ..achievements.achievements import Achievements as Legacy
from ..achievements.award import Award
from ..achievements.badge import Badge

__all__ = ["Legacy", "Award", "Badge"]
