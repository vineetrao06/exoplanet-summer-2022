SELECT
CONCAT('Inner bound ', pl_name, ': ', ((sqrt((pow(10,((((st_optmag-(5*(LOG10(st_dist/10)))) - 2.0)-4.72)/-2.5))) / 1.1))))
from Type_M
where st_optmag != ' ' and st_dist != ' '
union
SELECT
CONCAT('outer bound ', pl_name, ': ', ((sqrt((pow(10,((((st_optmag-(5*(LOG10(st_dist/10)))) - 2.0)-4.72)/-2.5))) / 0.53))))
from Type_M
where st_optmag != ' ' and st_dist != ' '