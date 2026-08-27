from .character_profile import CharacterProfile
import numpy as np


class SimilarityEngine:
    """Calculates similarity between character profiles using cosine similarity.

    This engine takes a list of character profiles and provides methods
    to calculate similarity between them and find the most similar
    profiles to a given profile.
    """

    def __init__(self, character_profiles: list[CharacterProfile]):
        """Initializes the similarity engine with a list of profiles.

        Args:
            character_profiles: List of character profiles for analysis.
        """
        self._profiles = character_profiles

    @property
    def profiles(self) -> list[CharacterProfile]:
        return self._profiles.copy()

    @staticmethod
    def _cosine_similarity(vector_a: np.ndarray, vector_b: np.ndarray) -> float:
        """Calculates the cosine similarity between two vectors.

        This is a pure formula that returns the cosine of the angle between
        two vectors, ranging from -1 (opposite) to 1 (identical), with 0
        indicating orthogonality.

        Args:
            vector_a: First numpy vector.
            vector_b: Second numpy vector.

        Returns:
            float: Cosine similarity value between -1 and 1.
        """
        return np.dot(vector_a, vector_b) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))
    
    def similarity(self, profile1: CharacterProfile, profile2: CharacterProfile) -> float:
        """Calculates the cosine similarity between two character profiles.

        Args:
            profile1: First character profile.
            profile2: Second character profile.

        Returns:
            float: Cosine similarity value between -1 and 1.
        """
        status1 = np.array(profile1.status)
        status2 = np.array(profile2.status)
        return self._cosine_similarity(status1, status2)

    def most_similar(self, profile: CharacterProfile) -> CharacterProfile:
        """Returns the most similar profile to the given profile.

        Args:
            profile: Reference character profile.

        Returns:
            CharacterProfile: The most similar profile in the profiles list.
        """
        return self.list_most_similar(profile, quantity=1)[0]

    def list_most_similar(self, profile: CharacterProfile, quantity: int) -> list[CharacterProfile]:
        """Returns a list of the most similar profiles to the given profile.

        Args:
            profile: Reference character profile.
            quantity: Number of similar profiles to return.

        Returns:
            list[CharacterProfile]: List of profiles sorted by similarity
                in descending order.
        """
        others = [other for other in self._profiles if other != profile]
        similarities = sorted(others, key=lambda other: self.similarity(other, profile), reverse=True)
        return similarities[: quantity]