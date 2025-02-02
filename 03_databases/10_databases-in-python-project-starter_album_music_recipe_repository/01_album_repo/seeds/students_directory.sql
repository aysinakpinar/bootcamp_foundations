CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  start_date timestamp
);

-- Then the table with the foreign key second.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
-- The foreign key name is always {other_table_singular}_id
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);

INSERT INTO cohorts (name, start_date) VALUES ('Onsite', '2024-11-18 09:00');
INSERT INTO cohorts (name, start_date) VALUES ('Remote', '2024-11-25 09:00');

INSERT INTO students (name, cohort_id) VALUES ('Aysin', 1);
INSERT INTO students (name, cohort_id) VALUES ('Jess', 2);
INSERT INTO students (name, cohort_id) VALUES ('Michal', 1);
INSERT INTO students (name, cohort_id) VALUES ('Shahida', 2);
INSERT INTO students (name, cohort_id) VALUES ('Milly', 1);


