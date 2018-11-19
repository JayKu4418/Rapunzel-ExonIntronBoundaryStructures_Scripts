#!/bin/bash

whichType=$1

fastqFolder="/data1/Madrasin_HiSeq_October2018/NexteraAdaptersTrimmedFastQFiles"

indexfolder="/home/jkumar12/Projects/ExonIntronBoundaryStructures/data"

folderToCD="/data1/Madrasin_HiSeq_October2018/AlignmentFiles_Bowtie2_ShapeMapper2Parms/GSTP1_GenomeVsTranscriptome"

cd ${folderToCD}
#pwd
#for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
for file in "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    
    echo "aligning Nextera Adapter Trimmed FastQ files to GSTP1....."
    # The command below is the ShapeMapper 2 alignment parameters
    bowtie2 -p 12 --local --sensitive-local --mp 3,1 --rdg 5,1 --rfg 5,1 --dpad 30 --maxins 800 --ignore-quals -x ${indexfolder}/GSTP1_${whichType}/GSTP1_${whichType} -1 ${fastqFolder}/${file}_L006_R1_001_val_1.fq.gz -2 ${fastqFolder}/${file}_L006_R2_001_val_2.fq.gz -S ${file}_AlignedToGSTP1_${whichType}.sam > ${file}_AlignedToGSTP1_${whichType}.log
    
    echo "converting SAM to BAM........"
    samtools view -b -o ${file}_AlignedToGSTP1_${whichType}.bam ${file}_AlignedToGSTP1_${whichType}.sam
    
    echo "Get header file separately from SAM file........."
    samtools view -H -o ${file}_AlignedToGSTP1_${whichType}_Header.sam ${file}_AlignedToGSTP1_${whichType}.sam
    
    echo "Remove SAM file..........."
    rm ${file}_AlignedToGSTP1_${whichType}.sam
    #echo "Get unaligned reads....."
    #samtools view -b -f 4 -o ${folderToWriteTo}/${file}_UnalignedReads.bam ${folderToWriteTo}/${file}.bam
    #bedtools bamtofastq -i ${folderToWriteTo}/${file}_UnalignedReads.bam -fq ${folderToWriteTo}/${file}_UnalignedReads.fastq
    
    #echo "Get aligned reads....." 
    #samtools view -b -F 4 -o ${file}_AlignedToGSTP1_${whichType}_AlignedReads.bam ${file}_AlignedToGSTP1_${whichType}.bam
    #bedtools bamtofastq -i ${folderToWriteTo}/${file}_AlignedReads.bam -fq ${folderToWriteTo}/${file}_AlignedReads.fastq
    
    echo "Obtain reads with MAPQ greater than 10"
    samtools view -b -q 10 -o ${file}_AlignedToGSTP1_${whichType}_MAPQgreaterThan10.bam ${file}_AlignedToGSTP1_${whichType}.bam
    
    echo "sorting and index BAM........"
    samtools sort -@ 4 -o ${file}_AlignedToGSTP1_${whichType}_MAPQgreaterThan10_SortedByCoords.bam ${file}_AlignedToGSTP1_${whichType}_MAPQgreaterThan10.bam

    samtools index ${file}_AlignedToGSTP1_${whichType}_MAPQgreaterThan10_SortedByCoords.bam
    
    echo "Remove non sorted BAM file with MAPQ greater than 10"
    rm ${file}_AlignedToGSTP1_${whichType}_MAPQgreaterThan10.bam
    
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts