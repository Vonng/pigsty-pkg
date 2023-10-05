# Pigsty Packages: RPM & APT Repo

Supplementary packages for the [Pigsty](https://github.com/Vonng/pigsty) project:

- [basic](rpm/basic/): Pigsty basic packages: cli, nginx, ansible, sealos, ferretdb
- [pgsql](rpm/pgsql/): PostgreSQL extra extensions and tools
- [minio](rpm/minio/): `minio` & `mcli` binaries for generic linux
- [redis](rpm/redis/): redis & redis stack server for el7 - el9
- [prometheus](rpm/prometheus/): prometheus & exporters
- [grafana](rpm/grafana/): grafana observability stack

The [`rpm`](rpm/) contains el7 ~ el9 packages, and the [`deb`](deb/) contains debian packages.

We have all the packages available on the `get.pigsty.cc` CDN:

```bash
curl -sSL https://get.pigsty.cc/rpm/basic/repo      -o /etc/yum.repos.d/pigsty-basic.repo
curl -sSL https://get.pigsty.cc/rpm/pgsql/repo      -o /etc/yum.repos.d/pigsty-pgsql.repo
curl -sSL https://get.pigsty.cc/rpm/minio/repo      -o /etc/yum.repos.d/pigsty-minio.repo
curl -sSL https://get.pigsty.cc/rpm/redis/repo      -o /etc/yum.repos.d/pigsty-redis.repo
curl -sSL https://get.pigsty.cc/rpm/grafana/repo    -o /etc/yum.repos.d/pigsty-grafana.repo
curl -sSL https://get.pigsty.cc/rpm/prometheus/repo -o /etc/yum.repos.d/pigsty-prometheus.repo
```


## Usage

For common users, use the package cloud version

```bash

```


For mainland china users, use the CDN version

```bash

```