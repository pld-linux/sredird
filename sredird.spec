Summary:	RFC 2217-compliant serial port redirector
Summary(pl):	Program przekierowuj±cy port szeregowy zgodny z RFC 2217
Name:		sredird
Version:	2.1.0
Release:	1
License:	GPL
Group:		Networking
Source0:	ftp://metalab.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sredird is a serial port redirector that is compliant with the RFC
2217 "Telnet Com Port Control Option" protocol. This protocol lets you
share a serial port through the network.

%description -l pl
sredird jest programem przekierowuj±cym port szeregowy zgodnym z RFC
2217 (Telnet Com Port Control Option protocol). Protokó³ ten pozwala
na udostêpnianie portu szeregowego przez sieæ.

%prep
%setup -q

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install sredird $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
