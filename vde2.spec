Summary:	VDE2: Virtual Distributed Ethernet
Summary(pl.UTF-8):	VDE2: wirtualny rozproszony ethernet
Name:		vde2
Version:	2.3.3
Release:	1
License:	LGPL v2.1+ (libvdeplug), GPL v2+ (the rest)
Group:		Networking/Utilities
Source0:	https://github.com/virtualsquare/vde-2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d73411e88975a9f7c9cb4c2b0ad32d15
Patch0:		%{name}-pathmax.patch
Patch1:		%{name}-pc.patch
URL:		https://github.com/virtualsquare/vde-2
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	rpm-pythonprov
BuildRequires:	wolfssl-devel
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	vde < 2
Obsoletes:	python-vde2 < 2.3.3
Obsoletes:	python3-vde2 < 2.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# expects "prompt" symbol from user
%define		skip_post_check_so	libvdehist.*

%description
VDE2: Virtual Distributed Ethernet. It creates the abstraction of a
virtual ethernet: a single vde can be accessed by virtual and real
computers.

%description -l pl.UTF-8
VDE2: wirtualny rozproszony ethernet. Narzędzie to tworzy abstrakcyjny
wirtualny ethernet - pojedynczy vde może być dostępny z wirtualnych
jak i rzeczywistych komputerów.

%package libs
Summary:	VDE2 libraries
Summary(pl.UTF-8):	Biblioteki VDE2
Group:		Libraries
Conflicts:	vde2 < 2.3.2

%description libs
VDE2 libraries.

%description libs -l pl.UTF-8
Biblioteki VDE2.

%package devel
Summary:	Header files for VDE2 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek VDE2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for VDE2 libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek VDE2.

%package static
Summary:	Static VDE2 library
Summary(pl.UTF-8):	Statyczna biblioteka VDE2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VDE2 library.

%description static -l pl.UTF-8
Statyczna biblioteka VDE2.

%prep
%setup -q -n vde-2-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvde*.la
# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/vde2/libvdetap.{la,a}
# libs .la kept - no Requires/Libs.private

# tools removed in 2.3.3
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/{slirpvde,unixterm,vde_cryptcab,vde_l3,vde_vxlan,vdekvm,vdeq,vdeqemu}.1*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/vde_tunctl.8*

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog README
%dir %{_sysconfdir}/vde2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/vdecmd
%dir %{_sysconfdir}/vde2/libvdemgmt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/asyncrecv.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/closemachine.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/openmachine.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/sendcmd.rc
%attr(755,root,root) %{_bindir}/dpipe
%attr(755,root,root) %{_bindir}/unixcmd
%attr(755,root,root) %{_bindir}/vde_autolink
%attr(755,root,root) %{_bindir}/vde_cryptcab
%attr(755,root,root) %{_bindir}/vde_over_ns
%attr(755,root,root) %{_bindir}/vde_pcapplug
%attr(755,root,root) %{_bindir}/vde_plug
%attr(755,root,root) %{_bindir}/vde_plug2tap
%attr(755,root,root) %{_bindir}/vde_router
%attr(755,root,root) %{_bindir}/vde_switch
%attr(755,root,root) %{_bindir}/vdecmd
%attr(755,root,root) %{_bindir}/vdeterm
%attr(755,root,root) %{_bindir}/wirefilter
%attr(755,root,root) %{_libexecdir}/vdetap
%dir %{_libdir}/vde2
%attr(755,root,root) %{_libdir}/vde2/libvdetap.so
%{_mandir}/man1/dpipe.1*
%{_mandir}/man1/unixcmd.1*
%{_mandir}/man1/vde_autolink.1*
%{_mandir}/man1/vde_over_ns.1*
%{_mandir}/man1/vde_pcapplug.1*
%{_mandir}/man1/vde_plug.1*
%{_mandir}/man1/vde_plug2tap.1*
%{_mandir}/man1/vde_router.1*
%{_mandir}/man1/vde_switch.1*
%{_mandir}/man1/vdecmd.1*
%{_mandir}/man1/vdetaplib.1*
%{_mandir}/man1/vdeterm.1*
%{_mandir}/man1/wirefilter.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvdehist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvdehist.so.0
%attr(755,root,root) %{_libdir}/libvdemgmt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvdemgmt.so.0
%attr(755,root,root) %{_libdir}/libvdeplug.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvdeplug.so.3
%attr(755,root,root) %{_libdir}/libvdesnmp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvdesnmp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvdehist.so
%attr(755,root,root) %{_libdir}/libvdemgmt.so
%attr(755,root,root) %{_libdir}/libvdeplug.so
%attr(755,root,root) %{_libdir}/libvdesnmp.so
%{_includedir}/libvdehist.h
%{_includedir}/libvdemgmt.h
%{_includedir}/libvdeplug.h
%{_includedir}/libvdeplug_dyn.h
%{_includedir}/libvdesnmp.h
%{_pkgconfigdir}/vdehist.pc
%{_pkgconfigdir}/vdemgmt.pc
%{_pkgconfigdir}/vdeplug.pc
%{_pkgconfigdir}/vdesnmp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvdehist.a
%{_libdir}/libvdemgmt.a
%{_libdir}/libvdeplug.a
%{_libdir}/libvdesnmp.a
