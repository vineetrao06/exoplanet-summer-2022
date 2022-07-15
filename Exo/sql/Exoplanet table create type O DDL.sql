create table Type_A AS select rowid,pl_hostname,pl_name,st_sp,st_spstr from data where st_spstr like "A%"

create table Type_B AS select rowid,pl_hostname,pl_name,st_sp,st_spstr from data where st_spstr like "B%"

create table Type_F AS select rowid,pl_hostname,pl_name,st_sp,st_spstr from data where st_spstr like "F%"

create table Type_G AS select rowid,pl_hostname,pl_name,st_sp,st_spstr from data where st_spstr like "G%"

create table Type_K AS select rowid,pl_hostname,pl_name,st_sp,st_spstr from data where st_spstr like "K%"

create table Type_M AS select rowid,pl_hostname,pl_name,st_sp,st_spstr from data where st_spstr like "M%"
