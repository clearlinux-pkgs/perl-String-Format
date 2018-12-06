#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Format
Version  : 1.18
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/String-Format-1.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/String-Format-1.18.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-format-perl/libstring-format-perl_1.18-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-String-Format-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
String::Format - sprintf-like string formatting capabilities with
arbitrary format definitions

%package dev
Summary: dev components for the perl-String-Format package.
Group: Development
Provides: perl-String-Format-devel = %{version}-%{release}

%description dev
dev components for the perl-String-Format package.


%package license
Summary: license components for the perl-String-Format package.
Group: Default

%description license
license components for the perl-String-Format package.


%prep
%setup -q -n String-Format-1.18
cd ..
%setup -q -T -D -n String-Format-1.18 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/String-Format-1.18/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Format
cp COPYING %{buildroot}/usr/share/package-licenses/perl-String-Format/COPYING
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-String-Format/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1String/Format.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Format.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Format/COPYING
/usr/share/package-licenses/perl-String-Format/deblicense_copyright
