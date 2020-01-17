from pkg.db import db
from pkg.db.models.workout import Workout, WorkoutExercise
from pkg.db.services.exercise_service import ExerciseService
from sqlalchemy import desc


class WorkoutService:
    @staticmethod
    async def view(workout_id: str):
        workouts = Workout.__table__
        query = workouts.select() \
            .where(workouts.c.id == workout_id)
        workout = await db.fetch_one(query)
        if workout:
            workout_dict = dict(workout)

            workout_exercises = WorkoutExercise.__table__
            query = workout_exercises.select()\
                .where(workout_exercises.c.workout_id == workout_id)
            exercises_list = await db.fetch_all(query)

            exercises_array = []
            for ex in exercises_list:
                exercise = await ExerciseService.view(ex['exercise_id'])
                exercise_dict = dict(ex)
                exercise_dict['exercise'] = exercise
                exercises_array.append(exercise_dict)

            workout_dict['exercises'] = exercises_array
            return workout_dict

    @staticmethod
    async def list(user_id: str):
        workouts = Workout.__table__
        query = workouts.select() \
            .where(workouts.c.user_id == user_id) \
            .order_by(desc(workouts.c.date))
        return await db.fetch_all(query)
