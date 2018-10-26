#!/bin/bash

# This script is going to get featureCounts using STAR alignment

folderToCD="/data1/Madrasin_HiSeq_October2018/AlignmentFiles_Bowtie2_ShapeMapper2Parms"

writeFolder="/home/jkumar12/Projects/ExonIntronBoundaryStructures/tmp/Madrasin_HiSeq_October2018_alignments"

dataFolder="/home/jkumar12/Projects/ExonIntronBoundaryStructures/data"

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
elif [ "$1" = "Intron5p" ]
then
    annotationFile="SAFformat_ExtractedIntronCoordinatesFromGFFfile_5p_OnlyTranscriptIDs.bed"
elif [ "$1" = "Intron3p" ]
then
    annotationFile="SAFformat_ExtractedIntronCoordinatesFromGFFfile_3p_OnlyTranscriptIDs.bed"
fi

cd ${folderToCD}
for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    featureCounts -p --largestOverlap -B -C -M -R SAM -t exon -g gene_id -a ${dataFolder}/${annotationFile} -F SAF -o ${writeFolder}/${file}_${1}_featureCounts.txt ${file}_MAPQgreaterThan10_SortedByCoords.bam
    cut -f1,6,7 ${writeFolder}/${file}_${1}_featureCounts.txt > ${writeFolder}/${file}_${1}_featureCounts_JustCounts.txt
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts