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
CREATE ALGORITHM=UNDEFINED DEFINER=`radii`@`localhost` SQL SECURITY DEFINER VIEW `Stats_orbsmax`  AS
SELECT AVG(pl_orbsmax) AS 'Average' FROM `data` UNION
select STDDEV_POP(pl_orbsmax) AS 'StD' from data UNION
select MAX(pl_orbsmax) AS 'Max' from data UNION
select min(pl_orbsmax) AS 'Min' from data where pl_orbsmax <> ""
