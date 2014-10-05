Summary:	Disposable Soft Synth Interface specification
Name:		dssi
Version:	1.1.1
Release:	3
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	http://downloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
# Source0-md5:	619ab73c883b02dc37ddb37001591f8b
URL:		http://dssi.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
Requires:	alsa-lib-devel
Requires:	ladspa-devel
Obsoletes:	dssi-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common environment for DSSI plugins.

%package devel
Summary:	Common environment for DSSI plugins
Group:		Libraries

%description devel
DSSI (pronounced "dizzy") is an API for audio plugins, with particular
application for software synthesis plugins with native user
interfaces. DSSI is an open specification developed for use in Linux
audio applications, although portable to other platforms. It may be
thought of as LADSPA-for-instruments, or something comparable to VSTi.

DSSI consists of a C language API for use by plugins and hosts, based
on the LADSPA API, and an OSC (Open Sound Control) API for use in user
interface to host communications. The DSSI specification consists of
an RFC which describes the background for the proposal and defines the
OSC part of the specification, and a documented header file which
defines the C API.

%package host-jack
Summary:	A simple JACK/ALSA-sequencer plugin host
Group:		Applications/Sound

%description host-jack
A simple JACK/ALSA-sequencer plugin host.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/dssi

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/TODO doc/*.txt
%dir %{_libdir}/dssi

%files devel
%defattr(644,root,root,755)
%{_includedir}/dssi.h
%{_pkgconfigdir}/dssi.pc

%files host-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jack-dssi-host
%{_mandir}/man1/jack-dssi-host.1*

