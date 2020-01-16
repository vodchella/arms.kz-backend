create table users
(
	id char(16) not null
		constraint users_pk
			primary key,
	email text not null
);

alter table users owner to postgres;

create unique index users_email_uindex
	on users (email);


