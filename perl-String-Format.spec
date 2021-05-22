#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Format
Version  : 1.18
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/String-Format-1.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SREZIC/String-Format-1.18.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-format-perl/libstring-format-perl_1.18-1.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-String-Format-license = %{version}-%{release}
Requires: perl-String-Format-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
String::Format - sprintf-like string formatting capabilities with
arbitrary format definitions

%package dev
Summary: dev components for the perl-String-Format package.
Group: Development
Provides: perl-String-Format-devel = %{version}-%{release}
Requires: perl-String-Format = %{version}-%{release}

%description dev
dev components for the perl-String-Format package.


%package license
Summary: license components for the perl-String-Format package.
Group: Default

%description license
license components for the perl-String-Format package.


%package perl
Summary: perl components for the perl-String-Format package.
Group: Default
Requires: perl-String-Format = %{version}-%{release}

%description perl
perl components for the perl-String-Format package.


%prep
%setup -q -n String-Format-1.18
cd %{_builddir}
tar xf %{_sourcedir}/libstring-format-perl_1.18-1.debian.tar.xz
cd %{_builddir}/String-Format-1.18
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/String-Format-1.18/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Format
cp %{_builddir}/String-Format-1.18/COPYING %{buildroot}/usr/share/package-licenses/perl-String-Format/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-String-Format/a25df1e07d17dbf111d44f72f8748a9a936b84a9
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Format.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Format/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1
/usr/share/package-licenses/perl-String-Format/a25df1e07d17dbf111d44f72f8748a9a936b84a9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/String/Format.pm
