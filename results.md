## ~7m rows high cardinality Data
32Gi ram Intel i7 11 gen

all explain plans done with ANALYZE and soft pars(after run)

## 1 query
```sql
select * from test_6_col_ind 
where 
job between  4800 and 5200
and nlp between  2400 and 2600 
and year between  80 and 120
and sequence between 2400 and 2600 
```
explain results 
```
Node Type	Entity	        Cost	        Rows	Time	
Index Scan	test_6_col_ind	0.43 - 13696.43	105	    10.840	

```

```sql 
select * from test_4_col_ind 
where 
job between  4800 and 5200
and nlp between  2400 and 2600 
and year between  80 and 120
and sequence between 2400 and 2600 
```
explain results 
```
Node Type	Entity	        Cost	        Rows	Time	
Index Scan	test_4_col_ind	0.43 - 13306.26	105	    7.223

```
## 2 query

```sql
select job, nlp, year, sequence, count(*), max(issue_date), min(stamp)  
from test_6_col_ind 
group by job, nlp, year, sequence
```
explain plan 
```
Node Type		Entity			Cost					Rows	Time		Condition
Aggregate		[NULL]			513726.22 - 724617.26	7569241	33812.413	[NULL]
Gather Merge	[NULL]			513726.22 - 690523.10	7569242	31984.135	[NULL]
Sort			[NULL]			512726.20 - 514620.32	2523081	29081.066	[NULL]
Aggregate		[NULL]			376036.42 - 420607.44	2523081	17863.996	[NULL]
Seq Scan		test_6_col_ind	0.00 - 109675.68		2523081	3991.357	[NULL]
```

```sql
select job, nlp, year, sequence, count(*), max(issue_date), min(stamp)  
from test_4_col_ind 
group by job, nlp, year, sequence
```

```
Node Type	Entity			Cost				Rows	Time		Condition
Aggregate	[NULL]			0.43 - 682128.53	7569241	887108.345	[NULL]
Index Scan	test_4_col_ind	0.43 - 542097.54	7569243	878234.374	[NULL]
```

```sql
select * from test_6_col_ind 
where 
job between  4800 and 5200
and nlp between  2400 and 2600 
and year between  80 and 120