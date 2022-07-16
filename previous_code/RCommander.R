
library(abind, pos=16)
library(e1071, pos=17)
numSummary(planets[,"pl_orbper", drop=FALSE], statistics=c("mean", "sd", "IQR", 
  "quantiles"), quantiles=c(0,.25,.5,.75,1))
numSummary(planets[,"pl_orbper", drop=FALSE], statistics=c("mean", "sd", "se(mean)", "IQR", 
  "quantiles", "cv"), quantiles=c(0,.25,.5,.75,1))
numSummary(planets[,"pl_orbper", drop=FALSE], statistics=c("mean", "sd", "se(mean)", "IQR", 
  "quantiles", "cv"), quantiles=c(0,.25,.5,.75,1))
with(planets, tapply(pl_orblper, list(st_spstr), mean, na.rm=TRUE))
with(planets, tapply(pl_orblper, list(st_spstr), mean, na.rm=TRUE))

