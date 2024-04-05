import os
import argparse
import vcfpy

arg = argparse.ArgumentParser()
arg.add_argument("--vcf", help="VCF file name")
arg.add_argument("--filter", help="Text argument for using with filter")
arg.add_argument("--out", help="Output VCF file name")
args = arg.parse_args()

def vcfFilter(infile="./sample.vcf",outfile="./test.vcf",filton="synonymous_variant"):
    """Filters a VCF file with the filtering option in the Info column alone
        infile : input vcf file
        outfile : output vcf file
        filton : term to filter in the INFO field
        start : starting for the header"""
    
    reader = vcfpy.Reader.from_path(infile)
    writer = vcfpy.Writer.from_path(outfile, reader.header)
    for rec in reader:
        outann = []
        # print(rec.INFO)
        for annotations in rec.INFO["ANN"]:
            annData = annotations.split("|")
            if filton in annData:
                # print(annotations)
                annData = ""
            else:
                outann.append("|".join(annData))
        rec.INFO["ANN"] = outann
        writer.write_record(rec)
        #         outann.append(annotations)
        # vcfpy.write_record(rec)

def main():
    vcfFilter(infile=args.vcf, outfile=args.out, filton=args.filter)

if __name__ == "__main__":
    main()
