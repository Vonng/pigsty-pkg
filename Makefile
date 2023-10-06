#---------------------------------------------#
# push/pull changes with development server sv
#---------------------------------------------#
push: clean
	rsync -avc --delete ./ sv:/data/rpm/
pull:
	rsync -avc sv:/data/yum/ ./
pulld:
	rsync -avc --delete sv:/data/yum/ ./

build: push build-on-sv pull
build-on-sv:
	ssh sv "cd /data/yum; make build-sv"

#---------------------------------------------#
# interact with build-el9 machine
#---------------------------------------------#
push9:
	ssh build-el9 'mkdir -p /tmp/yum'
	rsync -avc --delete /data/yum/ build-el9:/tmp/yum/
pull9:
	rsync -avc --delete build-el9:/tmp/yum/ ./
build9:
	ssh build-el9 "cd /tmp/yum; make build-on-el9"

# transfer to build-el9 and build, then pull back
build-sv:push9 build9 pull9

#---------------------------------------------#
# build repo
#---------------------------------------------#
build-on-el9:
	bin/build grafana/x86_64;
	bin/build grafana/aarch64;

	bin/build prometheus/el7.x86_64;
	bin/build prometheus/el8.x86_64;
	bin/build prometheus/el9.x86_64;

	bin/build redis/el7.x86_64;
	bin/build redis/el8.x86_64;
	bin/build redis/el9.x86_64;

	bin/build el.aarch64;
	bin/build el.x86_64;
	bin/build el7.x86_64;
	bin/build el8.x86_64;
	bin/build el9.x86_64;
	bin/build uel20.x86_64;

	bin/build minio/el.x86_64;
	bin/build minio/el.aarch64;

clean:
	find . -type f -name .DS_Store -delete

#---------------------------------------------#
# publish
#---------------------------------------------#
sync: release
pub: release
release: clean
	coscmd upload --recursive -s -f -y --delete --ignore .idea,.gitignore,bin . yum

.PHONY: push pull pulld build build-on-sv push9 pull9 build9 build-sv build-on-el9 clean sync pub release