"""
MEDIA DATA CLASS
"""

class Media:
    def __init__(self, data: dict):
        self.slug: str | None = data.get("playerSlug")
        self.headshot: str | None = data.get("headshot")
        self.hero_image: str | None = data.get("heroImage")