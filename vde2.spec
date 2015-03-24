Summary:	VDE2: Virtual Distributed Ethernet
Summary(pl.UTF-8):	VDE2: wirtualny rozproszony ethernet
Name:		vde2
Version:	2.3.2
Release:	2
License:	LGPL v2.1+ (libvdeplug), BSD (slirpvde), GPL v2+ (the rest)
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	46fbc5f97f03dc517aa3b2c9d9ea6628
Patch0:		%{name}-pathmax.patch
Patch1:		%{name}-format.patch
URL:		http://sourceforge.net/projects/vde/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	%{name}-libs = %{version}-%{release}
Obsoletes:	vde < 2
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

%package -n python-vde2
Summary:	Python interface to VDE2
Summary(pl.UTF-8):	Pythonowy interfejs do VDE2
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}

%description -n python-vde2
Python interface to VDE2.

%description -n python-vde2 -l pl.UTF-8
Pythonowy interfejs do VDE2.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure  \
	--disable-silent-rules \
	--enable-kernel-switch

%{__make} -j1 \
	pythondir=%{py_sitedir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/vde2/libvdetap.{la,a}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/vde2/vde_l3/*.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/vdeplug_python.la
# libs .la kept - no Requires/Libs.private

cp -p src/slirpvde/README README.slirpvde

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING.slirpvde Changelog README README.slirpvde
%dir %{_sysconfdir}/vde2
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/vdecmd
%dir %{_sysconfdir}/vde2/libvdemgmt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/asyncrecv.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/closemachine.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/openmachine.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/sendcmd.rc
%attr(755,root,root) %{_bindir}/dpipe
%attr(755,root,root) %{_bindir}/kvde_switch
%attr(755,root,root) %{_bindir}/slirpvde
%attr(755,root,root) %{_bindir}/unixcmd
%attr(755,root,root) %{_bindir}/unixterm
%attr(755,root,root) %{_bindir}/vde_autolink
%attr(755,root,root) %{_bindir}/vde_cryptcab
%attr(755,root,root) %{_bindir}/vde_l3
%attr(755,root,root) %{_bindir}/vde_over_ns
%attr(755,root,root) %{_bindir}/vde_pcapplug
%attr(755,root,root) %{_bindir}/vde_plug
%attr(755,root,root) %{_bindir}/vde_plug2tap
%attr(755,root,root) %{_bindir}/vde_switch
%attr(755,root,root) %{_bindir}/vdecmd
%attr(755,root,root) %{_bindir}/vdekvm
%attr(755,root,root) %{_bindir}/vdeq
%attr(755,root,root) %{_bindir}/vdeqemu
%attr(755,root,root) %{_bindir}/vdeterm
%attr(755,root,root) %{_bindir}/wirefilter
%attr(755,root,root) %{_sbindir}/vde_tunctl
%attr(755,root,root) %{_libdir}/vdetap
%dir %{_libdir}/vde2
%attr(755,root,root) %{_libdir}/vde2/libvdetap.so
%dir %{_libdir}/vde2/vde_l3
%attr(755,root,root) %{_libdir}/vde2/vde_l3/bfifo.so
%attr(755,root,root) %{_libdir}/vde2/vde_l3/pfifo.so
%attr(755,root,root) %{_libdir}/vde2/vde_l3/tbf.so
%{_mandir}/man1/dpipe.1*
%{_mandir}/man1/slirpvde.1*
%{_mandir}/man1/unixcmd.1*
%{_mandir}/man1/unixterm.1*
%{_mandir}/man1/vde_autolink.1*
%{_mandir}/man1/vde_cryptcab.1*
%{_mandir}/man1/vde_l3.1*
%{_mandir}/man1/vde_over_ns.1*
%{_mandir}/man1/vde_pcapplug.1*
%{_mandir}/man1/vde_plug.1*
%{_mandir}/man1/vde_plug2tap.1*
%{_mandir}/man1/vde_switch.1*
%{_mandir}/man1/vdecmd.1*
%{_mandir}/man1/vdekvm.1*
%{_mandir}/man1/vdeq.1*
%{_mandir}/man1/vdeqemu.1*
%{_mandir}/man1/vdetaplib.1*
%{_mandir}/man1/vdeterm.1*
%{_mandir}/man1/wirefilter.1*
%{_mandir}/man8/vde_tunctl.8*

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
%{_libdir}/libvdehist.la
%{_libdir}/libvdemgmt.la
%{_libdir}/libvdeplug.la
%{_libdir}/libvdesnmp.la
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

%files -n python-vde2
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/vdeplug_python.so
%{py_sitedir}/VdePlug.py[co]
