create table exercises
(
	id char(16) not null
		constraint exercises_pk
			primary key,
	user_id char(16) not null
		constraint exercises_users_id_fk
			references users
				on delete cascade,
	category_id char(16) not null
		constraint exercises_exercise_categories_id_fk
			references exercise_categories,
	name text not null,
	both_hands boolean not null,
	last_workout_date timestamp with time zone
);

alter table exercises owner to postgres;

create unique index exercises_user_id_name_uindex
	on exercises (user_id, name);


