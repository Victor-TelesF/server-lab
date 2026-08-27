from domain.character_profile import CharacterProfile

import pytest

@pytest.fixture
def profile():
    character = CharacterProfile(90,30,30,70,20)
    return character

def test_creates_profile_with_valid_values():
    CharacterProfile(50,35,65,20,90)

def test_status_returns_correct_values(profile):
    assert profile.status == [90,30,30,70,20]

def test_raises_error_when_value_below_minimum():
    with pytest.raises(ValueError):
        CharacterProfile(0,10,23,65,1)

def test_raises_error_when_value_above_maximum():
    with pytest.raises(ValueError):
        CharacterProfile(101,10,23,65,50)

def test_raises_error_when_value_is_not_int():
    with pytest.raises(ValueError):
        CharacterProfile(10.5,10,23,65,50)

def test_accepts_boundary_value_minimum():
    profile = CharacterProfile(1, 1, 1, 1, 1)
    assert profile.status == [1, 1, 1, 1, 1]

def test_accepts_boundary_value_maximum():
    profile = CharacterProfile(100, 100, 100, 100, 100)
    assert profile.status == [100, 100, 100, 100, 100]