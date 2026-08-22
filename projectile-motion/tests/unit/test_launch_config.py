import pytest

from domain.launch_config import LaunchConfig


def test_negative_v0_raises_error():
    with pytest.raises(ValueError):
        LaunchConfig(v0=-5, angle_deg=20, gravity=9)


def test_zero_v0_raises_error():
    with pytest.raises(ValueError):
        LaunchConfig(v0=0, angle_deg=20, gravity=9)


def test_negative_gravity_raises_error():
    with pytest.raises(ValueError):
        LaunchConfig(v0=5, angle_deg=20, gravity=-9)


def test_zero_gravity_raises_error():
    with pytest.raises(ValueError):
        LaunchConfig(v0=5, angle_deg=20, gravity=0)


def test_negative_angle_raises_error():
    with pytest.raises(ValueError):
        LaunchConfig(v0=5, angle_deg=-10, gravity=9)


def test_angle_above_90_raises_error():
    with pytest.raises(ValueError):
        LaunchConfig(v0=5, angle_deg=92, gravity=9)


def test_valid_config_does_not_raise_error():
    LaunchConfig(v0=50, angle_deg=45, gravity=9)