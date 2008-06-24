Summary:	VDE2: Virtual Distributed Ethernet
Summary(pl.UTF-8):	VDE2: wirtualny rozproszony ethernet
Name:		vde2
Version:	2.2.1
Release:	0.1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	e7854f33e702abb0436b89048c944400
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libvde*.so.*.*.*
%dir %{_libdir}/vde2
%{_libdir}/vde2/libvdetap.la
%attr(755,root,root) %{_libdir}/vde2/libvdetap.so
%attr(755,root,root) %{_libdir}/vdetap
%{_mandir}/man1/*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvde*.so
%{_libdir}/libvde*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvde*.a
