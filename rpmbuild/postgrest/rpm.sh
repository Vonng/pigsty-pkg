#!/bin/bash

ssh meta 'mkdir -p rpmbuild/{SOURCES,SPECS}'
scp ../dist/postgrest/postgrest-v9.0.0-linux-static-x64.tar.xz meta:~/rpmbuild/SOURCES/
scp postgrest.service meta:~/rpmbuild/SOURCES/
scp postgrest.conf meta:~/rpmbuild/SOURCES/
scp postgrest.spec meta:~/rpmbuild/SPECS/postgrest.spec

ssh meta rpmbuild -bb /home/vagrant/rpmbuild/SPECS/postgrest.spec
scp meta:~/rpmbuild/RPMS/x86_64/postgrest-9.0.0-1.el7.x86_64.rpm ../dist/postgrest/
