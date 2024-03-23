import os
import argparse

arg = argparse.ArgumentParser()
arg.add_argument("--vcf", help="VCF file name")
arg.add_argument("--filter", help="Text argument for using with filter")
arg.add_argument("--out", help="Output VCF file name")
args = arg.parse_args()
# print(os.listdir())

def vcf_filter(infile,outfile,filton):
    """Filters a VCF file with the filtering option in the Info column alone
        infile : input vcf file
        outfile : output vcf file
        filton : term to filter in the INFO field
        start : starting for the header"""
    vcf_in = open(infile,'r',encoding='utf-8',newline='\n')
    vcf_out = open(outfile, 'w',encoding='utf-8',newline='\n')
    vcf_data = [i for i in vcf_in.readlines() if i.startswith("#") is False]#
    vcf_header = [i for i in vcf_in.readlines() if i.startswith("#") is True]
    for i in vcf_header:
        vcf_out.write(i)
    for j in vcf_data:
        vcf_ann = j.split("\t")[7]
        if filton not in vcf_ann:
            print(j)
            vcf_out.write(j)

    vcf_in.close()
    vcf_out.close()

def main():
    vcf_filter(infile=args.vcf,outfile=args.out,filton=args.filter)

if __name__ == "__main__":
    main()