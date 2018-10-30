library(ggplot2)
library(reshape)

data <- read.table("../tmp/Madrasin_HiSeq_October2018_alignments/Combined_PlusMinusDMS_Aligned_MAPQscores.tsv",header=TRUE,sep="\t")
p<- ggplot(data, aes(x=MAPQ, fill=Sample, color=Sample)) +
  geom_histogram(alpha=0.25, binwidth=5,position="identity") +
    ggtitle(paste("Frequency of MAPQ values for\n Plus and Minus DMS",sampleName,sep=" ")) +
    xlab("\nMAPQ values") +
    ylab("Frequency\n") +
    theme(axis.title.x=element_text(face="bold",size=12),axis.title.y=element_text(face="bold",size=12),
          axis.text.x = element_text(face="bold",size=8),axis.text.y = element_text(face="bold",size=8),
         plot.title = element_text(face="bold",size=15))
filenameToSave = paste("../results/Madrasin_HiSeq_October2018_alignments/GGplot2-FrequencyMAPQvalsPlusMinusDMS.png",sep="")
print(filenameToSave)
ggsave(p,file=filenameToSave,width=8.1,height=5.6,dpi=300)