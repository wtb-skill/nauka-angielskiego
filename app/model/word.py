class Word:
    """Class for storing translations, nr of stars and managing stars."""

    def __init__(self, eng: str, pol: str, stars: int) -> None:
        self.eng = eng
        self.pol = pol
        self.stars = stars

    def __str__(self) -> str:
        stars_str = "*" * self.stars
        return f"English: {self.eng:<15} Polish: {self.pol:<15} {stars_str:15}"

    def add_star(self) -> None:
        """Add a star to a word's status."""
        self.stars += 1

    def remove_star(self) -> None:
        """Remove a star from a word's status, with a minimum value of 0."""
        self.stars -= 1
        self.stars = max(self.stars, 0)

    def to_dict(self) -> dict:
        """Return a dictionary representation of the Word object."""
        return {"ENG": self.eng, "PL": self.pol, "stars": self.stars}
