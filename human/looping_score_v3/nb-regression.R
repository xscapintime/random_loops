# negative binomial regression
# ----------------------------

library(tidyverse)
library(reshape2)
library(MASS)

# contact number
dat_r1 <- read.csv("real_r1.txt", header = T, sep = "\t")
dat_r2 <- read.csv("real_r2.txt", header = T, sep = "\t")

dat <- cbind(dat_r1, dat_r2)

df <- melt(as.matrix(dat))
colnames(df) <- c("read", "tf", "contacts")
df$id <- unlist(lapply(as.character(df$tf), function(x) strsplit(x, "_r")[[1]][1]))

# peak number
score_tb <- read.csv("contact_zscore.fin.txt", header = T, sep = "\t")

df <- inner_join(df, score_tb[c("X", "peak")], by = c("id" = "X"))


## NB regression
glm.nb(formula = read ~ contacts, data = df, start = c(1, 1))
#>>> got two errors
# Error: no valid set of coefficients has been found: please supply starting values
# Error: cannot find valid starting values: please specify some
#>>> fk, forget it
