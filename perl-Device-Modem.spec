#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses serial port)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Device
%define		pnam	Modem
Summary:	Device::Modem - a Perl class to interface generic modems (AT-compliant)
Summary(pl.UTF-8):	Device::Modem - perlowy interfejs do obsługi modemów szeregowych
Name:		perl-Device-Modem
Version:	1.50
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Device/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1c850ccc426f682f414cfd4d9d34155d
URL:		http://search.cpan.org/dist/Device-Modem/
BuildRequires:	perl-Device-SerialPort
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Perl extension to talk to AT compliant devices via serial
port.

%description -l pl.UTF-8
Jest to rozszerzenie Perla do obsługi urządzeń zgodnych z AT poprzez
port szeregowy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Device/*.pm
%dir %{perl_vendorlib}/Device/Modem
%{perl_vendorlib}/Device/Modem/*.pm
%dir %{perl_vendorlib}/Device/Modem/Log
%{perl_vendorlib}/Device/Modem/Log/*.pm
%dir %{perl_vendorlib}/Device/Modem/Protocol
%{perl_vendorlib}/Device/Modem/Protocol/*.pm
%{_mandir}/man3/*
