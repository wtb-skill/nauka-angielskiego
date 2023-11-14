class Word:
    """Class for storing translations, nr of stars and managing stars."""
    def __init__(self, eng, pol, stars):
        self.eng = eng
        self.pol = pol
        self.stars = stars

    def __str__(self):
        return f"English: {self.eng:<15} Polish: {self.pol:<15}"

    def add_star(self):
        """Add a star to a word's status."""
        self.stars += 1

    def remove_star(self):
        """Remove a star from a word's status, with a minimum value of 0."""
        self.stars -= 1
        self.stars = max(self.stars, 0)

    def to_dict(self):
        """Return a dictionary representation of the Word object."""
        return {
            "ENG": self.eng,
            "PL": self.pol,
            "stars": self.stars
        }
