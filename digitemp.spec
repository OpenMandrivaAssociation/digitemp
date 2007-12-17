Summary:	Digital thermometer using DS1820 1-wire sensors
Name:		digitemp
Version:	3.5.0
Release:	%mkrel 2
License:	GPL
Group:		Monitoring
URL:		http://www.digitemp.com/
Source0:	http://www.digitemp.com/software/linux/%{name}-%{version}.tar.bz2
Source1:	http://www.brianlane.com/linux/dthowto.txt
Source2:	DS9097_Schematic.gif
Patch0:		%{name}-opt.patch
BuildRequires:	libusb-devel
#BuildRequires:	lockdev-devel

%description
DigiTemp is a simple to use interface to the Dallas Semiconductor DS18S20,
DS1822, and DS18B20 1-wire digital temperature sensors. You can use DigiTemp
in a wide variety of applications, such as heating control, process monitoring,
weather station, indor/outdoor temperature logging, etc. It includes a couple
of useful Perl, Python and RRD Tool scripts for crating graphs and dynamic
signatures.

%prep

%setup -q
%patch0 -p1

cp %{SOURCE1} %{SOURCE2} .

%build
export OPT="%{optflags}"

%make ds9097
%make ds9097u
%make ds2490

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install digitemp_DS* %{buildroot}%{_bindir}/
install %{name}.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS DS9097_S* FAQ README TODO dthowto.txt perl python rrdb
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*


