from datetime import datetime
from pkg.models import NamedEntity


class ExerciseCategory(NamedEntity):
    pass


class Exercise(NamedEntity):
    pass


class ExerciseForListing(Exercise):
    last_workout_date: datetime
    category: ExerciseCategory
