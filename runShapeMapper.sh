#!/bin/bash





#shapemapper --target NFKBIA_NM_020529.fa --out NFKBIA_NM_020529_SHAPE_Pre_mRNA/ --modified --R1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R1.fastq --R2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R2.fastq --untreated --R1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R1.fastq  --R2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_PremRNA_R2.fastq  --overwrite --min-depth 500 --nproc 8

#shapemapper --target NFKBIA_NM_020529.fa --out NFKBIA_NM_020529_SHAPE_Mature_mRNA/ --modified --R1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R1.fastq --R2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R2.fastq --untreated --R1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R1.fastq  --R2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr14-35402671-35402859_MaturemRNA_R2.fastq  --overwrite --min-depth 100 --nproc 8

#shapemapper --target RPL10_NM_001256580.fa --out RPL10_NM_001256580_SHAPE_Pre_mRNA/ --modified --R1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R1.fastq --R2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R2.fastq --untreated --R1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R1.fastq  --R2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chrX-154399297-154399496_PremRNA_R2.fastq  --overwrite --min-depth 500 --nproc 8

shapemapper --target GSTP1_NM_000852.fa --out GSTP1_NM_000852_SHAPE_Pre_mRNA/ --modified --R1 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr11-67584470-67584670_PremRNA_R1.fastq --R2 DMSTreatedSample_TAGGCATG_S1_MAPQgreaterThan10_SortedByCoords_chr11-67584470-67584670_PremRNA_R2.fastq --untreated --R1 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr11-67584470-67584670_PremRNA_R1.fastq  --R2 NoDMSSample_CTCTCTAC_S2_MAPQgreaterThan10_SortedByCoords_chr11-67584470-67584670_PremRNA_R2.fastq  --overwrite --min-depth 100 --nproc 8