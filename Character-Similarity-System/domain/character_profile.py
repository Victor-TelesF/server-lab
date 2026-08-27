class CharacterProfile:
    """Represents a character profile with numerical attributes.

    This class is immutable and stores five main attributes: strength,
    agility, magic, defense, and intelligence. All values must be
    integers between 1 and 100.
    """

    def __init__(self, strength: int, agility: int, magic: int, defense: int, intelligence: int):
        """Initializes a new character profile.

        Args:
            strength: Character's strength level (1-100).
            agility: Character's agility level (1-100).
            magic: Character's magic level (1-100).
            defense: Character's defense level (1-100).
            intelligence: Character's intelligence level (1-100).

        Raises:
            ValueError: If any attribute is not an integer between 1 and 100.
        """
        value = [strength, agility, magic, defense, intelligence]
        if not all(isinstance(value, int) and 1 <= value <= 100 for value in [strength, agility, magic, defense, intelligence]):
            raise ValueError("todos os valores devem ser inteiros entre 1 e 100")
        self._status = value

    @property
    def status(self) -> list[int]:
        return self._status

    def __repr__(self):
        return f"{self.status}"
