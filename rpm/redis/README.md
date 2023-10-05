# Redis Repo

Redis server (el7,8,9) and redis stack (el7, el9) yum repo, pigsty mirror

-------------------

## Usage

Add pigsty redis repo to `/etc/yum.repos.d/redis.repo`

```bash
curl https://get.pigsty.cc/yum/redis/repo -o /etc/yum.repos.d/redis.repo
```

```bash
cat > /etc/yum.repos.d/redis.repo <<-'EOF'
[pigsty-redis]
name=Redis Yum Repo Pigsty Mirror $releasever - $basearch
baseurl=https://get.pigsty.cc/yum/redis/el$releasever.$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1
EOF
```

There's mirror on package cloud too:

```bash
cat > /etc/yum.repos.d/redis.repo <<-'EOF'
[pigsty_redis]
name=pigsty_redis
baseurl=https://packagecloud.io/pigsty/redis/el/$releasever/$basearch
repo_gpgcheck=0
gpgcheck=0
metadata_expire=86400
module_hotfixes=1
EOF
```



-------------------

## Upstream

- EL7: Redis Remi + Redis Stack
  - https://rpmfind.net/linux/remi/enterprise/7/remi/x86_64/
  - http://packages.redis.io/rpm/rhel$releasever
- EL8: Redis Remi + Redis Stack
  - https://rpmfind.net/linux/remi/enterprise/8/redis72/x86_64/
  - http://packages.redis.io/rpm/rhel$releasever
- EL9:
  - https://rpmfind.net/linux/remi/enterprise/9/redis72/x86_64/


-------------------

## Build

Collect x86_64 redis RPMs on building machines:

```bash
rm -rf /tmp/redis; mkdir -p /tmp/redis
sudo mv -f /etc/yum.repos.d/*.repo* /etc/yum.repos.d/backup/;

# add on el7
cat > /etc/yum.repos.d/redis.repo <<-'EOF'
[redis]
name=Redis $releasever - $basearch
baseurl=https://rpmfind.net/linux/remi/enterprise/7/remi/x86_64/
gpgcheck=0
enabled=1
EOF

# add on el7 , el8
cat > /etc/yum.repos.d/stack.repo <<-'EOF'
[redis-stack]
name=Redis $releasever - $basearch
baseurl=http://packages.redis.io/rpm/rhel$releasever
gpgcheck=0
enabled=1
EOF

# add on el8, el9
cat > /etc/yum.repos.d/redis.repo <<-'EOF'
[redis]
name=Redis $releasever - $basearch
baseurl=https://rpmfind.net/linux/remi/enterprise/$releasever/redis72/x86_64/
gpgcheck=0
enabled=1
EOF

yum clean all; yum makecache; yum list available | grep redis

# run on el7, el8, el9
yumdownloader --destdir=/tmp/redis --arch=x86_64 redis redis-devel
yumdownloader --destdir=/tmp/redis redis-doc

# run on el7, el8
yumdownloader --destdir=/tmp/redis --arch=x86_64 redis-stack-server redis-tools
```

Collect rpms on host building machine:

```bash
scp build-el7:/tmp/redis/*  /data/yum/redis/el7.x86_64/;
scp build-el8:/tmp/redis/*  /data/yum/redis/el8.x86_64/;
scp build-el9:/tmp/redis/*  /data/yum/redis/el9.x86_64/;
```

Publish to packagecloud.io

```bash
package_cloud push pigsty/redis/el/7 el7.x86_64/*.rpm
package_cloud push pigsty/redis/el/8 el8.x86_64/*.rpm
package_cloud push pigsty/redis/el/9 el9.x86_64/*.rpm
```