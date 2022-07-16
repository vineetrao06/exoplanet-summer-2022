
local({
  .Table <- with(Exo, table(st_metratio))
  cat("\ncounts:\n")
  print(.Table)
  cat("\npercentages:\n")
  print(round(100*.Table/sum(.Table), 2))
})
local({
  .Table <- with(Exo, table(st_metratio))
  cat("\ncounts:\n")
  print(.Table)
  cat("\npercentages:\n")
  print(round(100*.Table/sum(.Table), 2))
})
RegModel.1 <- lm(gaia_gmag~st_age, data=Exo)
summary(RegModel.1)
RegModel.2 <- lm(gaia_gmag~st_age, data=Exo)
summary(RegModel.2)

