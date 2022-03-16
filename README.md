# [Pigsty](https://github.com/Vonng/pigsty-pkg) RPM Packages

Some software does not have official rpm packages. So I'have to build or gather them here.

Some rpm build scripts are scraped from other github repo. Regards



## List

* [HAProxy](#HAProxy) 2.5.5
* Redis 6.2.6



```
- https://github.com/cybertec-postgresql/vip-manager/releases/download/v1.0.1/vip-manager_1.0.1-1_amd64.rpm
- https://github.com/Vonng/pg_exporter/releases/download/v0.4.1/pg_exporter-0.4.1-1.el7.x86_64.rpm
- https://github.com/Vonng/pigsty-pkg/releases/download/init/haproxy-2.5.1-1.el7.x86_64.rpm
- https://github.com/Vonng/pigsty-pkg/releases/download/init/haproxy-debuginfo-2.5.1-1.el7.x86_64.rpm
- https://rpmfind.net/linux/remi/enterprise/7/remi/x86_64/redis-6.2.6-1.el7.remi.x86_64.rpm
- https://github.com/greenplum-db/gpdb/releases/download/6.19.3/open-source-greenplum-db-6.19.3-rhel7-x86_64.rpm
- http://guichaz.free.fr/polysh/files/polysh-0.4-1.noarch.rpm
- https://github.com/dalibo/pev2/releases/download/v0.24.0/pev2.tar.gz
- https://github.com/sosedoff/pgweb/releases/download/v0.11.10/pgweb_linux_amd64.zip
- https://github.com/PostgREST/postgrest/releases/download/v9.0.0/postgrest-v9.0.0-linux-static-x64.tar.xz
- https://github.com/Vonng/pg_exporter/releases/download/v0.4.1/pg_exporter_v0.4.1_linux-amd64.tar.gz
- https://github.com/prometheus/node_exporter/releases/download/v1.3.1/node_exporter-1.3.1.linux-amd64.tar.gz
- https://github.com/grafana/loki/releases/download/v2.4.2/loki-linux-amd64.zip
- https://github.com/grafana/loki/releases/download/v2.4.2/promtail-linux-amd64.zip
- https://github.com/grafana/loki/releases/download/v2.4.2/logcli-linux-amd64.zip
- https://github.com/grafana/loki/releases/download/v2.4.2/loki-canary-linux-amd64.zip
```







## Redis

Download Lastest Redis RPM from rpmfind remi repo

```bash
rm -rf dist/redis; mkdir dist/redis
curl https://rpmfind.net/linux/remi/enterprise/7/remi/x86_64/redis-6.2.6-1.el7.remi.x86_64.rpm -o dist/redis/redis-6.2.6-1.el7.remi.x86_64.rpm
```



## Greenplum

Download Latest Greenplum RPM

```
rm -rf dist/gpsql; mkdir dist/gpsql; 
cd dist/gpsql
wget https://github.com/greenplum-db/gpdb/releases/download/6.19.4/open-source-greenplum-db-6.19.4-rhel7-x86_64.rpm
```



## HAProxy

Build Lastest HAProxy with Prometheus Support (2.5.5)

Haproxy：https://github.com/philyuchkoff/HAProxy-2-RPM-builder

```bash
sudo su
cd /opt
yum -y groupinstall 'Development Tools'
git clone https://github.com/philyuchkoff/HAProxy-2-RPM-builder.git
cd ./HAProxy-2-RPM-builder
make USE_PROMETHEUS=1

rm -rf dist/haproxy
scp -r meta:/opt/HAProxy-2-RPM-builder/rpmbuild/RPMS/x86_64/ dist/haproxy
```

Download Links：

* Binary：
* Debug：





## Loki Stack

Build Latest Loki & Promtail RPM

Repo: https://github.com/grafana/loki/releases/tag/v2.4.2

Spec: https://github.com/farwydi/loki-rpm

```
cd promtail; ./rpm.sh
cd loki;     ./rpm.sh
```

Download Links：

* Loki
* Promtail



## PostGrest

```bash
rm -rf dist/bytebase; mkdir dist/postgrest

cd dist/postgrest && wget https://github.com/PostgREST/postgrest/releases/download/v9.0.0/postgrest-v9.0.0-linux-static-x64.tar.xz
```





## ByteBase (Beta)

```bash
# install go node 
npm install -g npm@8.5.4
npm install -g yarn
 
sudo su; cd ~; mkdir -p go/src/github.com/bytebase; cd go/src/github.com/bytebase
git checkout tags/v1.0.0
scripts/build.sh
cd bytebase-build; cp bytebase /tmp; chmod 755 /tmp/bytebase

rm -rf dist/bytebase; mkdir dist/bytebase
scp meta:/tmp/bytebase dist/bytebase
```

