# histogram for all TF z-score
# -----------------------------

rm(list = ls())

library(tidyverse)


## load table
dat <- read.csv("../looping_score/looping_score.fin.txt", sep = "\t", header = T, row.names = 1)


## ctcf and cohesin zsocre
ctcf_mean <- mean(dat$zscore[grep("Ctcf", row.names(dat))])
rad21_mean <- mean(dat$zscore[grep("Rad21", row.names(dat))])

smc1 <- dat$zscore[grep("Smc1", row.names(dat))]


## plot
library(ggplot2)

theme_set(
    theme_classic() +
    theme(legend.position = "none")
)

p <- ggplot(dat, aes(x = zscore))

p + geom_histogram(aes(y = stat(density), colour = "black"), fill = "white", bins = 50) +
    geom_density(alpha = 0.4, fill = "#69b3a2") +
    scale_color_manual(values = c("#868686FF")) + ## color of bins
    geom_vline(aes(xintercept = ctcf_mean),  ## ctcf line
                linetype = "dashed", size = 0.6, color = "#AE123A") +
    geom_text(aes(x = ctcf_mean, y = ctcf_mean/2, label = paste0("Ctcf: ", round(ctcf_mean, 2))),
            color = "#AE123A") +
    geom_vline(aes(xintercept = rad21_mean),  ## rad21 line
                linetype = "dashed", size = 0.6, color = "#2E5A87") +
    geom_text(aes(x = rad21_mean, y = rad21_mean/1.8, label = paste0("Rad21: ", round(rad21_mean, 2))),
            color = "#2E5A87") +
    geom_vline(aes(xintercept = smc1),  ## smc1 line
                linetype = "dashed", size = 0.6, color = "#2E5A87") +
    geom_text(aes(x = smc1, y = smc1/2.2, label = paste0("Smc1: ", round(smc1, 2))),
            color = "#2E5A87") +

    # geom_vline(aes(xintercept = smc3),  ## smc3 line
    #             linetype = "dashed", size = 0.6, color = "#2E5A87") +
    # geom_text(aes(x = smc3, y = smc3/2, label = paste0("SMC3: ", round(smc3, 2))),
    #         color = "#2E5A87") +

    # geom_vline(aes(xintercept = wapl),  ## wapl line
            #   linetype = "dashed", size = 0.8, color = "#5D6D7E")+
    # geom_text(aes(x = wapl, y = 0.5, label = paste0("WAPL: ", round(wapl, 2))),
            #   color = "#34495E")+

    labs(title = "Loop Z-Score Histogram",
        subtitle = "Mouse") +
    ylab("Dens.") +
    xlab("Z-Score")
    # xlim(-2.2, 2.2) + ylim(0, 0.85)

ggsave(filename = "hisogram_all_zscore.png", path = "../figs/", width = 7, height = 7)