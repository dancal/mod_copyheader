mod_copyheader.la: mod_copyheader.slo
	$(SH_LINK) -rpath $(libexecdir) -module -avoid-version  mod_copyheader.lo
DISTCLEAN_TARGETS = modules.mk
shared =  mod_copyheader.la
