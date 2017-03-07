from paths import *
import os
from subprocess import check_output
from python_assets import unpack_into

DOIT_CONFIG = {'default_tasks': ['vep']}


def sh(args, **kwargs):
    shell = True if isinstance(args, str) else False
    return check_output(args, shell=shell, **kwargs)


def task_vep():
    return {
        'actions': None,
        'task_dep': ['download_vep', 'download_vep_libs']
    }


def task_download_vep():
    def action():
        # Make two teporary dirs, one for the whole ensembl suite, one for just VEP
        unpack_into("https://codeload.github.com/Ensembl/ensembl-vep/tar.gz/release/{}".format(VEP_VERSION), VEP_ROOT, compression='gz', archive='tar')
        BIN.mkdir(parents=True, exist_ok=True)
        os.symlink(VEP_BIN, BIN / 'vep')

    return {
        'actions': [action],
        'uptodate': [True],
        'targets': [BIN / 'vep']
    }


def task_download_vep_libs():
    def action():
        sh('''
            perl {install}\
                --AUTO acpl\
                --NO_HTSLIB\
                --SPECIES homo_sapiens_refseq homo_sapiens_merged homo_sapiens\
                --ASSEMBLY GRCh37\
                --PLUGINS all \
                --CACHEDIR {cache}
            '''.format(install=VEP_ROOT / "INSTALL.pl", cache=VEP_CACHE), cwd=ROOT)

    return {
        'task_dep': ['download_vep'],
        'actions': [action],
        'uptodate': [False]
    }
