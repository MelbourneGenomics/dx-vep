# Set the python path to the src directory
import sys
sys.path.append('../src')

from paths import *
import os
from doit.tools import create_folder
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
        # Make two temporary dirs, one for the whole ensembl suite, one for just VEP
        unpack_into("https://codeload.github.com/Ensembl/ensembl-vep/tar.gz/{}".format(VEP_VERSION), VEP_ROOT)
        BIN.mkdir(parents=True, exist_ok=True)
        os.symlink(VEP_BIN, BIN / 'vep')

    return {
        'actions': [action],
        'uptodate': [True],
        'targets': [BIN / 'vep']
    }


def task_download_vep_libs():
    def action():
        sh(f'''
            perl {VEP_ROOT / "INSTALL.pl"}
                --AUTO acp
                --NO_HTSLIB
                --SPECIES homo_sapiens_refseq homo_sapiens_merged homo_sapiens
                --ASSEMBLY GRCh37
                --PLUGINS all \
                --CACHEDIR {VEP_CACHE}
            ''', cwd=ROOT)

    return {
        'task_dep': ['download_vep'],
        'actions': [action],
        'uptodate': [False]
    }


def task_download_vep_plugins():
    def action():
        PLUGIN_ROOT.mkdir()
        sh(f'''
            git init
            git remote add origin https://github.com/Ensembl/VEP_plugins
            git fetch
            git checkout -t origin/master
            git reset --hard {VEP_PLUGIN_COMMIT}
            rm -rf .git
        ''', cwd=PLUGIN_ROOT)

    return {
        'actions': [action],
        'targets': [PLUGIN_ROOT],
        'uptodate': [True]
    }


def task_install_vep_cache():
    targets = [VEP_CACHE]
    return {
        'targets': targets,
        'actions': [
            lambda: create_folder(VEP_CACHE),
            f'''perl {VEP_ROOT / "INSTALL.pl"}\
            --AUTO cf\
            --SPECIES homo_sapiens_refseq\
            --ASSEMBLY GRCh37'''
        ],
        'uptodate': [False],
    }
