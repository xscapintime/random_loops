# peak number vs z-score dotplot with label
# divide the data to three groups
# --------------------------------


rm(list = ls())

library(tidyverse)


## load table
dat <- read.csv("../looping_score/looping_score.fin.txt", sep = "\t", header = T, row.names = 1)


## ctcf and rad21 zsocre average
ctcf_mean <- mean(dat$zscore[grep("CTCF", row.names(dat))])
rad21_mean <- mean(dat$zscore[grep("RAD21", row.names(dat))])

# replace
# dat <- dat %>% filter(!grepl(pattern = "CTCF|RAD21", x = row.names(dat)))
# dat <- rbind(dat, ctcf_mean, rad21_mean) #mean of peak number? feels wrong

## set the group
dat$group <- ifelse(dat$zscore > .4, "top", ifelse(dat$zscore < -.4, "bott", "mid"))


## dotplot
library(ggplot2)
library(ggpubr)
library(ggpmisc)

theme_set(theme_bw())
options(scipen = 999)

# highlight the sigs
p <- ggplot(dat, aes(x = zscore, y = peak_num))

formula <- y ~ x

p + geom_point(aes(color = group), alpha = 0.6) +
    scale_color_manual(values = c("#1E90FF", "#C0C0C0", "#F08080")) +
    #geom_smooth(method = "auto", se = TRUE, fullrange = FALSE, level = 0.95) +
    ggrepel::geom_text_repel(data = dat %>% filter(group != "mid"),#& row.names(dat) %in% colnames(tf)),
                            mapping = aes(label = row.names(filter(dat,group != "mid"))), size = 3,
                            segment.color = "#DCDCDC", segment.size = 0.3,
                            parse = T, max.overlaps = Inf) +

    #geom_rug(sides='l', color='black')+

    geom_vline(aes(xintercept = mean(ctcf_mean)), 
                linetype = "dashed", size = 0.6, color = "#16A085") +
  geom_text(aes(x = mean(ctcf[q,]*1.02), 
                y = 25000, label = "CTCF"), color = "#138D75") +
  geom_vline(aes(xintercept = mean(rad21[q,])), 
             linetype = "dashed", size = 0.6, color = "#16A085") +
  geom_text(aes(x = mean(rad21[q,]*1.02), 
                y = 25000, label = "RAD21"), color = "#138D75") +
  #geom_vline(aes(xintercept = mean(wapl[q,])), 
  #           linetype = "dashed", size = 0.6, color = "#5D6D7E")+
  #geom_text(aes(x = mean(wapl[q,]+.05) , 
  #              y = 120000, label = "WAPL"), color = "#34495E")+
  
  labs(title = "Human: Z-Score vs. No. of Peaks",
       subtitle = paste0("threshold: ", row.names(tf)[q]),
       x = "Z-Score", y = "No. of Peaks") +
  theme(legend.position = "none") +
  #stat_cor(method = "pearson",hjust=2.25,vjust=-26)+
  #stat_poly_eq(
  #aes(label = ..eq.label..),
  #formula = formula,parse = TRUE, geom = "text",vjust=1, hjust=1)+
  coord_flip()
ggsave(filename = paste0("threshold_", seq(1,20,1)[q], ".png"),
       path = "../../figure/ex_itr_zvp_comb/")