#!/bin/bash

folderToCD="/data1_1/Sequencing1_1/Madrasin_HiSeq_October2018" 

#datafolder="/home/jkumar12/Projects/Analyzing_SHAPEdata_In_Introns/data"

#folderToWriteTo="/home/jkumar12/Projects/ExonIntronBoundaryStructures/tmp/Madrasin_HiSeq_October2018_alignments"

cd ${folderToCD}
#pwd
for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    
    echo "unzipping fastq files..."
    #gzip -d ${file}_L006_R*_001.fastq.gz
    
    echo "run fastqc..."
    #fastqc ${file}_L006_R*_001.fastq
    # Move fastqc files into fastqc folder 
    mv ${file}_L006_R*_001_fastqc* fastqc_files
    
    echo "zipping fastq files..."
    gzip ${file}_L006_R*_001.fastq
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts
