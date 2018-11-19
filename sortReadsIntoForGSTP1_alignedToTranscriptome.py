import pysam
import sys

sampleName = sys.argv[1]

# Read files
samfile_genome = pysam.AlignmentFile(sampleName+"_AlignedToGSTP1_genome_MAPQgreaterThan10_SortedByCoords.bam","rb")
samfile_transcriptome = pysam.AlignmentFile(sampleName+"_AlignedToGSTP1_transcriptome_MAPQgreaterThan10_SortedByCoords.bam","rb")

# Write files
writefile_PremRNA = pysam.AlignmentFile(sampleName+"_AlignedToGSTP1_MAPQgreaterThan10_SortedByCoords_PremRNA.bam", "wb", template=samfile_genome)
writefile_mmRNA = pysam.AlignmentFile(sampleName+"_AlignedToGSTP1_MAPQgreaterThan10_SortedByCoords_MaturemRNA.bam", "wb", template=samfile_transcriptome)
writefile_ambRNA_genome = pysam.AlignmentFile(sampleName+"_AlignedToGSTP1_MAPQgreaterThan10_SortedByCoords_ambiguous_Genome.bam", "wb", template=samfile_genome)
writefile_ambRNA_transcriptome = pysam.AlignmentFile(sampleName+"_AlignedToGSTP1_MAPQgreaterThan10_SortedByCoords_ambiguous_Transcriptome.bam", "wb", template=samfile_transcriptome)

readNames_genome = list(set([read.query_name for read in samfile_genome.fetch()]))
print(len(readNames_genome))
readNames_transcriptome = list(set([read.query_name for read in samfile_transcriptome.fetch()]))
print(len(readNames_transcriptome))
commonreadNames = list(set(readNames_genome).intersection(readNames_transcriptome))
print len(commonreadNames)
print commonreadNames[0:5]

# Get all exon and intron locations in genome fasta
with open("genes_genome.bed") as f:
    alllines = [line.strip().split("\t") for line in f]
onlyexons_genome = [[int(i[1]),int(i[2])] for i in alllines if "Exon" in i[3]]
onlyintrons=[]
for i in alllines:
    onlyintrons.extend(range(int(i[1]),int(i[2])-1))
#onlyintrons = [[int(i[1]),int(i[2])] for i in alllines if "Intron" in i[3]]

readsInGenome = [i for i in samfile_genome.fetch()]
print(len(readsInGenome))
definitely_premRNA = []
possibly_maturemRNA = []
ambiguous_readToCheck_genome = []
# Go through every readName in genome alignment
for read_name in readNames_genome:
    # Get read pairs for read names
    read_pairs = [i for i in readsInGenome if i.query_name==read_name]
    # If there are read pairs for the read names then continue, else check if read name is in transcriptome ambiguous list
    if len(read_pairs)==2:
        # If the read name is not found in readNames aligned to transcriptome. then read is a premature mRNA, else further investigate
        if read_name not in readNames_transcriptome:
            writefile_PremRNA.write(read_pairs[0])
            writefile_PremRNA.write(read_pairs[1])
            definitely_premRNA.append(read_name)
        else:
            # Check if any of the read positions are in introns for the read pair
            positions_Read1 = read_pairs[0].get_reference_positions()
            introns_Read1 = [i for i in positions_Read1 if i in onlyintrons]
            positions_Read2 = read_pairs[1].get_reference_positions()
            introns_Read2 = [i for i in positions_Read2 if i in onlyintrons]
            if len(introns_Read1)!=0 or len(introns_Read2)!=0:
                writefile_PremRNA.write(read_pairs[0])
                writefile_PremRNA.write(read_pairs[1])
                definitely_premRNA.append(read_name)
            else:
                possibly_maturemRNA.append(read_name)
    # For read which does not have a pair
    else:
        # first that it is not found in transcriptome read names , if it is not immediately write to ambiguous file
        if read_name not in readNames_transcriptome:
            writefile_ambRNA_genome.write(read_pairs[0])
        # If it is found in the transcriptome read names list
        else:
            ambiguous_readToCheck_genome.append(read_name)

            
print(len(definitely_premRNA))
print(len(possibly_maturemRNA))
print(len(ambiguous_readToCheck_genome))


# Get all exon locations in transcriptome fasta
with open("genes_transcriptome.bed") as f:
    alllines = [line.strip().split("\t") for line in f]
onlyexons_transcriptome = [[int(i[1]),int(i[2])] for i in alllines if "exon" in i[3]]

readsInTranscriptome = [i for i in samfile_transcriptome.fetch()]
print(len(readsInTranscriptome))
writeReadFromGenomeFile = []
# Go through every read name in transcriptome alignment
for read_name in readNames_transcriptome:
    # Get read pairs for read names
    read_pairs = [i for i in readsInTranscriptome if i.query_name==read_name]
    # If there are read pairs for the read names then continue, else append read name to ambiguous read in transcriptome
    if len(read_pairs)==2:
        # If the read name is not found in readNames aligned to genome. then read is a mature mRNA, else further investigate
        if read_name not in readNames_genome:
            writefile_mmRNA.write(read_pairs[0])
            writefile_mmRNA.write(read_pairs[1])
        elif read_name not in definitely_premRNA:
            # If read pairs are both entirely in exons, then ambiguous read
            positions_Read1 = read_pairs[0].get_reference_positions()
            # Read1 in exons?
            # Go through every exon, and check if positions of read intersect entirely with positions of exon
            exons_Read1 = [i for i in onlyexons_transcriptome if len(set(positions_Read1).intersection(set(range(i[0],i[1]-1))))==len(set(positions_Read1))]
            positions_Read2 = read_pairs[0].get_reference_positions()
            exons_Read2 = [i for i in onlyexons_transcriptome if len(set(positions_Read2).intersection(set(range(i[0],i[1]-1))))==len(set(positions_Read2))]
            # If both reads are entirely within exons, then this is an ambiguous read, else further investigate
            if len(exons_Read1)==1 and len(exons_Read2)==1:
                writefile_ambRNA_transcriptome.write(read_pairs[0])
                writefile_ambRNA_transcriptome.write(read_pairs[1])
            else:
                writefile_mmRNA.write(read_pairs[0])
                writefile_mmRNA.write(read_pairs[1])
            if read_name in possibly_maturemRNA:
                possibly_maturemRNA.remove(read_name)
            if read_name in ambiguous_readToCheck_genome:
                ambiguous_readToCheck_genome.remove(read_name)
    else:
        # Check if solo read in transcriptome is not in readNames_genome, if so then write to ambiguous file
        if read_name not in readNames_genome:
            writefile_ambRNA_transcriptome.write(read_pairs[0])
        elif read_name in ambiguous_readToCheck_genome:
            writefile_ambRNA_transcriptome.write(read_pairs[0])
            ambiguous_readToCheck_genome.remove(read_name)
        elif read_name in possibly_maturemRNA:
            possibly_maturemRNA.remove(read_name)
            writeReadFromGenomeFile.append(read_name)
            
print(len(definitely_premRNA))
print(len(possibly_maturemRNA))
print(len(ambiguous_readToCheck_genome))
print(len(writeReadFromGenomeFile))