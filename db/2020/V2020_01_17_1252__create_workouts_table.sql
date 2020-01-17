create table workouts
(
	id char(16) not null
		constraint workouts_pk
			primary key,
	user_id char(16) not null
		constraint workouts_users_id_fk
			references users
				on delete cascade,
	date timestamp with time zone not null,
	comment text
);

alter table workouts owner to postgres;


