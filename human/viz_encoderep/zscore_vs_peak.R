# scatter plot
# -----------------------------

rm(list = ls())
# options(scipen = 999)

library(tidyverse)

## load table
# loop zscore
zscore <- read.csv("../looping_score_v3/contact_zscore.fin.txt", sep = "\t", header = T, row.names = 1)

# peak percentage against CTCF
## need a new method to get the percentage of peaks

per <- read.csv("../../../peak_overlap/hs/getpct/ave_ind_pct.txt",  sep = "\t", header = T, row.names = 1)
colnames(per) <- "percent"

## merge
dat <- merge(zscore, per * 100, by = 0, all = TRUE)
dat <- arrange(dat, desc(zscore))


## split into 3 groups
mk1 <- (dat %>% filter(Row.names == "BRCA1_45698"))$zscore
mk2 <- (dat %>% filter(Row.names == "EGR1_ENCFF100KKH"))$zscore


## plot

library(viridis)
library(ggthemes)
library(ggrepel)
library(ggpubr)


theme_set(theme_few() +
    theme(
        legend.justification = c("right", "bottom"),
        legend.position = c(1, .02),
        legend.background = element_blank(),
        legend.key = element_blank(),
        legend.key.size = unit(.35, "cm"),
        legend.title = element_text(size = 10))
        # legend.text  = element_text(size = 8))
        # legend.title = element_blank())
)


p <- ggplot() +
    geom_point(data = dat, aes(x = zscore, y = peak, fill = zscore, size = percent),
        position = position_nudge(y = -0.1), shape = 21, alpha = .8) +
    scale_fill_viridis(option = "viridis", limits = c(min(dat$zscore), tail(sort(dat$zscore),2)[1]), oob = scales::squish) +
    geom_text_repel(data = dat %>% filter(abs(zscore) >= .75 | peak >= 100000),
                    aes(zscore, peak, label = Row.names),
                size = 2.8, segment.size = 0.2, segment.color = "#DCDCDC", parse = T) +
    # scale_fill_gradient(limits = c(min(dat$zscore), max(dat$zscore))) +
    geom_vline(aes(xintercept = mk1),
                linetype = "dotted", size = 0.6, color = "#5D6D7E") +
    geom_vline(aes(xintercept = mk2),
                linetype = "dotted", size = 0.6, color = "#5D6D7E") +
    xlab("Contact Z-score") + ylab("Peak Num.") +
    labs(fill = "Contact Z-score", size = "% CTCF Peaks") +
    stat_cor(data = dat %>% select(zscore, peak), aes(zscore, peak),
        method = "pearson", label.x.npc = 0, label.y.npc = 1, output.type ="latex")

p_fixed <- egg::set_panel_size(p, width  = unit(6, "in"), height = unit(6, "in"))

# ggsave("../figs/zscore_vs_peak.png", width = 6.7, height = 6.7)
# ggsave("../figs/zscore_vs_peak.pdf", width = 6.7, height = 6.7)

# ggsave("../figs/zscore_vs_peak_new.png", width = 6.7, height = 6.7)
# ggsave("../figs/zscore_vs_peak_new.pdf", width = 6.7, height = 6.7)

ggsave("../figs/zscore_vs_peak_v3.png", p_fixed, width = 7, height = 7)
ggsave("../figs/zscore_vs_peak_v3.pdf", p_fixed, width = 7, height = 7)



## peak num vs zscore
p <- ggplot() +
    geom_point(data = dat, aes(x = peak, y = zscore, fill = zscore, size = percent),
        position = position_nudge(y = -0.1), shape = 21, alpha = .8) +
    scale_fill_viridis(option = "viridis", limits = c(min(dat$zscore), tail(sort(dat$zscore),2)[1]), oob = scales::squish) +
    geom_text_repel(data = dat %>% filter(abs(zscore) >= .75 | peak >= 100000),
                    aes(peak, zscore, label = Row.names),
                size = 2.8, segment.size = 0.2, segment.color = "#DCDCDC", parse = T) +
    # scale_fill_gradient(limits = c(min(dat$zscore), max(dat$zscore))) +
    geom_hline(aes(yintercept = mk1),
                linetype = "dotted", size = 0.6, color = "#5D6D7E") +
    geom_hline(aes(yintercept = mk2),
                linetype = "dotted", size = 0.6, color = "#5D6D7E") +
    ylab("Contact Z-score") + xlab("Peak Num.") +
    labs(fill = "Contact Z-score", size = "% CTCF Peaks") +
    stat_cor(data = dat %>% select(peak, zscore), aes(peak, zscore),
        method = "pearson", label.x.npc = 0, label.y.npc = 1, output.type ="latex")

p_fixed <- egg::set_panel_size(p, width  = unit(6, "in"), height = unit(6, "in"))

# ggsave("../figs/peak_vs_zscore.png", width = 6.7, height = 6.7)
# ggsave("../figs/peak_vs_zscore.pdf", width = 6.7, height = 6.7)

# ggsave("../figs/peak_vs_zscore_new.png", width = 6.7, height = 6.7)
# ggsave("../figs/peak_vs_zscore_new.pdf", width = 6.7, height = 6.7)

ggsave("../figs/peak_vs_zscore_v3.png", p_fixed, width = 7, height = 7)
ggsave("../figs/peak_vs_zscore_v3.pdf", p_fixed, width = 7, height = 7)
