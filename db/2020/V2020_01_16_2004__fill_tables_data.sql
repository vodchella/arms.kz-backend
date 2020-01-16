INSERT INTO public.users (id, email) VALUES ('TWRvTJ4GkUTP6dGr', 'twister.kz@gmail.com');

INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('9SbV89xpAYmneGQw', 'TWRvTJ4GkUTP6dGr', 'Боковое движение');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('zg8nYLJaNhdmSOeG', 'TWRvTJ4GkUTP6dGr', 'Бицепс');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('YtmJgP5R4q4o7wBA', 'TWRvTJ4GkUTP6dGr', 'Пронация');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('awJ7Gvm17LrOVglL', 'TWRvTJ4GkUTP6dGr', 'Супинация');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('pbEEFmoGKLb3S00o', 'TWRvTJ4GkUTP6dGr', 'Кисть');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('bmhXQrL3gUV5h3fr', 'TWRvTJ4GkUTP6dGr', 'Пальцы');

INSERT INTO public.exercises (id, user_id, category_id, name, both_hands, last_workout_date) VALUES ('mqwaAIQblczmUExp', 'TWRvTJ4GkUTP6dGr', '9SbV89xpAYmneGQw', 'Лопата с круглой ручкой', false, '2020-01-16 00:00:00.000000');
INSERT INTO public.exercises (id, user_id, category_id, name, both_hands, last_workout_date) VALUES ('3j7VPlHrsw5vf9YR', 'TWRvTJ4GkUTP6dGr', 'zg8nYLJaNhdmSOeG', 'Строгий бицепс', true, '2020-01-16 00:00:00.000000');
