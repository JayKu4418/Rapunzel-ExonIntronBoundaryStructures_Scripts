#!/bin/bash

folderToCD="/home/jkumar12/Projects/ExonIntronBoundaryStructures/tmp/Madrasin_HiSeq_October2018_alignments"

cd ${folderToCD}

for file in "DMSTreatedSample_TAGGCATG_S1" "NoDMSSample_CTCTCTAC_S2";
do
    echo ${file}
    
    echo "getting proper pairs........"
    # Get proper pairs 
    samtools view -b -f 2 -o ${file}_MAPQgreaterThan10_ProperPairs.bam ${file}_MAPQgreaterThan10.bam
    
    echo "sorting proper pairs........"
    # Sort proper pairs
    samtools sort -o ${file}_MAPQgreaterThan10_ProperPairs_SortedByCoords.bam ${file}_MAPQgreaterThan10_ProperPairs.bam
    
    echo "get fragment length distribution........"
    # Get fragment length distribution using Picard tools
    java -jar $PICARD CollectInsertSizeMetrics I=${file}_MAPQgreaterThan10_ProperPairs_SortedByCoords.bam O=${file}_MAPQgreaterThan10_ProperPairs_insert_size_metrics.txt H=${file}_MAPQgreaterThan10_ProperPairs_insert_size_histogram.pdf M=0.5
done

cd /home/jkumar12/Projects/ExonIntronBoundaryStructures/scripts