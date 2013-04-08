%define		mod_name	copyheader
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module:
Name:		mod_%{mod_name}
Version:	0.1
Release:	0.1
License:	Apache
Group:		Networking/Daemons/HTTP
Source0:	http://117.52.90.7/repo/mod_copyheader-%{version}.tar.gz
Source1:	mod_copyheader.conf
URL:		http://www.widerplanet.com
BuildRequires:	%{apxs}
BuildRequires:	httpd >= 2.2.0
Requires:	apache(modules-api) = %apache_modules_api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
mod_copy_header is Apache 2.2 module for copy response header to note

%prep
%setup -q -n mod_%{mod_name}-%{version}

%build
%{apxs} -c mod_%{mod_name}.c -o mod_%{mod_name}.so

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/conf.d}
install -p mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service apache restart

%postun
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*
