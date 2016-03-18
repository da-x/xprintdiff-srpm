Summary:		Prints User Idle Time to Stdout
Name:			xprintidle
Version:		0.1
Release:		2%{?dist}
Source:			http://www.dtek.chalmers.se/~henoch/text/xprintidle/xprintidle-%{version}.tar.gz
URL:			http://www.dtek.chalmers.se/~henoch/text/xprintidle.html
Group:			System/X11/Utilities
Packager:		Dan Aloni <alonid@gmail.com>
License:		BSD License (revised)

BuildRequires:          libX11-devel
BuildRequires:          libxkbcommon-devel
BuildRequires:          libXScrnSaver-devel

%description
xprintidle is a small program that prints the user's idle time to stdout,
using the X screensaver extension. It is meant for use in scripts.

%prep
%setup -q

%build
%__make

%install
%__install -D -m 0755 xprintidle "%{buildroot}%{_bindir}/xprintidle"

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/xprintidle

%changelog
* Mon Mar 18 2016 Dan Aloni <alonid@gmail.com> 0.1-2
- repackaged for Fedora

* Mon Nov 21 2005 Pascal Bleser <guru@unixtech.be> 0.1-1
- new package
