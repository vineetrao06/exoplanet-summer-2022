/* Structured Query Language Data Definition Language for
/* creating individual relations [tables] based on unique
/* stellar types:
/* create table <-> DDL to create table
/* "Type_(A/B/F/G/K/M)" name of new table
/* AS select <-> start of data selection query
/* "*" <-> selection criteria w/ "*" representing all fields
/* from data <-> specification of the source table
/* where st_spstr <-> specification of the desired fields
/* like "[A/B/F/G/K/M]%" specification of logical test value
/* A/B/F/G/K/M are the different stellar_object_types in the
/* source Exoplanet data
create table Type_A AS select * from data where st_spstr like "A%";
create table Type_B AS select * from data where st_spstr like "B%";
create table Type_F AS select * from data where st_spstr like "F%";
create table Type_G AS select * from data where st_spstr like "G%";
create table Type_K AS select * from data where st_spstr like "K%";
create table Type_M AS select * from data where st_spstr like "M%";