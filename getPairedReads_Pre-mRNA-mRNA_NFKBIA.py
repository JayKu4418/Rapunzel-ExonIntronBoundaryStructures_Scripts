import pysam
import sys

sampleName = sys.argv[1] 

#def extract_reads(query_names,bigbamFile,writebamfile):
#    n = query_names
#    bamfile = pysam.AlignmentFile(bigbamFile, 'rb')
#    name_indexed = pysam.IndexedReads(bamfile)
#    name_indexed.build()
#    header = bamfile.header.copy()
#    out = pysam.Samfile(writebamfile, 'wb', header=header)
#    for name in n:
#        try:
#            name_indexed.find(name)
#        except KeyError:
#            pass
#        else:
#            iterator = name_indexed.find(name)
#            for x in iterator:
#                out.write(x)

file_mmRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA.bam", "rb")
names_mmRNA = [read.query_name for read in file_mmRNA.fetch()]
with open(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_ReadNames.txt","w") as fw:
    fw.write("\n".join(names_mmRNA))
    fw.write("\n")
file_PremRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA.bam", "rb")
names_PremRNA = [read.query_name for read in file_PremRNA.fetch()]                
with open(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_ReadNames.txt","w") as pw:
    pw.write("\n".join(names_PremRNA))
    pw.write("\n")
#extract_reads(names_mmRNA,"../"+sampleName+"_MAPQgreaterThan10_SortedByCoords.bam",sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_PairedReads.bam")
#extract_reads(names_PremRNA,"../"+sampleName+"_MAPQgreaterThan10_SortedByCoords.bam",sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_PairedReads.bam")

# Convert bam to fastq 
#samtools fastq -N -1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R1.fastq -2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R2.fastq DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_PairedReads_Sorted.bam
#samtools fastq -N -1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R1.fastq -2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R2.fastq DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_PairedReads_Sorted.bam

#samtools fastq -N -1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R1.fastq -2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R2.fastq NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_PairedReads_Sorted.bam
#samtools fastq -N -1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R1.fastq -2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R2.fastq NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_PairedReads_Sorted.bam