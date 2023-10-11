#!/usr/bin/env python
import re
import requests

rpm_pattern = re.compile(r'href="(.+?\.rpm)"')
deb_pattern = re.compile(r'href="(.+?\.deb)"')

MINIO_AMD64 = 'https://dl.min.io/server/minio/release/linux-amd64'
MINIO_ARM64 = 'https://dl.min.io/server/minio/release/linux-arm64'
MCLI_AMD64  = 'https://dl.min.io/client/mc/release/linux-amd64'
MCLI_ARM64  = 'https://dl.min.io/client/mc/release/linux-arm64'

t_minio_amd64 = requests.get(MINIO_AMD64).text
t_minio_arm64 = requests.get(MINIO_ARM64).text
t_mcli_amd64  = requests.get(MCLI_AMD64 ).text
t_mcli_arm64  = requests.get(MCLI_ARM64 ).text

rp_minio_amd64 = rpm_pattern.findall(t_minio_amd64)[0]
rp_minio_arm64 = rpm_pattern.findall(t_minio_arm64)[0]
rp_mcli_amd64  = rpm_pattern.findall(t_mcli_amd64)[0]
rp_mcli_arm64  = rpm_pattern.findall(t_mcli_arm64)[0]

dp_minio_amd64 = deb_pattern.findall(t_minio_amd64)[0]
dp_minio_arm64 = deb_pattern.findall(t_minio_arm64)[0]
dp_mcli_amd64  = deb_pattern.findall(t_mcli_amd64)[0]
dp_mcli_arm64  = deb_pattern.findall(t_mcli_arm64)[0]

Tasks = [
    { "name": rp_minio_amd64,  "url": MINIO_AMD64 + '/' + rp_minio_amd64 , "dir": "el.x86_64"  ,"arch": "x86_64" , "package": "rpm" },
    { "name": dp_minio_amd64,  "url": MINIO_AMD64 + '/' + dp_minio_amd64 , "dir": "deb.x86_64" ,"arch": "x86_64" , "package": "deb" },

    { "name": rp_minio_arm64,  "url": MINIO_ARM64 + '/' + rp_minio_arm64 , "dir": "el.aarch64"  ,"arch": "arm64" , "package": "rpm" },
    { "name": dp_minio_arm64,  "url": MINIO_ARM64 + '/' + dp_minio_arm64 , "dir": "deb.arm64" ,"arch": "arm64" , "package": "deb" },

    { "name": rp_mcli_amd64,  "url": MCLI_AMD64 + '/' + rp_mcli_amd64 , "dir": "el.x86_64"  ,"arch": "x86_64" , "package": "rpm" },
    { "name": dp_mcli_amd64,  "url": MCLI_AMD64 + '/' + dp_mcli_amd64 , "dir": "deb.x86_64" ,"arch": "x86_64" , "package": "deb" },

    { "name": rp_mcli_arm64,  "url": MCLI_ARM64 + '/' + rp_mcli_arm64 , "dir": "el.aarch64"  ,"arch": "arm64" , "package": "rpm" },
    { "name": dp_mcli_arm64,  "url": MCLI_ARM64 + '/' + dp_mcli_arm64 , "dir": "deb.arm64" ,"arch": "arm64" , "package": "deb" },

]

for i in Tasks:
    if i['package'] == 'deb' and i['arch'] == 'x86_64':
        print("curl -SL %-90s -o %10s/%s" % (i["url"], i["dir"], i["name"]))

    if i['package'] == 'deb' and i['arch'] == 'arm64':
        print("curl -SL %-90s -o %10s/%s" % (i["url"], i["dir"], i["name"]))