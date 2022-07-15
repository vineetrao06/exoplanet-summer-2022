CREATE TABLE IF NOT EXIST HZ_stats AS
SELECT 
MAX(inside) as Max_In,
AVG(inside) as Avg_In,
MIN(inside) as Min_In,
STDDEV_SAMP(inside) as StdD_In,
MAX(outside) as Max_Out,
AVG(outside) as Avg_Out,
MIN(outside) as Min_Out,
STDDEV_SAMP(outside) as StdD_Out 
from `HZ_table`
===============================================================================================
Development/Exoplanets/HZ_table/		http://192.168.22.2/phpmyadmin/db_sql.php?db=Exoplanets
 Showing rows 0 -  0 (1 total, Query took 0.0092 seconds.)

SELECT 
MAX(inside) as Max_In,
AVG(inside) as Avg_In,
MIN(inside) as Min_In,
STDDEV_SAMP(inside) as StdD_In,
MAX(outside) as Max_Out,
AVG(outside) as Avg_Out,
MIN(outside) as Min_Out,
STDDEV_SAMP(outside) as StdD_Out 
from `HZ_table`



66.87646358641625	2.7321757394762796	0.004426791095972276	3.3767023038385826	96.3455604523769	3.9361082921809274	0.006377455479474105	4.864645325089236	
