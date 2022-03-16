#!/bin/bash

ssh meta 'mkdir -p rpmbuild/{SOURCES,SPECS}'
scp ../dist/loki/promtail-linux-amd64.zip meta:~/rpmbuild/SOURCES/
scp promtail.service meta:~/rpmbuild/SOURCES/
scp promtail.yml meta:~/rpmbuild/SOURCES/
scp promtail.spec meta:~/rpmbuild/SPECS/promtail.spec
ssh meta rpmbuild -bb /home/vagrant/rpmbuild/SPECS/promtail.spec
scp meta:~/rpmbuild/RPMS/x86_64/promtail-2.4.2-1.el7.x86_64.rpm ../dist/loki/