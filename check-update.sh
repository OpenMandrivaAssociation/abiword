#!/bin/sh
curl "http://www.abisource.com/downloads/abiword/" 2>/dev/null |sed -ne 's,.*>\([0-9]\)\.\([0-9]\)\.\([0-9]\)\/<.*,\1.\2.\3,p' |sort -hr |head -n1

