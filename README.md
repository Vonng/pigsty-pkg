# Pigsty Packages: RPM & APT Repo

Supplementary packages for the [Pigsty](https://github.com/Vonng/pigsty) project:

- [infra](rpm/infra/): Observability stack for Pigsty
- [basic](rpm/basic/): Pigsty node misc packages
- [pgsql](rpm/pgsql/): PostgreSQL extra extensions and tools
- [minio](rpm/minio/): `minio` & `mcli` binaries for generic linux
- [redis](rpm/redis/): redis & redis stack server for el7 - el9

The [`rpm`](rpm/) contains el7 ~ el9 packages, and the [`deb`](deb/) contains debian/ubuntu packages.

We have all the packages available on the `get.pigsty.cc` CDN:

```bash
curl -sSL https://get.pigsty.cc/rpm/node/repo  -o /etc/yum.repos.d/pigsty-node.repo
curl -sSL https://get.pigsty.cc/rpm/infra/repo -o /etc/yum.repos.d/pigsty-infra.repo
curl -sSL https://get.pigsty.cc/rpm/pgsql/repo -o /etc/yum.repos.d/pigsty-pgsql.repo
curl -sSL https://get.pigsty.cc/rpm/redis/repo -o /etc/yum.repos.d/pigsty-redis.repo
curl -sSL https://get.pigsty.cc/rpm/minio/repo -o /etc/yum.repos.d/pigsty-minio.repo
```

----------------

## Build


----------------

## Usage

For mainland china users, use the CDN version

```bash

```



----------------

## Publish

```bash
find . -type f -name .DS_Store -delete

coscmd upload --recursive -s -f -y --delete --ignore rpm/infra rpm/infra
coscmd upload --recursive -s -f -y --delete --ignore rpm/pgsql rpm/pgsql
coscmd upload --recursive -s -f -y --delete --ignore rpm/minio rpm/minio
coscmd upload --recursive -s -f -y --delete --ignore rpm/redis rpm/redis


coscmd upload --recursive -s -f -y --delete --ignore deb/infra deb/infra
#coscmd upload --recursive -s -f -y --delete --ignore deb/pgsql deb/pgsql
#coscmd upload --recursive -s -f -y --delete --ignore deb/minio deb/minio
#coscmd upload --recursive -s -f -y --delete --ignore deb/redis deb/redis
```