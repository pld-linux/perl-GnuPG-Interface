#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	GnuPG
%define	pnam	Interface
Summary:	GnuPG::Interface - Perl interface to GnuPG
Summary(pl):	GnuPG::Interface - interfejs perlowy do GnuPG
Name:		perl-GnuPG-Interface
Version:	0.33
Release:	5
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7349795ec874c2af78eec7f274d96bc8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
%if %{with tests}
BuildRequires:	perl-Class-MethodMaker
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuPG::Interface and its associated modules are designed to provide an
object-oriented method for interacting with GnuPG, being able to
perform functions such as but not limited to encrypting, signing,
decryption, verification, and key-listing parsing.

%description -l pl
GnuPG::Interface i powi±zane modu³y s³u¿± powsta³y, by udostêpniæ
obiektowo zorientowany sposób na interakcjê z GnuPG. Modu³y mog±
wykonywaæ funkcje takie jak szyfrowanie, podpisywanie,
odszyfrowywanie, weryfikacjê, analizê list kluczy i inne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:TEST_SHARED_MEMORY=1 TEST_FILE_CACHE=1 %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}/%{pnam}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS MANIFEST
%{perl_vendorlib}/%{pdir}/*.pm
%dir %{perl_vendorlib}/auto/%{pdir}/%{pnam}/*
%{_mandir}/man3/*
