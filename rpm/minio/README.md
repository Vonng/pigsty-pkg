# MinIO Repo

MinIO RPM Repo for x86_64 for EL generic

Including the latest version of `minio` and `mcli`


-------------------

## Usage

Add pigsty minio repo to `/etc/yum.repos.d/minio.repo`

```bash
curl https://get.pigsty.cc/yum/minio/repo -o /etc/yum.repos.d/minio.repo
```

```bash
cat > /etc/yum.repos.d/minio.repo <<-'EOF'
[pigsty-minio]
name=Minio Yum Repo Pigsty Mirror $basearch
baseurl=https://get.pigsty.cc/yum/minio/el.$basearch
skip_if_unavailable = 1
enabled = 1
priority = 1
gpgcheck = 0
EOF
```

There's mirror on package cloud too:

```bash
cat > /etc/yum.repos.d/minio.repo <<-'EOF'
[pigsty_minio]
name=pigsty_minio
baseurl=https://packagecloud.io/pigsty/minio/el/8/$basearch
repo_gpgcheck=0
gpgcheck=0
metadata_expire=86400
EOF
```

> don't worry about the `el/8` here, minio packages are generic and can be used on any EL version



-------------------

## Upstream

- [MCLI.x86_64](https://dl.min.io/client/mc/release/linux-amd64/)
- [MCLI.arm64](https://dl.min.io/client/mc/release/linux-arm64/)
- [MinIO.x86_64](https://dl.min.io/server/minio/release/linux-amd64/)
- [MinIO.arm64](https://dl.min.io/server/minio/release/linux-arm64/)


-------------------

## Build

Get latest package list:

```bash
python get-minio.py
```

```bash
curl -SL https://dl.min.io/server/minio/release/linux-amd64/minio-20230930070229.0.0.x86_64.rpm     -o  el.x86_64/minio-20230930070229.0.0.x86_64.rpm
curl -SL https://dl.min.io/server/minio/release/linux-arm64/minio-20230930070229.0.0.aarch64.rpm    -o el.aarch64/minio-20230930070229.0.0.aarch64.rpm
curl -SL https://dl.min.io/client/mc/release/linux-amd64/mcli-20230929164122.0.0.x86_64.rpm         -o  el.x86_64/mcli-20230929164122.0.0.x86_64.rpm
curl -SL https://dl.min.io/client/mc/release/linux-arm64/mcli-20230929164122.0.0.aarch64.rpm        -o el.aarch64/mcli-20230929164122.0.0.aarch64.rpm
```

Upload rpm & deb packages to packagecloud.io

```bash
cd el.x86_64/
package_cloud push pigsty/minio *.rpm

cd ../deb.x86_64/
package_cloud push pigsty/minio *.deb
```