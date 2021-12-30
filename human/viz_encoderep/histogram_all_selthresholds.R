# histogram for all TF z-score
# add group spliting line
# -----------------------------

rm(list = ls())

library(tidyverse)


## load table
dat <- read.csv("../looping_score_v3/zmat_thresholds.txt", sep = "\t", header = T)

fin_df <- read.csv("../looping_score_v3/contact_zscore.fin.txt", sep = "\t", header = T, row.names = 1)

## ctcf and cohesin zsocre
ctcf_mean <- mean(fin_df$zscore[grep("CTCF", row.names(fin_df))])
rad21_mean <- mean(fin_df$zscore[grep("RAD21", row.names(fin_df))])

smc3 <- fin_df$zscore[grep("SMC3", row.names(fin_df))]
smc1 <- fin_df$zscore[grep("SMC1A", row.names(fin_df))]


## split into 3 groups
mk1 <- fin_df["BRCA1_45698", "zscore"]
mk2 <- fin_df["EGR1_ENCFF100KKH", "zscore"]

## plot
library(ggplot2)
library(ggthemes)
library(reshape2)


plot_dat <- melt(dat)

theme_set(
    theme_few() +
    theme(legend.position = "none")
)

p <- ggplot(plot_dat, aes(x = value))

p <- p + geom_histogram(aes(y = stat(density), colour = "black"), fill = "white", bins = 35) +
    geom_density(alpha = 0.4, fill = "#69b3a2") +
    scale_color_manual(values = c("#868686FF")) + ## color of bins
    # geom_vline(aes(xintercept = ctcf_mean),  ## ctcf line
                # linetype = "dotted", size = 0.6, color = "#AE123A") +
    geom_text(aes(x = ctcf_mean, y = .01, label = paste0("CTCF: ", round(ctcf_mean, 2))), color = "#AE123A", angle = 45, size = 3, nudge_x = .15) +
    # geom_vline(aes(xintercept = rad21_mean),  ## rad21 line
                # linetype = "dotted", size = 0.6, color = "#2E5A87") +
    geom_text(aes(x = rad21_mean, y = .01, label = paste0("RAD21: ", round(rad21_mean, 2))), color = "#2E5A87", angle = 45, size = 3) +
    # geom_vline(aes(xintercept = smc1),  ## smc1 line
                # linetype = "dotted", size = 0.6, color = "#2E5A87") +
    geom_text(aes(x = smc1, y = .01, label = paste0("SMC1A: ", round(smc1, 2))), color = "#2E5A87", angle = 45, size = 3) +
    # geom_vline(aes(xintercept = smc3),  ## smc3 line
                # linetype = "dotted", size = 0.6, color = "#2E5A87") +
    geom_text(aes(x = smc3, y = .01, label = paste0("SMC3: ", round(smc3, 2))), color = "#2E5A87", angle = 45, size = 3) +
    geom_vline(aes(xintercept = mk1),
                linetype = "dotted", size = 0.6, color = "#5D6D7E") +
    geom_vline(aes(xintercept = mk2),
                linetype = "dotted", size = 0.6, color = "#5D6D7E") +
    # geom_vline(aes(xintercept = wapl),  ## wapl line
            #   linetype = "dashed", size = 0.8, color = "#5D6D7E")+
    # geom_text(aes(x = wapl, y = 0.5, label = paste0("WAPL: ", round(wapl, 2))),
            #   color = "#34495E")+

    # labs(title = "Loop Z-Score Histogram", subtitle = "Human") +
    ylab("Dens.") +
    xlab("Contact Z-score") +
    ylim(0, 0.85)
# ggsave(filename = "hisogram_all_zscore.png", path = "../figs/", width = 6.7, height = 6.7)
# ggsave(filename = "hisogram_all_zscore.pdf", path = "../figs/", width = 6.7, height = 6.7)


p_fixed <- egg::set_panel_size(p, width  = unit(6, "in"), height = unit(6, "in"))


ggsave(filename = "hisogram_all_zscore_v3.png", p_fixed, path = "../figs/encode_rep", width = 7, height = 7)
ggsave(filename = "hisogram_all_zscore_v3.pdf", p_fixed, path = "../figs/encode_rep", width = 7, height = 7)
