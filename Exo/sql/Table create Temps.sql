create table Temps as 
select 
rowid,pl_hostname,pl_pnum,pl_name,pl_letter,
st_dist,gaia_dist,
st_sp,st_spstr,st_lum,
st_optmag,gaia_gmag,
st_teff,st_mass,st_rad,
st_metfe,st_metratio,st_age from data
where (st_dist <> 0 and gaia_dist <> 0)
group by st_optmag
order by st_teff asc

create temporary table Sums 
select @ax := avg(st_dist), 
       @ay := avg(gaia_dist), 
       @div := (stddev_samp(st_dist) * stddev_samp(gaia_dist))
from Temps;

select sum( ( st_dist - @ax ) * (gaia_dist - @ay) ) / ((count(st_dist) -1) * @div) from Temps,Sums;
+-----------------------------------------------------------------------------+
| sum( ( st_dist - @ax ) * (gaia_dist - @ay) ) / ((count(st_dist) -1) * @div) |
+-----------------------------------------------------------------------------+
|                                                           0.700885077729073 |
+-----------------------------------------------------------------------------+

create temporary table tempor 
select @ax := avg(st_lum), 
       @ay := avg(st_teff), 
       @div := (stddev_samp(st_lum) * stddev_samp(st_teff))
from Temps;

select sum( ( st_lum - @ax ) * (st_teff - @ay) ) / ((count(st_lum) -1) * @div) from Temps,tempor;
+-------------------------------------------------------------------------+
| sum( ( st_lum - @ax ) * (st_teff - @ay) ) / ((count(st_lum) -1) * @div) |
+-------------------------------------------------------------------------+
|                                                     0.19264265669639571 |
+-------------------------------------------------------------------------+

create temporary table tempor 
select @ax := avg(st_optmag), 
       @ay := avg(st_teff), 
       @div := (stddev_samp(st_optmag) * stddev_samp(st_teff))
from Temps;

select sum( ( st_optmag - @ax ) * (st_teff - @ay) ) / ((count(st_optmag) -1) * @div) from Temps,tempor;
+-------------------------------------------------------------------------------+
| sum( ( st_optmag - @ax ) * (st_teff - @ay) ) / ((count(st_optmag) -1) * @div) |
+-------------------------------------------------------------------------------+
|                                                         -0.004397116938309072 |
+-------------------------------------------------------------------------------+