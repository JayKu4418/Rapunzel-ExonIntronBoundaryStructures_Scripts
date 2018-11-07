import pysam
import sys

#samtools view -b -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496.bam ../DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam chrX:154399297-154399496
#samtools index DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496.bam
#samtools view -b -o NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496.bam ../NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords.bam chrX:154399297-154399496
#samtools index NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496.bam

sampleName = sys.argv[1] 

wholesamfile = pysam.AlignmentFile("../"+sampleName+"_MAPQgreaterThan10_SortedByCoords.bam","rb")
smallsamfile = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496.bam","rb")

readNamesInSmallSamFile = [read.query_name for read in smallsamfile.fetch()]
print len(readNamesInSmallSamFile)
reads_Interest = [read for read in wholesamfile.fetch("chrX",154398065,154402339) if read.query_name in readNamesInSmallSamFile]
print(len(reads_Interest))
      
writefile_BothPairs = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PairedReads.bam", "wb", template=wholesamfile)

for read in reads_Interest:
    writefile_BothPairs.write(read)
    
pure_introns = range(154398543-1,154399337-2) + range(154399397-1,154399486-2) + range(154399595-1,154399802-2) + range(154399942-1,154400463-2) + range(154400627-1,154400701-2)
pure_exons = range(154398065-1,154398394-2) + range(154398497-1,154398542-2) + range(154399338-1,154399396-2) + range(154399803-1,154399941-2) + range(154400702-1,154402339-2) 
ambiguous = range(154398395-1,154398496-2) + range(154399487-1,154399594-2) + range(154400464-1,154400626-2)

#samfile = pysam.AlignmentFile("DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam","rb")

#reads_PremRNA = []

#reads_mmRNA = []

#reads_ambiguous = []


writefile_PremRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA.bam", "wb", template=smallsamfile)
writefile_mmRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_MaturemRNA.bam", "wb", template=smallsamfile)
writefile_ambRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_ambiguous.bam", "wb", template=smallsamfile)

for read in smallsamfile.fetch():
    
    # Get all positions read is in 
    positions_Read = read.get_reference_positions(full_length=True)
    
    # Check number of positions in read that are in pure introns
    positions_Read_In_Intron = [i for i in positions_Read if i in pure_introns]
    
    # Check number of positions in the read are in the ambiguous positions
    positions_Read_In_Ambiguous = [i for i in positions_Read if i in ambiguous]
    
    # Check number of positions in the read that are in the pure exons positions
    positions_Read_In_Exon = [i for i in positions_Read if i in pure_exons]
    
    # If at least even 1 position is in pure intron then it must be pre-mRNA
    if len(positions_Read_In_Intron)!=0:
        #reads_PremRNA.append(read)
        writefile_PremRNA.write(read)
    # If zero are in pre-mRNA, then we have to check if its mature mRNA or ambiguous
    else:
        # Get the read pair
        read_pair = [i for i in reads_Interest if i.query_name==read.query_name and i!=read]
        # If there is read pair continue, else read is ambiguous
        if len(read_pair)==1:
            # Get the positions of the read pair
            positions_ReadPair = read_pair[0].get_reference_positions(full_length=True)
            # Check number of  positions in read that are in pure introns
            positions_ReadPair_In_Intron = [i for i in positions_ReadPair if i in pure_introns]
            # Check number of positions in the read are in the ambiguous positions
            positions_ReadPair_In_Ambiguous = [i for i in positions_ReadPair if i in ambiguous]
            # Check number of positions in the read that are in the pure exons positions
            positions_ReadPair_In_Exon = [i for i in positions_ReadPair if i in pure_exons]
            # If there positions in the read pair that are intronic, then read is pre-mRNA
            if len(positions_ReadPair_In_Intron)!=0:
                #reads_PremRNA.append(read)
                writefile_PremRNA.write(read)
            # Else if there are positions in both the read and read pair that are exonic, then read is mature mRNA
            elif len(positions_Read_In_Exon)!=0 and len(positions_ReadPair_In_Exon)!=0:
                writefile_mmRNA.write(read)
            # If that's not the case, then read is ambiguous
            else:
                writefile_ambRNA.write(read)
                
        else:
            writefile_ambRNA.write(read)

#writefile_PremRNA_Paired = pysam.AlignmentFile("DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_Paired.bam", "wb", template=smallsamfile)
#writefile_mmRNA_Paired = pysam.AlignmentFile("DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_Paired.bam", "wb", template=smallsamfile)                







