
exo <- 
  readXL("C:/Users/Robert/Temp/STEM/ASDRP/Exoplanet/planets_2019.06.06_15.41.16.xlsx",
   rownames=FALSE, header=TRUE, na="", sheet="planets_2019.06.06_15.41.16", 
  stringsAsFactors=TRUE)
summary(exo)
with(exo, Hist(gaia_dist, scale="frequency", breaks="Sturges", 
  col="darkgray"))
with(exo, Dotplot(gaia_gmag, bin=FALSE))
with(exo, Dotplot(pl_bmasse, bin=FALSE))
with(exo, Hist(pl_bmasse, scale="frequency", breaks="Sturges", 
  col="darkgray"))
densityPlot( ~ pl_bmasse, data=exo, bw=bw.SJ, adjust=1, kernel=dnorm, 
  method="adaptive")
library(mvtnorm, pos=16)
library(survival, pos=16)
library(MASS, pos=16)
library(TH.data, pos=16)
library(multcomp, pos=16)
library(abind, pos=21)
AnovaModel.1 <- aov(gaia_gmag ~ st_spstr, data=exo)
summary(AnovaModel.1)
with(exo, numSummary(gaia_gmag, groups=st_spstr, statistics=c("mean", 
  "sd")))
with(exo, tapply(gaia_gmag, st_optband,  var, na.rm=TRUE))
var.test(gaia_gmag ~ st_optband, alternative='two.sided', conf.level=.95, 
  data=exo)
library(tcltk, pos=22)
library(aplpack, pos=22)
with(exo, stem.leaf(gaia_gmag, na.rm=TRUE))
with(exo, plotMeans(gaia_gmag, st_spstr, error.bars="se", connect=TRUE))

