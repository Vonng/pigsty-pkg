# Grafana Repo

Grafana LGTM stack packages for EL generic linux.

There's no difference between el7, el8, el9, so there's only [`x86_64`](x86_64/) directory.

There's no package cloud mirror for grafana since there's already an official yum repo: [`rpm.grafana.com`](https://rpm.grafana.com)


-------------------

## Usage

Add pigsty grafana repo to `/etc/yum.repos.d/grafana.repo`

```bash
curl https://repo.pigsty.cc/yum/grafana/repo -o /etc/yum.repos.d/grafana.repo
```

You can use the pigsty CDN mirror

```bash
cat > /etc/yum.repos.d/grafana.repo <<-'EOF'
[pigsty-grafana]
name=Grafana Yum Repo Pigsty Mirror $releasever - $basearch
baseurl=https://repo.pigsty.cc/rpm/grafana/el$releasever.$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
module_hotfixes=1
EOF
```


-------------------

## Upstream

There's an official Grafana yum repo

```bash
cat > /etc/yum.repos.d/prometheus.repo <<-'EOF'
[grafana]
name=Grafana $releasever - $basearch
baseurl=https://rpm.grafana.com
gpgcheck=0
enabled=1
EOF
```



-------------------

## Build

How to update grafana packages?

```bash
# Run on `build-el9` server:
rm -rf /tmp/x86_64 /tmp/aarch64; mkdir -p /tmp/x86_64 /tmp/aarch64;
sudo mv -f /etc/yum.repos.d/*.repo* /etc/yum.repos.d/backup/;
cat > /etc/yum.repos.d/grafana.repo <<-'EOF'
[grafana]
name=Grafana $releasever - $basearch
baseurl=https://rpm.grafana.com
gpgcheck=0
enabled=1
EOF

yumdownloader --destdir=/tmp/x86_64  --arch=x86_64 grafana loki logcli promtail grafana-agent grafana-agent-flow loki-canary metaconvert mimir mimirtool mimir-continuous-test query-tee tempo synthetic-monitoring-agent
yumdownloader --destdir=/tmp/aarch64 --arch=aarch64 grafana loki logcli promtail grafana-agent grafana-agent-flow loki-canary metaconvert mimir mimirtool mimir-continuous-test query-tee tempo synthetic-monitoring-agent


# run on host machine
scp build-el9:/tmp/x86_64/*  /data/yum/grafana/x86_64/  ;
scp build-el9:/tmp/aarch64/* /data/yum/grafana/aarch64/ ;
```


-------------------

## Publish
