Tool to filter VCF files using INFO field

Dependencies:
Tested using Python 3.10
vcfpy = 0.13.8 (https://pypi.org/project/vcfpy/)

#sample command
python3 filterVCF.py --vcf sample.vcf --filter synonymous_variant --out test_new.vcf
