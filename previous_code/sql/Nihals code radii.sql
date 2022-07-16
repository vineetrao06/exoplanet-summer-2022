CREATE temporary table Inside as 
SELECT
pl_hostname,pl_name,st_spstr, ((sqrt((pow(10,((((st_optmag-(5*(LOG10(st_dist/10)))) - 2.0)-4.72)/-2.5))) / 1.1))) as 'inside'
from Type_M
where st_optmag != '' and st_dist != '';

CREATE temporary table Outside as 
SELECT
pl_hostname,pl_name,st_spstr,((sqrt((pow(10,((((st_optmag-(5*(LOG10(st_dist/10)))) - 2.0)-4.72)/-2.5))) / 0.53))) as 'outside'
from Type_M
where st_optmag != ' ' and st_dist != ' ';

Create table if not exists Nihals_table as Select Inside.pl_name as Planet, Inside.inside as inside, Outside.outside as outside from Inside
inner join Outside 
on Inside.pl_name=Outside.pl_name