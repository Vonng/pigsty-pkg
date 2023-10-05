# Prometheus Repo

Prometheus RPM repo for x86_64 on el7,8,9 . Mirror from [packagecloud.io/prometheus-rpm/release/el](https://packagecloud.io/prometheus-rpm/release/el)


-------------------

## Usage

Add pigsty prometheus repo to `/etc/yum.repos.d/prometheus.repo`

```bash
curl https://get.pigsty.cc/yum/prometheus/repo -o /etc/yum.repos.d/prometheus.repo
```

```bash
cat > /etc/yum.repos.d/prometheus.repo <<-'EOF'
[pigsty-prometheus]
name=Prometheus Yum Repo Pigsty Mirror $releasever - $basearch
baseurl=https://get.pigsty.cc/yum/prometheus/el$releasever.$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1
EOF
```

There's an official `prometheus-rpm` repo on package packagecloud.io:

```bash
cat > /etc/yum.repos.d/prometheus.repo <<-'EOF'
[prometheus]
name=Prometheus $releasever - $basearch
baseurl=https://packagecloud.io/prometheus-rpm/release/el/$releasever/$basearch
gpgcheck=0
enabled=1
module_hotfixes=1
EOF
```


-------------------

## Upstream

- `https://packagecloud.io/prometheus-rpm/release/el/$releasever/$basearch`
  - el7: https://packagecloud.io/prometheus-rpm/release/el/7
  - el8: https://packagecloud.io/prometheus-rpm/release/el/8
  - el9: https://packagecloud.io/prometheus-rpm/release/el/9



-------------------

## Build

How to update prometheus packages?

Repeat on el7 / el8 / el9

```bash
rm -rf /tmp/prometheus; mkdir -p /tmp/prometheus
sudo mv -f /etc/yum.repos.d/*.repo* /etc/yum.repos.d/backup/;

cat > /etc/yum.repos.d/prometheus.repo <<-'EOF'
[prometheus]
name=Prometheus $releasever - $basearch
baseurl=https://packagecloud.io/prometheus-rpm/release/el/$releasever/$basearch
gpgcheck=0
enabled=1
EOF

yumdownloader --destdir=/tmp/prometheus --arch=x86_64 prometheus2 alertmanager pushgateway karma apache_exporter artifactory_exporter bareos_exporter bind_exporter blackbox_exporter cadvisor collectd_exporter consul_exporter couchbase_exporter dellhw_exporter domain_exporter ebpf_exporter elasticsearch_exporter exim_exporter exporter_exporter frr_exporter graphite_exporter haproxy_exporter influxdb_exporter iperf3_exporter ipmi_exporter jolokia_exporter json_exporter junos_exporter kafka_exporter keepalived_exporter memcached_exporter mongodb_exporter mtail mysqld_exporter nats_exporter nginx_exporter node_exporter openstack_exporter pgbouncer_exporter phpfpm_exporter ping_exporter postgres_exporter process_exporter rabbitmq_exporter redis_exporter smokeping_prober snmp_exporter sql_exporter squid_exporter ssl_exporter statsd_exporter systemd_exporter 
```

Then collect rpm packages from building machines.

```bash
scp build-el7:/tmp/prometheus/*  /data/yum/prometheus/el7.x86_64/;
scp build-el8:/tmp/prometheus/*  /data/yum/prometheus/el8.x86_64/;
scp build-el9:/tmp/prometheus/*  /data/yum/prometheus/el9.x86_64/;
```
