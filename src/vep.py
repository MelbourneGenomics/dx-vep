#!/usr/bin/env python

from pathlib2 import Path
import dxpy
import subprocess


@dxpy.entry_point('main')
def main(vcf, reference_fasta, variant_class, sift):
    # Paths
    outputs = Path('outputs/')
    output_vcf = outputs / 'output.vcf'
    output_stats = outputs / 'report.html'

    inputs = Path('inputs/')
    input_vcf = inputs / 'input.vcf'
    input_fasta = inputs / 'reference.fasta'

    # Input files
    vcf = dxpy.DXFile(vcf)
    dxpy.download_dxfile(vcf.get_id(), str(input_vcf))

    reference_fasta = dxpy.DXFile(reference_fasta)
    dxpy.download_dxfile(reference_fasta.get_id(), str(input_fasta))

    # Install HTSLib
    subprocess.check_call('perl INSTALL.pl --AUTO a')

    # Run VEP
    args = ['vep',
            '--species', 'homo_sapiens',
            '--input_file', str(input_vcf),
            '--output_file', str(output_vcf),
            '--stats_file', str(output_stats),
            '--cache',
            '--offline',
            '--fasta',
            '--vcf'
            ]

    # Handle optional parameters
    if variant_class:
        args.append('--variant_class')
    if sift:
        args.extend(['--sift', sift])

    subprocess.check_call(args)

    # Outputs
    annotated_vcf = dxpy.upload_local_file("annotated_vcf")
    return {"annotated_vcf": dxpy.dxlink(annotated_vcf)}


dxpy.run()
