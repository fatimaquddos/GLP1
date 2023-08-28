# This script was used to visualize the 2D UMAP components obtained from previous step for Sample 1 with a scatter plot

# Load required libraries
library(ggplot2)


# Read data
UMAPSample1 <- read.csv("UMAPComponentsSample1.csv", row.names=1)

UMAPSample1$labels <- factor(UMAPSample1$labels, levels = c(1,2,3,4,5,6,8,7))


# Create the scatter plot for final optimized clusters
UMAP <- ggplot(UMAPSample1, aes(UMAPx, UMAPy, colour = as.factor(labels))) +
  geom_point() +
  scale_color_manual(labels = c("Gratitude and Positive Feelings", "Weight loss and Obesity",
                                "Effects of Medications", "Healthcare and Pharmacy", "Dose-related",
                                "Insurance and Coverage", "Diabetes", "Unclassified"),
                     values=c("#0048BA", "#B0BF1A", "black", "#C46210","red","#3B7A57","#FFBF00", "gray")) +
  labs(title='Optimized clusters scatter plot', color='Optimized clusters') +
  guides(colour = guide_legend(override.aes = list(size=5))) + theme_minimal() +
  ylim(-7, 7) + xlim(0,20)
  #theme(axis.text = element_text(size=18), axis.title = element_text(size = 20), plot.title = element_text(size = 22, hjust = 0.5), legend.text = element_text(size = 20), legend.title = element_text(size = 20))

UMAP
