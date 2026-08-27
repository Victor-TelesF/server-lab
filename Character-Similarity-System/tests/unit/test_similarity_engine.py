from domain.character_profile import CharacterProfile
from domain.similarity_engine import SimilarityEngine
import numpy as np

import pytest

@pytest.fixture
def engine():
    return SimilarityEngine([])


def test_proportional_vectors_have_similarity_one(engine):
    status1 = CharacterProfile(10,20,30,40,50)
    status2 = CharacterProfile(20,40,60,80,100)
    result = engine.similarity(status1,status2)
    assert result == pytest.approx(1.0)

def test_orthogonal_vectors_have_similarity_zero():
    vector_a = np.array([1, 0, 0])
    vector_b = np.array([0, 1, 0])

    result = SimilarityEngine._cosine_similarity(vector_a, vector_b)

    assert result == pytest.approx(0.0)

def test_similarity_is_symmetric(engine):
    profile_a = CharacterProfile(80, 30, 50, 20, 90)
    profile_b = CharacterProfile(40, 70, 10, 60, 25)

    result_ab = engine.similarity(profile_a, profile_b)
    result_ba = engine.similarity(profile_b, profile_a)

    assert result_ab == pytest.approx(result_ba)

