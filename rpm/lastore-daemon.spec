Name:           lastore-daemon
Version:        1.0.0
Release:        1%{?dist}
Summary:        Lastore Daemon - App Store Backend for Lingmo OS
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/lastore-daemon
Source0:        lastore-daemon-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  golang-github-linuxdeepin-go-dbus-factory-devel
BuildRequires:  golang-github-linuxdeepin-go-lib-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  dbus-devel

%description
Lastore daemon is the backend service for the application store
on Lingmo OS, handling package management and updates.

%prep
%autosetup -n %{name}-%{version}

%build
export GOPATH=%{_gopath}
go build -v -p %{?_smp_mflags} -ldflags "-s -w" ./...

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/dbus-1/services/
install -d %{buildroot}%{_libexecdir}/lastore/
install -m 0755 lastore-daemon %{buildroot}%{_bindir}/
cp -r misc/dbus/*.service %{buildroot}%{_datadir}/dbus-1/services/ || true

%files
%doc README.md
%license LICENSE*
%{_bindir}/lastore-daemon*
%{_datadir}/dbus-1/services/lastore*.service
%{_libexecdir}/lastore/

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
