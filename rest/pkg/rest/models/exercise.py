from datetime import datetime
from pkg.rest.models import NamedEntity


class ExerciseCategory(NamedEntity):
    pass


class Exercise(NamedEntity):
    both_hands: bool


class ExerciseForListing(Exercise):
    last_workout_date: datetime
    category: ExerciseCategory
