create table exercise_categories
(
	id char(16) not null
		constraint exercise_categories_pk
			primary key,
	user_id char(16) not null
		constraint exercise_categories_users_id_fk
			references users
				on delete cascade,
	name text not null,
	is_main boolean default false not null,
	is_deleted boolean default false not null
);

alter table exercise_categories owner to postgres;

create unique index exercise_categories_user_id_name_is_deleted_uindex
	on exercise_categories (user_id, name, is_deleted);


