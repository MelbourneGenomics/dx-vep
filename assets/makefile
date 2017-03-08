VEP_VERSION = 87.26
ROOT = /vep
VEP = $(ROOT)/vep
API = $(ROOT)/Bio
INSTALL = $(VEP)/INSTALL.pl

vep_deps: $(INSTALL) perl_deps
	cd $(VEP) && perl $(VEP)/INSTALL.pl\
		--AUTO ap\
		--SPECIES homo_sapiens_refseq homo_sapiens_merged homo_sapiens\
		--ASSEMBLY GRCh38\
		--PLUGINS all

clean:
	rm -rf $(VEP) $(API)

$(INSTALL):
	git clone https://github.com/Ensembl/ensembl-vep --branch release/$(VEP_VERSION) $(VEP)

perl_deps:
	sudo cpanm --installdeps --force ~

.PHONY: vep_deps clean perl_deps

