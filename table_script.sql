DROP TABLE test;
CREATE TABLE test (
  id BIGSERIAL ,
  job integer NOT NULL,
  nlp smallint not null,
  year smallint not null,
  scan_id smallint NOT NULL,
  issue_flag smallint NOT NULL DEFAULT 0,
  sequence smallint NOT NULL,
  issue_date date ,
  stamp timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  img_name varchar(255) DEFAULT null,
  PRIMARY KEY (id, job));


Create index job_nlp_year_sequence on test (job,nlp,year,sequence);
Create index job_nlp_year_scan_id_issue_flag_sequence on test (job, nlp, year, scan_id, issue_flag, sequence);

drop index job_nlp_year_sequence on test

ALTER TABLE test
RENAME TO test_6_col_ind;

create table test_4_col_ind as 
select * from test_6_col_ind;

alter table test_4_col_ind 
add CONSTRAINT test_4_col_ind_pkey PRIMARY KEY (id, job);

Create index job_nlp_year_sequence on test_4_col_ind (job,nlp,year,sequence);




