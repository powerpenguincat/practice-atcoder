import pytest
from src.star import satellite

def test_satellite_name():
    target=satellite("lua")
    ans=target.name
    assert ans=="lua"

if __name__ == "__main__":
    pass