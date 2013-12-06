%define	_class	Net
%define	_subclass	POP3
%define	modname	%{_class}_%{_subclass}

Summary:	POP3 class to access POP3 server
Name:		php-pear-%{modname}
Version:	1.3.8
Release:	7
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_POP3/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Provides a POP3 class to access POP3 server. Support all POP3 commands
including UIDL listings, APOP authentication, DIGEST-MD5 and CRAM-MD5
using optional Auth_SASL package.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

