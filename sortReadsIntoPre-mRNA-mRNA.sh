#!/bin/bash

# This is specifically for the region in NFKBIA, NM_020529.2, NM_020529.2_2, chr14:35402671-35402770

# Get header for samfile 
samtools view -H -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_JustHeader.sam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam

# Get reads overlapping intron chr14:35,402,671-35,402,770
samtools view -b -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402770_JustIntron.bam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam chr14:35402671-35402770
samtools index DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402770_JustIntron.bam

# Get reads overlapping exon chr14:35402771-35402859
samtools view -b -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402771-35402859_JustExon.bam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam chr14:35402771-35402859
samtools index DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402771-35402859_JustExon.bam

# Get rid of reads that are in the exon set but that are also found in the intron set -> these are one set of pre-cursor mRNAs
samtools view DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402770_JustIntron.bam | sort > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402671-35402770_JustIntron_Sorted.sam
samtools view DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402771-35402859_JustExon.bam | sort > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustExon_Sorted.sam
comm -13 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402671-35402770_JustIntron_Sorted.sam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustExon_Sorted.sam > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustReadsInExonNotIntron.sam
cat DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_JustHeader.sam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustReadsInExonNotIntron.sam > DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustReadsInExonNotIntron_WithHeader.sam
samtools view -u DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustReadsInExonNotIntron_WithHeader.sam | samtools sort -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustReadsInExonNotIntron.bam
samtools index DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_chr14-35402771-35402859_JustReadsInExonNotIntron.bam


while read line;
do
    #if [ ${line:0:1} != '@' ]
    if 
    then
        #echo ${line}
        A="$(cut -f5 <<<"$line")"
        echo ${A} >> ${mapqFileToWrite}
        #cut -f5 $line >> ${mapqFileToWrite}
    fi
done < ${samFileToExtract}

# Above steps were not successful
# Maybe key is to get all reads spanning the intron exon junction and split it up from there by looking at each read. I could use pysam to do this
# Get reads overlapping intron chr14:35,402,671-35,402,770 and exon chr14:35402771-35402859
samtools view -b -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam ../DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords.bam chr14:35402671-35402859
samtools index DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam
samtools view -o DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.sam DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam


samtools view -b -o NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam ../NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords.bam chr14:35402671-35402859
samtools index NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam
samtools view -o NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.sam NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859.bam