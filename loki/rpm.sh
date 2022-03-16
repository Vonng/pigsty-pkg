#!/bin/bash

ssh meta 'mkdir -p rpmbuild/{SOURCES,SPECS}'
scp ../dist/loki/loki-linux-amd64.zip meta:~/rpmbuild/SOURCES/
scp ../dist/loki/loki-canary-linux-amd64.zip meta:~/rpmbuild/SOURCES/
scp ../dist/loki/logcli-linux-amd64.zip meta:~/rpmbuild/SOURCES/

scp loki.service meta:~/rpmbuild/SOURCES/
scp loki.yml meta:~/rpmbuild/SOURCES/
scp loki.spec meta:~/rpmbuild/SPECS/loki.spec
ssh meta rpmbuild -bb /home/vagrant/rpmbuild/SPECS/loki.spec
scp meta:~/rpmbuild/RPMS/x86_64/loki-2.4.2-1.el7.x86_64.rpm ../dist/loki/