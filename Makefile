#---------------------------------------------#
# RPM
#---------------------------------------------#
rpm: push-rpm build-rpm pull-rpm
deb: push-deb build-deb pull-deb

#---------------------------------------------#
# PUSH
#---------------------------------------------#
push: push-rpm push-deb
push-rpm: clean
	rsync -avc --delete ./rpm/ sv:/data/rpm/
push-deb: clean
	rsync -avc --delete ./deb/ sv:/data/deb/

#---------------------------------------------#
# PULL
#---------------------------------------------#
pull: pull-rpm pull-deb
pull-rpm:
	rsync -avc sv:/data/rpm/ ./rpm/
pull-deb:
	rsync -avc sv:/data/deb/ ./deb/

#---------------------------------------------#
# Build
#---------------------------------------------#
build: push build-on-sv pull
build-rpm:
	ssh sv "cd /data/rpm; make"
build-deb:
	ssh sv "cd /data/deb; make"

#---------------------------------------------#
# UPLOAD
#---------------------------------------------#
publish: clean publish-rpm publish-deb publish-etc publish-src
publish-rpm:
	coscmd upload --recursive -s -f -y --delete --ignore rpm/Makefile rpm rpm
publish-deb:
	coscmd upload --recursive -s -f -y --delete --ignore deb/Makefile deb deb
publish-etc:
	coscmd upload --recursive -s -f -y --delete --ignore etc etc
publish-src:
	coscmd upload --recursive -s -f -y --delete --ignore src src

#---------------------------------------------#
# push/pull changes with development server sv
#---------------------------------------------#
clean:
	find . -type f -name .DS_Store -delete

#---------------------------------------------#
# MISC
#---------------------------------------------#
.PHONY: rpm deb push push-rpm push-deb pull pull-rpm pull-deb \
    build build-rpm build-deb publish publish-rpm publish-deb publish-etc publish-src \
    clean