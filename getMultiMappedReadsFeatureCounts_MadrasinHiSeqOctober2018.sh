#!/bin/bash

# This script is going to get featureCounts using STAR alignment

folderToCD="/data1/Madrasin_HiSeq_October2018/AlignmentFiles_Bowtie2_ShapeMapper2Parms"

dataFolder="/home/jkumar12/Projects/ExonIntronBoundaryStructures/data"

writeFolder="/home/jkumar12/Projects/ExonIntronBoundaryStructures/tmp/Madrasin_HiSeq_October2018_alignments"

if [ "$1" = "Transcriptome" ]
then
    annotationFile="SAFformat_GRCh38_latest_genomic_ValidChroms_OnlyGenes.bed"
elif [ "$1" = "Genome" ]
then
    annotationFile="SAFformat_ExtractedGenomicCoordinatesFromGFFfile_OnlyGenes.bed"
elif [ "$1" = "ExonIntron5p" ]
then
    annotationFile="SAFformat_ExtractedExonIntronCoordinatesFromGFFfile_5p_OnlyGenes.bed"
elif [ "$1" = "ExonIntron3p" ]
then
    annotationFile="SAFformat_ExtractedExonIntronCoordinatesFromGFFfile_3p_OnlyGenes.bed"
fi

cd ${folderToCD}

for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    # Get multi mapped reads and single mapped reads 
    samtools view -F 4 ${file}.bam | grep XS:i > ${file}_MultiMappedReads.sam
    samtools view -F 4 ${file}.bam | grep -v XS:i > ${file}_SingleMappedReads.sam
    # Concatenate Header file with multimapped reads and get bam file
    cat ${file}_Header.sam ${file}_MultiMappedReads.sam > ${file}_MultiMappedReadsPlusHeader.sam
    samtools view -b -o ${file}_MultiMappedReads.bam ${file}_MultiMappedReadsPlusHeader.sam
    # Remove sam files for multimapped reads
    rm ${file}_MultiMappedReads.sam
    rm ${file}_MultiMappedReadsPlusHeader.sam
    # Concatenate Header file with single mapped reads and get bam file
    cat ${file}_Header.sam ${file}_SingleMappedReads.sam > ${file}_SingleMappedReadsPlusHeader.sam
    samtools view -b -o ${file}_SingleMappedReads.bam ${file}_SingleMappedReadsPlusHeader.sam
    # Remove sam files for singlemapped reads
    rm ${file}_SingleMappedReads.sam
    rm ${file}_SingleMappedReadsPlusHeader.sam
    
    featureCounts -p --largestOverlap -B -C -M -R SAM -t exon -g gene_id -a ${dataFolder}/${annotationFile} -F SAF -o ${writeFolder}/${file}_${1}_featureCounts_SingleMappedReads.txt ${file}_SingleMappedReads.bam
    cut -f1,6,7 ${writeFolder}/${file}_${1}_featureCounts_SingleMappedReads.txt > ${writeFolder}/${file}_${1}_featureCounts_SingleMappedReads_JustCounts.txt
    
    featureCounts -p --largestOverlap -B -C -M -R SAM -t exon -g gene_id -a ${dataFolder}/${annotationFile} -F SAF -o ${writeFolder}/${file}_${1}_featureCounts_MultiMappedReads.txt ${file}_MultiMappedReads.bam
    cut -f1,6,7 ${writeFolder}/${file}_${1}_featureCounts_MultiMappedReads.txt > ${writeFolder}/${file}_${1}_featureCounts_MultiMappedReads_JustCounts.txt
    
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts