Summary:	VDE2: Virtual Distributed Ethernet
Summary(pl.UTF-8):	VDE2: wirtualny rozproszony ethernet
Name:		vde2
Version:	2.2.2
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	b198b92d511e4a6276b3bc87dfebe5d7
Patch0:		%{name}-pathmax.patch
URL:		http://sourceforge.net/projects/vde/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDE2: Virtual Distributed Ethernet. It creates the abstraction of a
virtual ethernet: a single vde can be accessed by virtual and real
computers.

%description -l pl.UTF-8
VDE2: wirtualny rozproszony ethernet. Narzędzie to tworzy abstrakcyjny
wirtualny ethernet - pojedynczy vde może być dostępny z wirtualnych
jak i rzeczywistych komputerów.

%package devel
Summary:	Header files for VDE2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki VDE2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VDE2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki VDE2.

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
%setup -q 
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install  \
	DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{_bindir}/vdeqemu
#ln -sf vdeq $RPM_BUILD_ROOT%{_bindir}/vdeqemu

rm -f $RPM_BUILD_ROOT%{_libdir}/vde2/libvdetap.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sysconfdir}/vde2
%dir %{_sysconfdir}/vde2/libvdemgmt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/vdecmd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/asyncrecv.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/closemachine.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/openmachine.rc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde2/libvdemgmt/sendcmd.rc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libvde*.so.*.*.*
%attr(755,root,root) %{_libdir}/libvde*.so.0
%attr(755,root,root) %{_libdir}/libvde*.so.2
%dir %{_libdir}/vde2
%dir %{_libdir}/vde2/vde_l3
%{_libdir}/vde2/libvdetap.la
%{_libdir}/vde2/vde_l3/*.la
%{_libdir}/vde2/vde_l3/*.so
%attr(755,root,root) %{_libdir}/vde2/libvdetap.so
%attr(755,root,root) %{_libdir}/vdetap
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvde*.so
%{_libdir}/libvde*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvde*.a
