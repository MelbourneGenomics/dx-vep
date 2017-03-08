#!/usr/bin/env bash
set -e -x -o pipefail


#
# Fetch inputs (~/in/vcfgz/*)
#
dx-download-all-inputs --parallel

# Run Variant Effect Predictor
perl /vep/vep/vep.pl -i ./in/vcfgz/* --cache --dir /vep --offline --vcf -o ./out/annotated_vcf/out.vcf --everything --no_stats --fork `nproc`

#vcf-sort < output.vcf > output.sorted.vcf
#
#bgzip output.sorted.vcf
#tabix -p vcf output.sorted.vcf.gz
#
##
## Upload results
##
#mkdir -p ~/out/vcfgz/ ~/out/tbi/
#mv output.sorted.vcf.gz ~/out/vcfgz/"$vcfgz_prefix".annotated.vcf.gz
#mv output.sorted.vcf.gz.tbi ~/out/tbi/"$vcfgz_prefix".annotated.vcf.gz.tbi
dx-upload-all-outputs --parallel
