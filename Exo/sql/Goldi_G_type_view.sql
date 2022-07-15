-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 04, 2019 at 02:50 PM
-- Server version: 5.5.60-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Exoplanets`
--

-- --------------------------------------------------------

--
-- Structure for view `Goldi_G_type`
--

CREATE ALGORITHM=UNDEFINED DEFINER=`radii`@`localhost` SQL SECURITY DEFINER VIEW `Goldi_G_type`  AS  select 
`data`.`rowid` AS `Row`,
`data`.`pl_hostname` AS `Star`,
`data`.`pl_letter` AS `Pl_letter`,
`data`.`pl_name` AS `Name`,
`data`.`st_sp` AS `Type`,
`data`.`st_spstr` AS `Sp_str`,
`data`.`pl_orbsmax` AS `Semi_maj` 
from `data` where ((`data`.`st_spstr` like '%G%') and 
(`data`.`pl_orbsmax` between 0.95 and 2.4)) 
order by st_sp` ASC ;

--
-- VIEW  `Goldi_G_type`
-- Data: None
--

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
