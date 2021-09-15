# scatter plot
# -----------------------------

rm(list = ls())
options(scipen = 999)

library(tidyverse)

## load table
dat <- read.csv("../looping_score/looping_score.fin.txt", sep = "\t", header = T, row.names = 1)


## plot

library(viridis)
library(ggthemes)
library(ggrepel)
library(ggpubr)


theme_set(theme_few() +
    theme(legend.justification = c(0, 1),
        legend.position = c(0, 1),
        legend.background = element_blank(),
        legend.key = element_blank(),
        legend.key.size = unit(14, "pt"),
        legend.title=element_blank())
)


ggplot() +
    geom_point(data = dat, aes(x = zscore, y = peak_num, color = zscore),
        position = position_nudge(y = -0.1), size = 2) +
    scale_color_viridis(option = "viridis", limits = c(min(dat$zscore), tail(sort(dat$zscore),2)[1]), oob = scales::squish) +
    geom_text_repel(data = dat %>% filter(abs(zscore) >= 1 | peak_num >= 100000),
                    aes(zscore, peak_num, label = dat %>% filter(abs(zscore) >= 1 | peak_num >= 100000) %>% row.names()),
                size = 2.8, segment.size = 0.2, segment.color = "#DCDCDC", parse = T) +
    scale_fill_gradient(limits = c(min(dat$zscore), max(dat$zscore))) +
    xlab("Looping Z-score") + ylab("Peak number") +
    stat_cor(data = dat %>% select(zscore, peak_num), aes(zscore, peak_num),
        method = "pearson", label.x.npc = .08, label.y.npc = 1, output.type ="latex")

ggsave("../figs/zscore_vs_peak.png", width = 6.7, height = 6.7)
