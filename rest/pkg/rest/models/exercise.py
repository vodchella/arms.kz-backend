from datetime import datetime
from pkg.rest.models import NamedEntity
from typing import Optional


class ExerciseCategoryDTO(NamedEntity):
    pass


class ExerciseDTO(NamedEntity):
    category_id: str
    both_hands: bool


class ExerciseForListingDTO(ExerciseDTO):
    last_workout_date: Optional[datetime]
