# TODO: longer description
Summary:	FSP client
Summary(pl.UTF-8):   Program klienta dla protokołu FSP
Name:		fspclient
Version:	0.91.0
Release:	1
License:	BSD-like
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/fspclient/%{name}-%{version}.tar.bz2
# Source0-md5:	58d196e1e8e4656be15d2ad7fb8bbf7d
URL:		http://fspclient.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSP protocol client.

%description -l pl.UTF-8
Program dla klienta protokołu FSP.

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
