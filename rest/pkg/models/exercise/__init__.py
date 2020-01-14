from pydantic import BaseModel


class Exercise(BaseModel):
    name: str


class ExerciseOut(Exercise):
    pass
