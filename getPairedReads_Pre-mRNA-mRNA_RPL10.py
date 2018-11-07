import pysam
import sys

sampleName = sys.argv[1] 

file_mmRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA.bam", "rb")
names_mmRNA = [read.query_name for read in file_mmRNA.fetch()]
with open(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_ReadNames.txt","w") as fw:
    fw.write("\n".join(names_mmRNA))
    fw.write("\n")
file_PremRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA.bam", "rb")
names_PremRNA = [read.query_name for read in file_PremRNA.fetch()]                
with open(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_ReadNames.txt","w") as pw:
    pw.write("\n".join(names_PremRNA))
    pw.write("\n")
    
# Get paired reads
#samtools view ../DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam | fgrep -w -f DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_ReadNames.txt > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads.sam
#samtools view ../DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam | fgrep -w -f DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_ReadNames.txt > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads.sam

# Concatenate paired reads sam with header
# cat DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_Header.sam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads.sam > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_PlusHeader.sam
# cat DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_Header.sam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads.sam > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_PlusHeader.sam

# Convert sam file to bam file
#samtools view -u DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_PlusHeader.sam | samtools sort -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_Sorted.bam
#samtools view -u DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_PlusHeader.sam | samtools sort -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_Sorted.bam

    
    
# Convert bam to fastq 
#samtools fastq -N -1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_R1.fastq -2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_R2.fastq DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_Sorted.bam
#samtools fastq -N -1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R1.fastq -2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R2.fastq DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_Sorted.bam

# Get paired reads
#samtools view ../NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords.bam | fgrep -w -f NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_ReadNames.txt > NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads.sam
#samtools view ../NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords.bam | fgrep -w -f NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_ReadNames.txt > NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads.sam

# Concatenate paired reads sam with header
# cat NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_Header.sam NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads.sam > NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_PlusHeader.sam
# cat NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_Header.sam NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads.sam > NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_PlusHeader.sam

# Convert sam file to bam file
#samtools view -u NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_PlusHeader.sam | samtools sort -o NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_Sorted.bam
#samtools view -u NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_PlusHeader.sam | samtools sort -o NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_Sorted.bam

    
    
# Convert bam to fastq 
#samtools fastq -N -1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_R1.fastq -2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_R2.fastq NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA_PairedReads_Sorted.bam
#samtools fastq -N -1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R1.fastq -2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R2.fastq NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_PairedReads_Sorted.bam

#samtools fastq -N -1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R1.fastq -2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R2.fastq NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_PairedReads_Sorted.bam
#samtools fastq -N -1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R1.fastq -2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R2.fastq NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_PairedReads_Sorted.bam