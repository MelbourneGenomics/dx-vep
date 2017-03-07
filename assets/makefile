VEP_VERSION = 87.26
ROOT = /vep
VEP = $(ROOT)/vep
API = $(ROOT)/Bio
INSTALL = $(VEP)/INSTALL.pl

install_deps: $(INSTALL)
	cd $(ROOT) && perl $(VEP)/INSTALL.pl\
		--AUTO apl\
		--NO_HTSLIB\
		--SPECIES homo_sapiens_refseq homo_sapiens_merged homo_sapiens\
		--ASSEMBLY GRCh38\
		--PLUGINS all\

clean:
	rm -rf $(VEP) $(API)

$(INSTALL):
	mkdir -p $(VEP)
	curl 'https://codeload.github.com/Ensembl/ensembl-vep/tar.gz/release/$(VEP_VERSION)' | tar --strip-components 1 -xz -C $(VEP)

.PHONY: install_deps clean

