CREATE TABLE data_table (
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
  PRIMARY KEY (id));

 
CREATE TABLE data_3_indexes AS 
TABLE data_table ;
 
CREATE TABLE data_job_nlp_year_index AS 
TABLE data_table ;

CREATE TABLE data_1_index AS 
TABLE data_table ;

ALTER TABLE data_3_indexes ADD PRIMARY KEY (id);
ALTER TABLE data_job_nlp_year_index ADD PRIMARY KEY (id);
ALTER TABLE data_1_index ADD PRIMARY KEY (id);


create index job_nlp_year_sequence on data_3_indexes (job, nlp, year, sequence);
create index job_nlp_year_scan_id on data_3_indexes (job, nlp, year, scan_id);
create index job_nlp_year_issue_flag on data_3_indexes (job, nlp, year, issue_flag);

create index job_nlp_year on data_job_nlp_year_index (job, nlp, year);

create index job_nlp_year_scan_id_sequence_issue_flag on data_1_index (job, nlp, year, scan_id, sequence, issue_flag);




