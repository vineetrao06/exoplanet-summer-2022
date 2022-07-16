create table Type_A AS select * from data where st_spstr like "A%";

create table Type_B AS select * from data where st_spstr like "B%";

create table Type_F AS select * from data where st_spstr like "F%";

create table Type_G AS select * from data where st_spstr like "G%";

create table Type_K AS select * from data where st_spstr like "K%";

create table Type_M AS select * from data where st_spstr like "M%";
