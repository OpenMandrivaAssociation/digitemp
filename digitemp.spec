Summary:	Digital thermometer using DS1820 1-wire sensors
Name:		digitemp
Version:	3.6.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Monitoring
URL:		http://www.digitemp.com/
Source0:	http://www.digitemp.com/software/linux/%{name}-%{version}.tar.gz
Source1:	http://www.brianlane.com/linux/dthowto.txt
Source2:	DS9097_Schematic.gif
Patch0:		%{name}-opt.patch
Patch1:		%{name}-str_fmt.patch
BuildRequires:	libusb-devel
#BuildRequires:	lockdev-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch1 -p1

cp %{SOURCE1} %{SOURCE2} .

%build
export OPT="%{optflags}"

%make ds9097

%make clean
%make ds9097u

%make clean
%make ds2490

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -pm0755 digitemp_DS* %{buildroot}%{_bindir}/
install -pm0644 %{name}.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CREDITS DS9097_S* FAQ README TODO dthowto.txt perl python rrdb
%{_bindir}/*
%{_mandir}/man1/*
