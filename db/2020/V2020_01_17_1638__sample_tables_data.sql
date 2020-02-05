INSERT INTO public.users (id, email, name, picture, locale, is_active) VALUES ('TWRvTJ4GkUTP6dGr', 'twister.kz@gmail.com', 'Павлов Максим', 'https://lh3.googleusercontent.com/a-/AAuE7mAYAn0X0xHHDd6lkAm6F8NEUjy0woDi9i0qVGex=s96-c', 'ru', true);


INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('9SbV89xpAYmneGQw', 'TWRvTJ4GkUTP6dGr', 'Боковое движение');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('zg8nYLJaNhdmSOeG', 'TWRvTJ4GkUTP6dGr', 'Бицепс');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('YtmJgP5R4q4o7wBA', 'TWRvTJ4GkUTP6dGr', 'Пронация');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('awJ7Gvm17LrOVglL', 'TWRvTJ4GkUTP6dGr', 'Супинация');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('pbEEFmoGKLb3S00o', 'TWRvTJ4GkUTP6dGr', 'Кисть');
INSERT INTO public.exercise_categories (id, user_id, name) VALUES ('bmhXQrL3gUV5h3fr', 'TWRvTJ4GkUTP6dGr', 'Пальцы');


INSERT INTO public.workouts (id, user_id, date, comment) VALUES ('5WaAWF4KnsoX2eX8', 'TWRvTJ4GkUTP6dGr', '2020-01-17 12:48:47.939000', 'Some workout');
INSERT INTO public.workouts (id, user_id, date, comment) VALUES ('rFvW35XX90LzDCQp', 'TWRvTJ4GkUTP6dGr', '2020-01-15 12:49:06.739000', null);


INSERT INTO public.exercises (id, user_id, category_id, name, both_hands, last_workout_id) VALUES ('mqwaAIQblczmUExp', 'TWRvTJ4GkUTP6dGr', '9SbV89xpAYmneGQw', 'Лопата с круглой ручкой', false, '5WaAWF4KnsoX2eX8');
INSERT INTO public.exercises (id, user_id, category_id, name, both_hands, last_workout_id) VALUES ('3j7VPlHrsw5vf9YR', 'TWRvTJ4GkUTP6dGr', 'zg8nYLJaNhdmSOeG', 'Строгий бицепс', true, '5WaAWF4KnsoX2eX8');


INSERT INTO public.workout_exercises (id, workout_id, exercise_id, approaches, lh_weight, lh_value, rh_weight, rh_value, bh_weight, bh_value) VALUES ('Qd1xcWBSeM1OAUaF', '5WaAWF4KnsoX2eX8', 'mqwaAIQblczmUExp', null, 49.5, 5, 49.5, 5, null, null);
INSERT INTO public.workout_exercises (id, workout_id, exercise_id, approaches, lh_weight, lh_value, rh_weight, rh_value, bh_weight, bh_value) VALUES ('aYSRbvqpl2brAxVG', '5WaAWF4KnsoX2eX8', '3j7VPlHrsw5vf9YR', null, null, null, null, null, 47, 4);
INSERT INTO public.workout_exercises (id, workout_id, exercise_id, approaches, lh_weight, lh_value, rh_weight, rh_value, bh_weight, bh_value) VALUES ('3gaqFtb93q4SbStk', 'rFvW35XX90LzDCQp', 'mqwaAIQblczmUExp', null, 54, 4, 54, 4, null, null);
INSERT INTO public.workout_exercises (id, workout_id, exercise_id, approaches, lh_weight, lh_value, rh_weight, rh_value, bh_weight, bh_value) VALUES ('tEaQz3TTtbKxnEoA', 'rFvW35XX90LzDCQp', '3j7VPlHrsw5vf9YR', null, null, null, null, null, 52, 3);
