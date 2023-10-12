all: push pull build

push:
	ssh build-el9 'mkdir -p /tmp/rpm'
	rsync -avc --delete /data/rpm/ build-el9:/tmp/rpm/

pull:
	rsync -avc --delete build-el9:/tmp/rpm/ /data/rpm/

build:
	ssh build-el9 'cd /tmp/rpm/infra/x86_64      && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/infra/aarch64     && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/pgsql/el8.x86_64  && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/pgsql/el9.x86_64  && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/redis/el7.x86_64  && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/redis/el8.x86_64  && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/redis/el9.x86_64  && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/minio/x86_64  && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'
	ssh build-el9 'cd /tmp/rpm/minio/aarch64 && createrepo_c . && repo2module -s stable . modules.yaml && modifyrepo_c --mdtype=modules modules.yaml repodata/'

.PHONY: push pull build