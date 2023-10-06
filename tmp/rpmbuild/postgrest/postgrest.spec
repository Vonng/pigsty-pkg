%define debug_package %{nil}

Name:       postgrest
Version:    9.0.0
Release:    1%{?dist}
Summary:    PostgREST agent
URL:        https://postgrest.org/en/stable/
Group:      PostgREST
License:    MIT License

Source0: https://github.com/PostgREST/postgrest/releases/download/v%{version}/postgrest-v%{version}-linux-static-x64.tar.xz
Source1: %{name}.service
Source2: %{name}.conf

%{?systemd_requires}
Requires(pre): shadow-utils

%description
PostgREST is a standalone web server that turns your PostgreSQL database directly into a RESTful API. The structural constraints and permissions in the database determine the API endpoints and operations.

%prep
tar -xf %{SOURCE0}

%build
# nothing to do here

# %install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.conf

# %pre
# getent group postgres >/dev/null || groupadd -r postgres
# getent passwd postgres >/dev/null || \
#   useradd -r -g postgres -d %{_sharedstatedir}/postgres -s /sbin/nologin \
#           -c "postgres" postgres
# exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service