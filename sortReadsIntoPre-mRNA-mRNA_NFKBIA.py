import pysam
import sys

sampleName = sys.argv[1] 

wholesamfile = pysam.AlignmentFile("../"+sampleName+"_MAPQgreaterThan10_SortedByCoords.bam","rb")
smallsamfile = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam","rb")

readNamesInSmallSamFile = [read.query_name for read in smallsamfile.fetch()]
print len(readNamesInSmallSamFile)
reads_Interest = [read for read in wholesamfile.fetch("chr14",35401510,35404754) if read.query_name in readNamesInSmallSamFile]
print(len(reads_Interest))
      
writefile_BothPairs = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PairedReads.bam", "wb", template=wholesamfile)

for read in reads_Interest:
    writefile_BothPairs.write(read)

exon0_start_coord = 35401510
exon0_end_coord = 35402060

intron0_start_coord = 35402061
intron0_end_coord = 35402393    
    
exon1_start_coord = 35402394
exon1_end_coord = 35402663

intron1_start_coord = 35402664
intron1_end_coord = 35402770

exon2_start_coord = 35402771
exon2_end_coord = 35402859

intron2_start_coord = 35402860
intron2_end_coord = 35403149

exon3_start_coord = 35403150
exon3_end_coord = 35403360

intron3_start_coord = 35403361
intron3_end_coord = 35403689

exon4_start_coord = 35403690
exon4_end_coord = 35403798

intron4_start_coord = 35403799
intron4_end_coord = 35404417

exon5_start_coord = 35404418
exon5_end_coord = 35404754

introns_interest = range(intron0_start_coord-1,intron0_end_coord-2) + range(intron3_start_coord-1,intron3_end_coord-2) + range(intron4_start_coord-1,intron4_end_coord-2)
print len(introns_interest)
#samfile = pysam.AlignmentFile("DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam","rb")

reads_PremRNA = []

reads_mmRNA = []

#reads_ambiguous = []


writefile_PremRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA.bam", "wb", template=smallsamfile)
writefile_mmRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA.bam", "wb", template=smallsamfile)
writefile_ambRNA = pysam.AlignmentFile(sampleName+"_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_ambiguous.bam", "wb", template=smallsamfile)

for read in smallsamfile.fetch():
    positions_Read = read.get_reference_positions(full_length=True)
    
    #positions_Read_noNone = [i for i in positions_Read if i!=None]
    
    # Check if pre-mRNA first
    positions_Read_In_Intron1 = [i for i in positions_Read if i in range(intron1_start_coord-1,intron1_end_coord-2)]
    positions_Read_In_Intron2 = [i for i in positions_Read if i in range(intron2_start_coord-1,intron2_end_coord-2)]
    
    if len(positions_Read_In_Intron1)!=0 or len(positions_Read_In_Intron2)!=0:
        reads_PremRNA.append(read)
        writefile_PremRNA.write(read)
    else:
        positions_Read_In_Exon1 = [i for i in positions_Read if i in range(exon1_start_coord-1,exon1_end_coord)]
        positions_Read_In_Exon2 = [i for i in positions_Read if i in range(exon2_start_coord-1,exon2_end_coord)]
        if len(positions_Read_In_Exon1)!=0 and len(positions_Read_In_Exon2)!=0:
            reads_mmRNA.append(read)
            writefile_mmRNA.write(read)
        #elif len(positions_Read_In_Exon1)==len(positions_Read_noNone) or len(positions_Read_In_Exon2)==len(positions_Read_noNone):
        else:
            read_pair = [i for i in reads_Interest if i.query_name==read.query_name and i!=read]
            #reads_ambiguous.append(read)
            if len(read_pair)==1:
                positions_ReadPair_In_Introns_0_3_4 = [i for i in read_pair[0].get_reference_positions(full_length=True) if i in introns_interest]
                if len(positions_ReadPair_In_Introns_0_3_4)!=0:
                    reads_PremRNA.append(read)
                    writefile_PremRNA.write(read)
                else:
                    reads_mmRNA.append(read)
                    writefile_mmRNA.write(read)
            else:
                writefile_ambRNA.write(read)


#writefile_PremRNA_Paired = pysam.AlignmentFile("DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_Paired.bam", "wb", template=smallsamfile)
#
writefile_mmRNA_Paired = pysam.AlignmentFile("DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_Paired.bam", "wb", template=smallsamfile)                







