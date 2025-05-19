from dataclasses import dataclass
from typing import List, Dict


@dataclass
class UserProfile:
    id: int
    name: str
    age: int
    interests: List[str]


def segment_audience(users: List[UserProfile]) -> List[List[UserProfile]]:
    """Segment users into age-based groups as a simple demo."""
    segments: Dict[str, List[UserProfile]] = {"young": [], "adult": [], "senior": []}
    for user in users:
        if user.age < 30:
            segments["young"].append(user)
        elif user.age < 60:
            segments["adult"].append(user)
        else:
            segments["senior"].append(user)
    return list(segments.values())
