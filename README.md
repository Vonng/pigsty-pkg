# Pigsty Packages: RPM & APT Repo

Supplementary packages for the [Pigsty](https://github.com/Vonng/pigsty) project:

- [infra](rpm/infra/): Observability stack: prometheus etc...
- [pgsql](rpm/pgsql/): PostgreSQL extra extensions and tools
- [minio](rpm/minio/): `minio` & `mcli` binaries for generic linux
- [redis](rpm/redis/): redis & redis stack server for el7 - el9

The [`rpm`](rpm/) contains el7 ~ el9 packages, and the [`deb`](deb/) contains debian/ubuntu packages.

We have all the EL packages available on the `repo.pigsty.cc` CDN:

```bash
curl -sSL https://repo.pigsty.cc/rpm/infra/repo     -o /etc/yum.repos.d/pigsty-infra.repo
curl -sSL https://repo.pigsty.cc/rpm/pgsql/repo     -o /etc/yum.repos.d/pigsty-pgsql.repo
curl -sSL https://repo.pigsty.cc/rpm/redis/repo     -o /etc/yum.repos.d/pigsty-redis.repo
curl -sSL https://repo.pigsty.cc/rpm/minio/repo     -o /etc/yum.repos.d/pigsty-minio.repo
curl -sSL https://get.pigsty.cc/yum/prometheus/repo -o /etc/yum.repos.d/prometheus.repo
curl -sSL https://get.pigsty.cc/yum/grafana/repo    -o /etc/yum.repos.d/grafana.repo
```

For Debian, we have repo for infra, minio & redis

```
deb [trusted=yes] https://repo.pigsty.cc/deb/infra/amd64 ./
deb [trusted=yes] https://repo.pigsty.cc/deb/pgsql/amd64 ./
deb [trusted=yes] https://repo.pigsty.cc/deb/minio/amd64 ./
```

```
deb [trusted=yes] https://repo.pigsty.cc/deb/infra/arm64 ./
deb [trusted=yes] https://repo.pigsty.cc/deb/pgsql/arm64 ./
deb [trusted=yes] https://repo.pigsty.cc/deb/minio/arm64 ./
```


----------------

## Package Cloud Mirror

For EL8 / EL9 and compatible distributions:

```bash
echo > /etc/yum.repos.d/pigsty-pgsql.repo <<EOF
[pigsty-infra]
name=Pigsty INFRA Module Repo For $basearch
baseurl=https://packagecloud.io/pigsty/infra/el/8/$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1

[pigsty-pgsql]
name=Pigsty PGSQL Module Repo For el$releasever.$basearch
baseurl=https://packagecloud.io/pigsty/pgsql/el/$releasever/$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1

[pigsty-redis]
name=Pigsty REDIS Module Repo For el$releasever.$basearch
baseurl=https://packagecloud.io/pigsty/pgsql/el/$releasever/$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1

[pigsty-minio]
name=Pigsty MINIO Module Repo For el$releasever.$basearch
baseurl=https://packagecloud.io/pigsty/minio/el/$releasever/$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1

EOF

yum makecache
```


For Ubuntu Jammy 22.04:

```bash
echo > /etc/apt/sources.list.d/pigsty-jammy.list <<EOF
deb [trusted=yes] https://packagecloud.io/pigsty/infra/ubuntu/ jammy main
deb [trusted=yes] https://packagecloud.io/pigsty/pgsql/ubuntu/ jammy main
deb [trusted=yes] https://packagecloud.io/pigsty/minio/ubuntu/ jammy main
EOF

apt update
```


----------------

## Publish

```bash
find . -type f -name .DS_Store -delete
make publish-rpm
make publish-deb
make publish-etc
make publish-src
```

There's a packagecloud.io mirror, and we will use hard-coded el/8 and ubuntu/jammy for generic linux packages:

```bash
package_cloud push pigsty/infra/el/8         rpm/infra/x86_64/*.rpm
package_cloud push pigsty/infra/ubuntu/jammy deb/infra/amd64/*.deb
package_cloud push pigsty/minio/el/8         rpm/minio/x86_64/*.rpm
package_cloud push pigsty/minio/ubuntu/jammy deb/minio/amd64/*.deb
package_cloud push pigsty/pgsql/el/7         rpm/pgsql/el7.x86_64/*.rpm
package_cloud push pigsty/pgsql/el/8         rpm/pgsql/el8.x86_64/*.rpm
package_cloud push pigsty/pgsql/el/9         rpm/pgsql/el9.x86_64/*.rpm
package_cloud push pigsty/pgsql/ubuntu/jammy deb/pgsql/jammy.amd64/*.deb
```


```bash
package_cloud push pigsty/infra/el/8         rpm/infra/aarch64/*.rpm
package_cloud push pigsty/infra/ubuntu/jammy deb/infra/arm64/*.deb
package_cloud push pigsty/minio/el/8         rpm/minio/aarch64/*.rpm
package_cloud push pigsty/minio/ubuntu/jammy deb/minio/arm64/*.deb

```

https://repo.pigsty.cc/deb/infra/Packages.gz
```


package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/pushgateway-1.6.2-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/redis_exporter-1.54.0-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/sealos_4.3.5_linux_amd64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/vector-0.33.0-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/victoria-logs-0.4.1-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/victoria-metrics-1.94.0-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/victoria-metrics-cluster-1.94.0-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/victoria-metrics-utils-1.94.0-1.x86_64.rpm
package_cloud push pigsty/infra/el/8  rpm/infra/x86_64/vip-manager_2.1.0_Linux_x86_64.rpm