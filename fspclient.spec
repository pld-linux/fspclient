# TODO: longer description
Summary:	FSP client
Summary(pl):	Program klienta dla protoko³u FSP
Name:		fspclient
Version:	0.90.0
Release:	1
License:	BSD-like
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/fspclient/%{name}-%{version}.tar.bz2
# Source0-md5:	554cec4b3a409415e307ba7f3eed857a
URL:		http://fspclient.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSP protocol client.

%description -l pl
Program dla klienta protoko³u FSP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO fsprc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
