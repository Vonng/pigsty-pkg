%define debug_package %{nil}

Name:       promtail
Version:    2.4.2
Release:    1%{?dist}
Summary:    Promtail agent
URL:        https://github.com/grafana/loki
Group:      Grafana
License:    Apache License 2.0

Source0: https://github.com/grafana/loki/releases/download/v%{version}/%{name}-linux-amd64.zip
Source1: %{name}.service
Source2: %{name}.yml

%{?systemd_requires}
Requires(pre): shadow-utils

%description
Promtail is an agent which ships the contents of local logs to a private Loki
instance or Grafana Cloud. It is usually
deployed to every machine that has applications needed to be monitored.

It primarily:

1. Discovers targets
2. Attaches labels to log streams
3. Pushes them to the Loki instance.

Currently, Promtail can tail logs from two sources: local log files and the
systemd journal (on AMD64 machines only).

%prep
unzip -o %{SOURCE0}

%build
# nothing to do here

# %install
install -D -m 755 %{name}-linux-amd64 %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.yml

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
  useradd -r -g prometheus -d %{_sharedstatedir}/prometheus -s /sbin/nologin \
          -c "Prometheus services" prometheus
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.yml
%{_unitdir}/%{name}.service