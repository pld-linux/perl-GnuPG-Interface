#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	GnuPG
%define		pnam	Interface
Summary:	GnuPG::Interface - Perl interface to GnuPG
Summary(pl.UTF-8):	GnuPG::Interface - perlowy interfejs do GnuPG
Name:		perl-GnuPG-Interface
Version:	0.52
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GnuPG/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7de2662f2fb00a89fd0762ca027e80a8
URL:		http://search.cpan.org/dist/GnuPG-Interface/
BuildRequires:	gnupg
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-MethodMaker
BuildRequires:	perl-Moo
BuildRequires:	perl-MooX-late
BuildRequires:	perl-MooX-HandlesVia
BuildRequires:	perl-Moose
%endif
# not recognized by perl.req
Requires:	perl-Class-MethodMaker
Requires:	perl-Mouse
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to
perform functions such as but not limited to encrypting, signing,
decryption, verification, and key-listing parsing.

%description -l pl.UTF-8
GnuPG::Interface i powiązane moduły powstały, by udostępnić obiektowo
zorientowany sposób na interakcję z GnuPG. Moduły mogą wykonywać
funkcje takie jak szyfrowanie, podpisywanie, odszyfrowywanie,
weryfikację, analizę list kluczy i inne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}/%{pnam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MANIFEST
%{perl_vendorlib}/GnuPG/*.pm
%{_mandir}/man3/*
