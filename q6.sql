\set j1 random(0,9600)
\set j2 (:j1 + 400)
\set n1 random(0,4800)
\set n2 (:n1 + 200)
\set y1 random(0,160)
\set y2 (:y1 + 40)
\set s1 random(0,4800)
\set s2 (:s1 + 200)

select * from test_6_col_ind
where
job between :j1 and :j2
and nlp between :n1 and :n2
and year between :y1 and :y2
and sequence between :s1 and :s2;


--  pgbench -n -f q4.sql -T 60