from pkg.db import db
from pkg.db.models.exercise import Exercise
from pkg.db.models.workout import Workout, WorkoutExercise
from sqlalchemy import desc
from sqlalchemy.sql import Select
from sqlalchemy.sql.expression import false


class WorkoutService:
    @staticmethod
    async def get(workout_id: str):
        workouts = Workout.__table__
        query = workouts.select() \
            .where(workouts.c.is_deleted == false()) \
            .where(workouts.c.id == workout_id)
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def get_exercises(workout_id):
        w = WorkoutExercise.__table__
        e = Exercise.__table__
        query = Select(columns=[*w.c, e.c.name.label('exercise_name')]) \
            .select_from(w.join(e)) \
            .where(w.c.workout_id == workout_id)
        return await db.fetch_all(query)

    @staticmethod
    async def list(user_id: str):
        workouts = Workout.__table__
        query = workouts.select() \
            .where(workouts.c.is_deleted == false()) \
            .where(workouts.c.user_id == user_id) \
            .order_by(desc(workouts.c.date))
        return await db.fetch_all(query)

    @staticmethod
    async def view_exercise_history(exercise_id: str):
        we = WorkoutExercise.__table__
        workouts = Workout.__table__
        query = Select(columns=[*we.c, workouts.c.date.label('workout_date')]) \
            .select_from(we.join(workouts)) \
            .where(workouts.c.is_deleted == false()) \
            .where(we.c.exercise_id == exercise_id) \
            .order_by(desc(workouts.c.date))
        return await db.fetch_all(query)
