#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	GnuPG
%define	pnam	Interface
Summary:	GnuPG::Interface - Perl module to use GnuPG
Summary(pl):	GnuPG::Interface - Obs³uga GnuPG
Name:		perl-GnuPG-Interface
Version:	0.33
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.gnu.org/
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-GnuPG
Requires:	perl-GnuPG
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts make using GnuPG simple and natural.

%description -l pl
Nieniejszy modu³ jest prób± ³atwej i naturalnej obs³ugi GnuPG.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_sitelib}/%{pdir}/%{pnam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS MANIFEST
%{perl_sitelib}/%{pdir}/*.pm
#%dir %{perl_sitelib}/%{pdir}/%{pnam}/
%{_mandir}/man3/*
