#!/bin/bash

folderToCD="/data1/Madrasin_HiSeq_October2018/NexteraAdaptersTrimmedFastQFiles"

indexfolder="/home/shared/GenomeReferences/bowtie2_index_hg38"

folderToWriteTo="/data1/Madrasin_HiSeq_October2018/AlignmentFiles_Bowtie2_ShapeMapper2Parms"


cd ${folderToCD}
#pwd
for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    
    echo "aligning Nextera Adapter Trimmed FastQ files....."
    # The command below is the ShapeMapper 2 alignment parameters
    bowtie2 -p 12 --local --sensitive-local --mp 3,1 --rdg 5,1 --rfg 5,1 --dpad 30 --maxins 800 --ignore-quals -x ${indexfolder}/hg38 -1 ${file}_L006_R1_001_val_1.fq.gz -2 ${file}_L006_R2_001_val_2.fq.gz -S ${folderToWriteTo}/${file}.sam > ${folderToWriteTo}/${file}.log
    
    echo "converting SAM to BAM........"
    samtools view -b -o ${folderToWriteTo}/${file}.bam ${folderToWriteTo}/${file}.sam
    
    echo "Get header file separately from SAM file........."
    samtools view -h -o ${folderToWriteTo}/${file}_Header.sam ${folderToWriteTo}/${file}.sam
    
    echo "Remove SAM file..........."
    rm ${folderToWriteTo}/${file}.sam
    #echo "Get unaligned reads....."
    #samtools view -b -f 4 -o ${folderToWriteTo}/${file}_UnalignedReads.bam ${folderToWriteTo}/${file}.bam
    #bedtools bamtofastq -i ${folderToWriteTo}/${file}_UnalignedReads.bam -fq ${folderToWriteTo}/${file}_UnalignedReads.fastq
    
    echo "Get aligned reads....." 
    samtools view -b -F 4 -o ${folderToWriteTo}/${file}_AlignedReads.bam ${folderToWriteTo}/${file}.bam
    #bedtools bamtofastq -i ${folderToWriteTo}/${file}_AlignedReads.bam -fq ${folderToWriteTo}/${file}_AlignedReads.fastq
    
    echo "Obtain reads with MAPQ greater than 10"
    samtools view -b -q 10 -o ${folderToWriteTo}/${file}_MAPQgreaterThan10.bam ${folderToWriteTo}/${file}.bam
    
    echo "sorting and index BAM........"
    samtools sort -@ 4 -o ${folderToWriteTo}/${file}_MAPQgreaterThan10_SortedByCoords.bam ${folderToWriteTo}/${file}_MAPQgreaterThan10.bam

    samtools index ${folderToWriteTo}/${file}_MAPQgreaterThan10_SortedByCoords.bam
    
    echo "Remove non sorted BAM file with MAPQ greater than 10"
    rm ${folderToWriteTo}/${file}_MAPQgreaterThan10.bam
    
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts