from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ReportContextConfig:
    display_items: list[str]
    result_filters: list[str]
    sort_keys: list[str]

    @classmethod
    def from_dict(cls, data: dict) -> ReportContextConfig:
        return cls(
            display_items = data.get("displayItems") or [],
            result_filters = data.get("resultFilters") or [],
            sort_keys = data.get("sortKeys") or [],
        )


@dataclass(slots=True, frozen=True)
class ReportConfig:
    game: ReportContextConfig | None
    season: ReportContextConfig | None

    @classmethod
    def from_dict(cls, data: dict) -> ReportConfig:
        raw_game = data.get("game")
        raw_season = data.get("season")
        return cls(
            game = ReportContextConfig.from_dict(raw_game) if raw_game else None,
            season = ReportContextConfig.from_dict(raw_season) if raw_season else None,
        )


@dataclass(slots=True, frozen=True)
class StatsConfig:
    player_report_data: dict[str, ReportConfig]
    goalie_report_data: dict[str, ReportConfig]
    team_report_data: dict[str, ReportConfig]
    aggregated_columns: list[str]
    individual_columns: list[str]

    @classmethod
    def from_dict(cls, data: dict) -> StatsConfig:
        return cls(
            player_report_data = {k: ReportConfig.from_dict(v) for k, v in (data.get("playerReportData") or {}).items()},
            goalie_report_data = {k: ReportConfig.from_dict(v) for k, v in (data.get("goalieReportData") or {}).items()},
            team_report_data = {k: ReportConfig.from_dict(v) for k, v in (data.get("teamReportData") or {}).items()},
            aggregated_columns = data.get("aggregatedColumns") or [],
            individual_columns = data.get("individualColumns") or [],
        )
