create table users
(
	id char(16) not null
		constraint users_pk
			primary key,
	email text not null,
	name text,
	picture text,
	locale varchar(10),
	token_key char(16),
	is_active boolean default true not null
);

alter table users owner to postgres;

create unique index users_email_uindex
	on users (email);


