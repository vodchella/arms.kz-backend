create table workout_exercises
(
	id char(16) not null
		constraint workout_exercise_pk
			primary key,
	workout_id char(16) not null
		constraint workout_exercise_workouts_id_fk
			references workouts
				on delete cascade,
	exercise_id char(16) not null
		constraint workout_exercise_exercises_id_fk
			references exercises,
	approaches smallint,
	lh_weight numeric,
	lh_value integer,
	rh_weight numeric,
	rh_value integer,
	bh_weight numeric,
	bh_value integer
);

alter table workout_exercises owner to postgres;


