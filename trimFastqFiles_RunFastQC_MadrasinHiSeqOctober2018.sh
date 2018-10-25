#!/bin/bash

folderToCD="/data1_1/Sequencing1_1/Madrasin_HiSeq_October2018" 

outputfolder="/data1_1/Sequencing1_1/Madrasin_HiSeq_October2018/NexteraAdaptersTrimmedFastQFiles"

#datafolder="/home/jkumar12/Projects/Analyzing_SHAPEdata_In_Introns/data"

#folderToWriteTo="/home/jkumar12/Projects/ExonIntronBoundaryStructures/tmp/Madrasin_HiSeq_October2018_alignments"

cd ${folderToCD}
#pwd
for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    
    echo "run trim_galore"
    trim_galore --phred33 --paired --output_dir ${outputfolder} --nextera --fastqc ${file}_L006_R1_001.fastq.gz ${file}_L006_R2_001.fastq.gz
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts
