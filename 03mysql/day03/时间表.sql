create table t520
(
  id int,
  username varchar(20),
  password varchar(20),
  money int,
  birthday date,
  cztime timestamp
);

insert into t520 values(
1,
'�û�1',
'123456',
300,
'1990-05-20',
'2018-08-30 08:30:00');

insert into t520 value(
2,
'�û�2',
'123456',
400,
'1991-01-01',
now());

insert into t520 value(
3,
'�û�3',
'123456',
500,
19840201,
now());

insert into t520 value(
4,
'�û�4',
'123456',
600,
19950520,
now());

insert into t520 value(
5,
'�û�5',
'123456',
800,
19850228,
20181104000000);