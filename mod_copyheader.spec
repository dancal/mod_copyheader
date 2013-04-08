Summary: mod_copyheader is Apache 2.2 module for copy response header to note
Name: mod_copyheader
Version: 0.1
Release: 0.1.wp
License: Apache
Group: System Environment/Daemons
URL: https://www.widerplanet.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: httpd-devel
Requires: httpd httpd-devel

%description
mod_copyheader is Apache 2.2 module for copy response header to note

%prep
%setup -q

%build
make copyheader

%install
rm -rf $RPM_BUILD_ROOT
install -m0755 -d $RPM_BUILD_ROOT$(apxs -q LIBEXECDIR)
make DESTDIR=$RPM_BUILD_ROOT install
install -m0644 -D mod_copyheader.conf $RPM_BUILD_ROOT/etc/httpd/conf.d/mod_copyheader.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/httpd/modules/mod_copyheader.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_copyheader.conf

%post
/usr/sbin/apxs -e -A -n mod_copyheader $(apxs -q LIBEXECDIR)/mod_copyheader.so

%preun
/usr/sbin/apxs -e -A -n mod_copyheader $(apxs -q LIBEXECDIR)/mod_copyheader.so
