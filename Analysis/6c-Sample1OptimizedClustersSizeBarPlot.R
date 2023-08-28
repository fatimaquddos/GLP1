# This script was used to visualize the distribution of size of the final optimized clusters for Sample 1 using Bar plot

# Load required libraries
library(ggplot2)

# Read data
Sample1MainClusterSizes <- read.csv("Sample1FinalClusterSizes.csv")

# Create a factor of the main clusters columns
Sample1MainClusterSizes$labels <- factor(Sample1MainClusterSizes$labels, levels = c(1,2,3,4,5,6,8,7))

Sample1MainClusterSizes$labels <- factor(Sample1MainClusterSizes$labels, levels = c(1,2,3,4,5,6,8,7))
Sample1MainClusterSizes$Sample1MainClusters <- factor(Sample1MainClusterSizes$Sample1MainClusters, 
                                                      levels = c("Gratitude and Positive Feelings", "Weight loss and Obesity",
                                                                                                              "Effects of Medications", "Healthcare and Pharmacy", "Dose-related",
                                                                                                              "Insurance and Coverage", "Diabetes", "Unclassified"))

# Create the bar plot for final optimized clusters
BAR <- ggplot(Sample1MainClusterSizes, aes(x=Sample1MainClusters, y=prct, fill = labels)) +
  geom_bar(stat="identity", position = 'dodge') + 
  labs(title='Optimized clusters size distribution', x='Optimized clusters', y='% of total posts in cluster', fill='Clusters') + 
  geom_text(aes(label=prct), position = position_dodge(width = 0.9), vjust=-0.3, size=4) + 
  theme_minimal() +
  theme(legend.position="none", axis.text.x = element_text(angle = 45, hjust=1)) +
  #theme(legend.position="none", axis.text = element_text(size=18), axis.title = element_text(size = 20), plot.title = element_text(size = 22, hjust = 0.5),  axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1, colour = "black", size = 20), axis.text.y = element_text()) +  
  scale_fill_manual(labels = c("Gratitude and Positive Feelings", "Weight loss and Obesity",
                                "Effects of Medications", "Healthcare and Pharmacy", "Dose-related",
                                "Insurance and Coverage", "Diabetes", "Unclassified"),
                     values=c("#0048BA", "#B0BF1A", "black", "#C46210","red","#3B7A57","#FFBF00", "gray")) +
 theme(axis.text.x = element_blank()) +
  scale_y_continuous(limits=c(0,0.30), labels = scales::percent_format(accuracy = 1))

BAR
