-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 18, 2019 at 12:41 PM
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
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `rowid` int(4) NOT NULL DEFAULT '0',
  `pl_hostname` varchar(27) DEFAULT NULL,
  `pl_letter` varchar(1) DEFAULT NULL,
  `pl_name` varchar(29) DEFAULT NULL,
  `pl_discmethod` varchar(29) DEFAULT NULL,
  `pl_controvflag` varchar(2) DEFAULT NULL,
  `pl_pnum` int(1) DEFAULT NULL,
  `pl_orbper` varchar(10) DEFAULT NULL,
  `pl_orbpererr1` varchar(9) DEFAULT NULL,
  `pl_orbpererr2` varchar(10) DEFAULT NULL,
  `pl_orbperlim` varchar(2) DEFAULT NULL,
  `pl_orbsmax` varchar(7) DEFAULT NULL,
  `pl_orbsmaxerr1` varchar(7) DEFAULT NULL,
  `pl_orbsmaxerr2` varchar(8) DEFAULT NULL,
  `pl_orbsmaxlim` varchar(2) DEFAULT NULL,
  `pl_orbeccen` varchar(6) DEFAULT NULL,
  `pl_orbeccenerr1` varchar(7) DEFAULT NULL,
  `pl_orbeccenerr2` varchar(8) DEFAULT NULL,
  `pl_orbeccenlim` varchar(2) DEFAULT NULL,
  `pl_orbincl` varchar(5) DEFAULT NULL,
  `pl_orbinclerr1` varchar(5) DEFAULT NULL,
  `pl_orbinclerr2` varchar(6) DEFAULT NULL,
  `pl_orbincllim` varchar(2) DEFAULT NULL,
  `pl_bmassj` varchar(7) DEFAULT NULL,
  `pl_bmassjerr1` varchar(6) DEFAULT NULL,
  `pl_bmassjerr2` varchar(7) DEFAULT NULL,
  `pl_bmassjlim` varchar(2) DEFAULT NULL,
  `pl_bmassprov` varchar(14) DEFAULT NULL,
  `pl_radj` varchar(4) DEFAULT NULL,
  `pl_radjerr1` varchar(4) DEFAULT NULL,
  `pl_radjerr2` varchar(5) DEFAULT NULL,
  `pl_radjlim` varchar(2) DEFAULT NULL,
  `pl_dens` varchar(5) DEFAULT NULL,
  `pl_denserr1` varchar(4) DEFAULT NULL,
  `pl_denserr2` varchar(5) DEFAULT NULL,
  `pl_denslim` varchar(2) DEFAULT NULL,
  `pl_ttvflag` int(1) DEFAULT NULL,
  `pl_kepflag` int(1) DEFAULT NULL,
  `pl_k2flag` int(1) DEFAULT NULL,
  `pl_nnotes` int(1) DEFAULT NULL,
  `ra_str` varchar(12) DEFAULT NULL,
  `ra` decimal(9,6) DEFAULT NULL,
  `dec_str` varchar(12) DEFAULT NULL,
  `dec` decimal(9,6) DEFAULT NULL,
  `st_dist` varchar(6) DEFAULT NULL,
  `st_disterr1` varchar(5) DEFAULT NULL,
  `st_disterr2` varchar(6) DEFAULT NULL,
  `st_distlim` varchar(1) DEFAULT NULL,
  `st_optmag` varchar(5) DEFAULT NULL,
  `st_optmagerr` varchar(4) DEFAULT NULL,
  `st_optmaglim` varchar(1) DEFAULT NULL,
  `st_optband` varchar(11) DEFAULT NULL,
  `gaia_gmag` varchar(5) DEFAULT NULL,
  `gaia_gmagerr` varchar(10) DEFAULT NULL,
  `gaia_gmaglim` varchar(1) DEFAULT NULL,
  `st_teff` varchar(6) DEFAULT NULL,
  `st_tefferr1` varchar(5) DEFAULT NULL,
  `st_tefferr2` varchar(7) DEFAULT NULL,
  `st_tefflim` varchar(1) DEFAULT NULL,
  `st_mass` varchar(4) DEFAULT NULL,
  `st_masserr1` varchar(4) DEFAULT NULL,
  `st_masserr2` varchar(5) DEFAULT NULL,
  `st_masslim` varchar(1) DEFAULT NULL,
  `st_rad` varchar(4) DEFAULT NULL,
  `st_raderr1` varchar(5) DEFAULT NULL,
  `st_raderr2` varchar(5) DEFAULT NULL,
  `st_radlim` varchar(1) DEFAULT NULL,
  `rowupdate` varchar(10) DEFAULT NULL,
  `pl_tranflag` int(1) DEFAULT NULL,
  `pl_rvflag` int(1) DEFAULT NULL,
  `pl_imgflag` int(1) DEFAULT NULL,
  `pl_astflag` varchar(1) DEFAULT NULL,
  `pl_omflag` int(1) DEFAULT NULL,
  `pl_cbflag` int(1) DEFAULT NULL,
  `pl_angsep` varchar(7) DEFAULT NULL,
  `pl_angseperr1` varchar(7) DEFAULT NULL,
  `pl_angseperr2` varchar(8) DEFAULT NULL,
  `pl_orbtper` varchar(10) DEFAULT NULL,
  `pl_orbtpererr1` varchar(6) DEFAULT NULL,
  `pl_orbtpererr2` varchar(7) DEFAULT NULL,
  `pl_orbtperlim` varchar(1) DEFAULT NULL,
  `pl_orblper` varchar(7) DEFAULT NULL,
  `pl_orblpererr1` varchar(7) DEFAULT NULL,
  `pl_orblpererr2` varchar(8) DEFAULT NULL,
  `pl_orblperlim` varchar(1) DEFAULT NULL,
  `pl_rvamp` varchar(6) DEFAULT NULL,
  `pl_rvamperr1` varchar(5) DEFAULT NULL,
  `pl_rvamperr2` varchar(6) DEFAULT NULL,
  `pl_rvamplim` varchar(2) DEFAULT NULL,
  `pl_eqt` varchar(4) DEFAULT NULL,
  `pl_eqterr1` varchar(3) DEFAULT NULL,
  `pl_eqterr2` varchar(4) DEFAULT NULL,
  `pl_eqtlim` varchar(1) DEFAULT NULL,
  `pl_insol` varchar(5) DEFAULT NULL,
  `pl_insolerr1` varchar(4) DEFAULT NULL,
  `pl_insolerr2` varchar(5) DEFAULT NULL,
  `pl_insollim` varchar(1) DEFAULT NULL,
  `pl_massj` varchar(6) DEFAULT NULL,
  `pl_massjerr1` varchar(6) DEFAULT NULL,
  `pl_massjerr2` varchar(7) DEFAULT NULL,
  `pl_massjlim` varchar(2) DEFAULT NULL,
  `pl_msinij` varchar(6) DEFAULT NULL,
  `pl_msinijerr1` varchar(6) DEFAULT NULL,
  `pl_msinijerr2` varchar(7) DEFAULT NULL,
  `pl_msinijlim` varchar(2) DEFAULT NULL,
  `pl_masse` varchar(9) DEFAULT NULL,
  `pl_masseerr1` varchar(8) DEFAULT NULL,
  `pl_masseerr2` varchar(9) DEFAULT NULL,
  `pl_masselim` varchar(2) DEFAULT NULL,
  `pl_msinie` varchar(9) DEFAULT NULL,
  `pl_msinieerr1` varchar(9) DEFAULT NULL,
  `pl_msinieerr2` varchar(10) DEFAULT NULL,
  `pl_msinielim` varchar(2) DEFAULT NULL,
  `pl_bmasse` varchar(9) DEFAULT NULL,
  `pl_bmasseerr1` varchar(9) DEFAULT NULL,
  `pl_bmasseerr2` varchar(10) DEFAULT NULL,
  `pl_bmasselim` varchar(2) DEFAULT NULL,
  `pl_rade` varchar(5) DEFAULT NULL,
  `pl_radeerr1` varchar(5) DEFAULT NULL,
  `pl_radeerr2` varchar(6) DEFAULT NULL,
  `pl_radelim` varchar(2) DEFAULT NULL,
  `pl_rads` varchar(4) DEFAULT NULL,
  `pl_radserr1` varchar(4) DEFAULT NULL,
  `pl_radserr2` varchar(5) DEFAULT NULL,
  `pl_radslim` varchar(2) DEFAULT NULL,
  `pl_trandep` varchar(7) DEFAULT NULL,
  `pl_trandeperr1` varchar(7) DEFAULT NULL,
  `pl_trandeperr2` varchar(8) DEFAULT NULL,
  `pl_trandeplim` varchar(1) DEFAULT NULL,
  `pl_trandur` varchar(8) DEFAULT NULL,
  `pl_trandurerr1` varchar(8) DEFAULT NULL,
  `pl_trandurerr2` varchar(9) DEFAULT NULL,
  `pl_trandurlim` varchar(1) DEFAULT NULL,
  `pl_tranmid` varchar(10) DEFAULT NULL,
  `pl_tranmiderr1` varchar(7) DEFAULT NULL,
  `pl_tranmiderr2` varchar(8) DEFAULT NULL,
  `pl_tranmidlim` varchar(1) DEFAULT NULL,
  `pl_tsystemref` varchar(7) DEFAULT NULL,
  `pl_imppar` varchar(5) DEFAULT NULL,
  `pl_impparerr1` varchar(5) DEFAULT NULL,
  `pl_impparerr2` varchar(6) DEFAULT NULL,
  `pl_impparlim` varchar(1) DEFAULT NULL,
  `pl_occdep` varchar(6) DEFAULT NULL,
  `pl_occdeperr1` varchar(6) DEFAULT NULL,
  `pl_occdeperr2` varchar(7) DEFAULT NULL,
  `pl_occdeplim` varchar(1) DEFAULT NULL,
  `pl_ratdor` varchar(8) DEFAULT NULL,
  `pl_ratdorerr1` varchar(8) DEFAULT NULL,
  `pl_ratdorerr2` varchar(9) DEFAULT NULL,
  `pl_ratdorlim` varchar(1) DEFAULT NULL,
  `pl_ratror` varchar(6) DEFAULT NULL,
  `pl_ratrorerr1` varchar(6) DEFAULT NULL,
  `pl_ratrorerr2` varchar(7) DEFAULT NULL,
  `pl_ratrorlim` varchar(1) DEFAULT NULL,
  `pl_def_reflink` varchar(191) DEFAULT NULL,
  `pl_disc` int(4) DEFAULT NULL,
  `pl_disc_reflink` varchar(191) DEFAULT NULL,
  `pl_locale` varchar(16) DEFAULT NULL,
  `pl_facility` varchar(44) DEFAULT NULL,
  `pl_telescope` varchar(59) DEFAULT NULL,
  `pl_instrument` varchar(35) DEFAULT NULL,
  `pl_status` int(1) DEFAULT NULL,
  `pl_mnum` int(1) DEFAULT NULL,
  `pl_st_npar` int(3) DEFAULT NULL,
  `pl_st_nref` int(2) DEFAULT NULL,
  `pl_pelink` varchar(56) DEFAULT NULL,
  `pl_edelink` varchar(49) DEFAULT NULL,
  `pl_publ_date` varchar(7) DEFAULT NULL,
  `hd_name` varchar(11) DEFAULT NULL,
  `hip_name` varchar(11) DEFAULT NULL,
  `st_rah` decimal(10,8) DEFAULT NULL,
  `st_glon` decimal(9,6) DEFAULT NULL,
  `st_glat` decimal(9,6) DEFAULT NULL,
  `st_elon` decimal(9,6) DEFAULT NULL,
  `st_elat` decimal(9,6) DEFAULT NULL,
  `st_plx` varchar(5) DEFAULT NULL,
  `st_plxerr1` varchar(3) DEFAULT NULL,
  `st_plxerr2` varchar(4) DEFAULT NULL,
  `st_plxlim` varchar(1) DEFAULT NULL,
  `gaia_plx` varchar(5) DEFAULT NULL,
  `gaia_plxerr1` varchar(3) DEFAULT NULL,
  `gaia_plxerr2` varchar(4) DEFAULT NULL,
  `gaia_plxlim` varchar(1) DEFAULT NULL,
  `gaia_dist` varchar(7) DEFAULT NULL,
  `gaia_disterr1` varchar(7) DEFAULT NULL,
  `gaia_disterr2` varchar(8) DEFAULT NULL,
  `gaia_distlim` varchar(1) DEFAULT NULL,
  `st_pmra` varchar(7) DEFAULT NULL,
  `st_pmraerr` varchar(4) DEFAULT NULL,
  `st_pmralim` varchar(1) DEFAULT NULL,
  `st_pmdec` varchar(7) DEFAULT NULL,
  `st_pmdecerr` varchar(4) DEFAULT NULL,
  `st_pmdeclim` varchar(1) DEFAULT NULL,
  `st_pm` varchar(6) DEFAULT NULL,
  `st_pmerr` varchar(4) DEFAULT NULL,
  `st_pmlim` varchar(1) DEFAULT NULL,
  `gaia_pmra` varchar(6) DEFAULT NULL,
  `gaia_pmraerr` varchar(4) DEFAULT NULL,
  `gaia_pmralim` varchar(1) DEFAULT NULL,
  `gaia_pmdec` varchar(6) DEFAULT NULL,
  `gaia_pmdecerr` varchar(4) DEFAULT NULL,
  `gaia_pmdeclim` varchar(1) DEFAULT NULL,
  `gaia_pm` varchar(6) DEFAULT NULL,
  `gaia_pmerr` varchar(4) DEFAULT NULL,
  `gaia_pmlim` varchar(1) DEFAULT NULL,
  `st_radv` varchar(5) DEFAULT NULL,
  `st_radverr1` varchar(4) DEFAULT NULL,
  `st_radverr2` varchar(5) DEFAULT NULL,
  `st_radvlim` varchar(1) DEFAULT NULL,
  `st_sp` varchar(3) DEFAULT NULL,
  `st_spstr` varchar(23) DEFAULT NULL,
  `st_sperr` varchar(10) DEFAULT NULL,
  `st_splim` varchar(1) DEFAULT NULL,
  `st_logg` varchar(3) DEFAULT NULL,
  `st_loggerr1` varchar(3) DEFAULT NULL,
  `st_loggerr2` varchar(4) DEFAULT NULL,
  `st_logglim` varchar(1) DEFAULT NULL,
  `st_lum` varchar(5) DEFAULT NULL,
  `st_lumerr1` varchar(4) DEFAULT NULL,
  `st_lumerr2` varchar(5) DEFAULT NULL,
  `st_lumlim` varchar(1) DEFAULT NULL,
  `st_dens` varchar(5) DEFAULT NULL,
  `st_denserr1` varchar(5) DEFAULT NULL,
  `st_denserr2` varchar(6) DEFAULT NULL,
  `st_denslim` varchar(1) DEFAULT NULL,
  `st_metfe` varchar(5) DEFAULT NULL,
  `st_metfeerr1` varchar(4) DEFAULT NULL,
  `st_metfeerr2` varchar(5) DEFAULT NULL,
  `st_metfelim` varchar(1) DEFAULT NULL,
  `st_metratio` varchar(6) DEFAULT NULL,
  `st_age` varchar(4) DEFAULT NULL,
  `st_ageerr1` varchar(4) DEFAULT NULL,
  `st_ageerr2` varchar(5) DEFAULT NULL,
  `st_agelim` varchar(1) DEFAULT NULL,
  `st_vsini` varchar(5) DEFAULT NULL,
  `st_vsinierr1` varchar(4) DEFAULT NULL,
  `st_vsinierr2` varchar(5) DEFAULT NULL,
  `st_vsinilim` varchar(1) DEFAULT NULL,
  `st_acts` varchar(4) DEFAULT NULL,
  `st_actserr` varchar(4) DEFAULT NULL,
  `st_actslim` varchar(1) DEFAULT NULL,
  `st_actr` varchar(4) DEFAULT NULL,
  `st_actrerr` varchar(10) DEFAULT NULL,
  `st_actrlim` varchar(1) DEFAULT NULL,
  `st_actlx` varchar(4) DEFAULT NULL,
  `st_actlxerr` varchar(10) DEFAULT NULL,
  `st_actlxlim` varchar(1) DEFAULT NULL,
  `swasp_id` varchar(26) DEFAULT NULL,
  `st_nts` int(2) DEFAULT NULL,
  `st_nplc` int(2) DEFAULT NULL,
  `st_nglc` int(1) DEFAULT NULL,
  `st_nrvc` int(2) DEFAULT NULL,
  `st_naxa` int(2) DEFAULT NULL,
  `st_nimg` int(1) DEFAULT NULL,
  `st_nspec` int(2) DEFAULT NULL,
  `st_uj` varchar(5) DEFAULT NULL,
  `st_ujerr` varchar(4) DEFAULT NULL,
  `st_ujlim` varchar(1) DEFAULT NULL,
  `st_vj` varchar(5) DEFAULT NULL,
  `st_vjerr` varchar(4) DEFAULT NULL,
  `st_vjlim` varchar(1) DEFAULT NULL,
  `st_bj` varchar(5) DEFAULT NULL,
  `st_bjerr` varchar(4) DEFAULT NULL,
  `st_bjlim` varchar(1) DEFAULT NULL,
  `st_rc` varchar(5) DEFAULT NULL,
  `st_rcerr` varchar(4) DEFAULT NULL,
  `st_rclim` varchar(1) DEFAULT NULL,
  `st_ic` varchar(5) DEFAULT NULL,
  `st_icerr` varchar(4) DEFAULT NULL,
  `st_iclim` varchar(1) DEFAULT NULL,
  `st_j` varchar(5) DEFAULT NULL,
  `st_jerr` varchar(4) DEFAULT NULL,
  `st_jlim` varchar(2) DEFAULT NULL,
  `st_h` varchar(5) DEFAULT NULL,
  `st_herr` varchar(4) DEFAULT NULL,
  `st_hlim` varchar(2) DEFAULT NULL,
  `st_k` varchar(5) DEFAULT NULL,
  `st_kerr` varchar(4) DEFAULT NULL,
  `st_klim` varchar(2) DEFAULT NULL,
  `st_wise1` varchar(5) DEFAULT NULL,
  `st_wise1err` varchar(4) DEFAULT NULL,
  `st_wise1lim` varchar(2) DEFAULT NULL,
  `st_wise2` varchar(5) DEFAULT NULL,
  `st_wise2err` varchar(4) DEFAULT NULL,
  `st_wise2lim` varchar(2) DEFAULT NULL,
  `st_wise3` varchar(5) DEFAULT NULL,
  `st_wise3err` varchar(4) DEFAULT NULL,
  `st_wise3lim` varchar(2) DEFAULT NULL,
  `st_wise4` varchar(5) DEFAULT NULL,
  `st_wise4err` varchar(4) DEFAULT NULL,
  `st_wise4lim` varchar(2) DEFAULT NULL,
  `st_irac1` varchar(4) DEFAULT NULL,
  `st_irac1err` varchar(4) DEFAULT NULL,
  `st_irac1lim` varchar(1) DEFAULT NULL,
  `st_irac2` varchar(4) DEFAULT NULL,
  `st_irac2err` varchar(4) DEFAULT NULL,
  `st_irac2lim` varchar(1) DEFAULT NULL,
  `st_irac3` varchar(4) DEFAULT NULL,
  `st_irac3err` varchar(4) DEFAULT NULL,
  `st_irac3lim` varchar(1) DEFAULT NULL,
  `st_irac4` varchar(4) DEFAULT NULL,
  `st_irac4err` varchar(4) DEFAULT NULL,
  `st_irac4lim` varchar(1) DEFAULT NULL,
  `st_mips1` varchar(8) DEFAULT NULL,
  `st_mips1err` varchar(7) DEFAULT NULL,
  `st_mips1lim` varchar(1) DEFAULT NULL,
  `st_mips2` varchar(8) DEFAULT NULL,
  `st_mips2err` varchar(7) DEFAULT NULL,
  `st_mips2lim` varchar(1) DEFAULT NULL,
  `st_mips3` varchar(8) DEFAULT NULL,
  `st_mips3err` varchar(7) DEFAULT NULL,
  `st_mips3lim` varchar(1) DEFAULT NULL,
  `st_iras1` varchar(8) DEFAULT NULL,
  `st_iras1err` varchar(7) DEFAULT NULL,
  `st_iras1lim` varchar(1) DEFAULT NULL,
  `st_iras2` varchar(8) DEFAULT NULL,
  `st_iras2err` varchar(7) DEFAULT NULL,
  `st_iras2lim` varchar(1) DEFAULT NULL,
  `st_iras3` varchar(8) DEFAULT NULL,
  `st_iras3err` varchar(7) DEFAULT NULL,
  `st_iras3lim` varchar(1) DEFAULT NULL,
  `st_iras4` varchar(8) DEFAULT NULL,
  `st_iras4err` varchar(7) DEFAULT NULL,
  `st_iras4lim` varchar(1) DEFAULT NULL,
  `st_photn` int(3) DEFAULT NULL,
  `st_umbj` varchar(4) DEFAULT NULL,
  `st_umbjerr` varchar(4) DEFAULT NULL,
  `st_umbjlim` varchar(1) DEFAULT NULL,
  `st_bmvj` varchar(4) DEFAULT NULL,
  `st_bmvjerr` varchar(4) DEFAULT NULL,
  `st_bmvjlim` varchar(1) DEFAULT NULL,
  `st_vjmic` varchar(4) DEFAULT NULL,
  `st_vjmicerr` varchar(4) DEFAULT NULL,
  `st_vjmiclim` varchar(1) DEFAULT NULL,
  `st_vjmrc` varchar(4) DEFAULT NULL,
  `st_vjmrcerr` varchar(4) DEFAULT NULL,
  `st_vjmrclim` varchar(1) DEFAULT NULL,
  `st_jmh2` varchar(5) DEFAULT NULL,
  `st_jmh2err` varchar(4) DEFAULT NULL,
  `st_jmh2lim` varchar(2) DEFAULT NULL,
  `st_hmk2` varchar(5) DEFAULT NULL,
  `st_hmk2err` varchar(4) DEFAULT NULL,
  `st_hmk2lim` varchar(2) DEFAULT NULL,
  `st_jmk2` varchar(5) DEFAULT NULL,
  `st_jmk2err` varchar(4) DEFAULT NULL,
  `st_jmk2lim` varchar(2) DEFAULT NULL,
  `st_bmy` varchar(4) DEFAULT NULL,
  `st_bmyerr` varchar(4) DEFAULT NULL,
  `st_bmylim` varchar(1) DEFAULT NULL,
  `st_m1` varchar(4) DEFAULT NULL,
  `st_m1err` varchar(4) DEFAULT NULL,
  `st_m1lim` varchar(1) DEFAULT NULL,
  `st_c1` varchar(5) DEFAULT NULL,
  `st_c1err` varchar(4) DEFAULT NULL,
  `st_c1lim` varchar(1) DEFAULT NULL,
  `st_colorn` int(2) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`rowid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
