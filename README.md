# Pigsty Packages: RPM & APT Repo

Supplementary packages for the [Pigsty](https://github.com/Vonng/pigsty) project:

- [infra](rpm/infra/): Observability stack for Pigsty
- [basic](rpm/basic/): Pigsty node misc packages
- [pgsql](rpm/pgsql/): PostgreSQL extra extensions and tools
- [minio](rpm/minio/): `minio` & `mcli` binaries for generic linux
- [redis](rpm/redis/): redis & redis stack server for el7 - el9

The [`rpm`](rpm/) contains el7 ~ el9 packages, and the [`deb`](deb/) contains debian/ubuntu packages.

We have all the packages available on the `repo.pigsty.cc` CDN:

```bash
curl -sSL https://repo.pigsty.cc/rpm/node/repo  -o /etc/yum.repos.d/pigsty-node.repo
curl -sSL https://repo.pigsty.cc/rpm/infra/repo -o /etc/yum.repos.d/pigsty-infra.repo
curl -sSL https://repo.pigsty.cc/rpm/pgsql/repo -o /etc/yum.repos.d/pigsty-pgsql.repo
curl -sSL https://repo.pigsty.cc/rpm/redis/repo -o /etc/yum.repos.d/pigsty-redis.repo
curl -sSL https://repo.pigsty.cc/rpm/minio/repo -o /etc/yum.repos.d/pigsty-minio.repo
```

```
deb [trusted=yes] https://repo.pigsty.cc/deb/infra/ x86_64
```


----------------

## Build

```
cd deb/infra/x86_64
dpkg-scanpackages -m . /dev/null | gzip -9c > Packages.gz
```

----------------

## Usage

For mainland china users, use the CDN version

```bash

```


----------------

## Publish

```bash
find . -type f -name .DS_Store -delete
coscmd upload --recursive -s -f -y --delete rpm/infra rpm/infra
coscmd upload --recursive -s -f -y --delete rpm/pgsql rpm/pgsql
coscmd upload --recursive -s -f -y --delete rpm/minio rpm/minio
coscmd upload --recursive -s -f -y --delete rpm/redis rpm/redis


coscmd upload --recursive -s -f -y --delete deb deb
coscmd upload --recursive -s -f -y --delete rpm rpm


coscmd upload --recursive -s -f -y --delete deb/minio deb/minio
#coscmd upload --recursive -s -f -y --delete --ignore deb/pgsql deb/pgsql
#coscmd upload --recursive -s -f -y --delete --ignore deb/minio deb/minio
#coscmd upload --recursive -s -f -y --delete --ignore deb/redis deb/redis

https://repo.pigsty.cc/deb/infra/Packages.gz
```