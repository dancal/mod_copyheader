ABSTRACT
================

mod_copyheader is Apache 2.2 module for copy response header to note

INSTALLATION
================

download from http://github.com/dancal/mod_copyheader

    # rpmbuild -ba mod_copyheader.spec 
	

DOCUMENTATION
================

    Description: Enable CopyHeader module
    Syntax:      CopyHeaderActive on/off
    Context:     dir config
    Module:      mod_copyheader

    Description: set a header name to copy to note
    Syntax:      CopyHeader header
    Context:     dir config
    Module:      mod_bumpy_life

Example
----------------
	/etc/httpd/conf/httpd.conf

	LogFormat "... \"%{WPLogResult}n\"" combined

	<?php
		#아파치 로그에는 결과가 저장되지만, 사용자 브라우져로는 전송되지 않는다.
		header("WPLogResult: test");
	?>

	
COPYRIGHT & LICENSE
================

Copyright 2012 Masahiro Nagano

Apache License, Version 2.0

CHANGES
================
add mod_copyheader.conf - 2013.04.08 dancal
add rpmbuild spec - 2013.04.08 dancal
