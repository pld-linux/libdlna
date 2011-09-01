Summary:	DLNA library
Summary(pl.UTF-8):	Biblioteka DLNA
Name:		libdlna
Version:	0.2.3
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://libdlna.geexbox.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	2c974f95b711e5fd07f78fc4ebfcca66
Patch0:		%{name}-ffmpeg_paths.patch
Patch1:		%{name}-ffmpeg.patch
URL:		http://libdlna.geexbox.org
BuildRequires:	ffmpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdlna aims at being the reference open-source implementation of DLNA
(Digital Living Network Alliance) standards.

%package devel
Summary:	Header files for libdlna library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdlna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdlna library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdlna.

%package static
Summary:	Static libdlna library
Summary(pl.UTF-8):	Statyczna biblioteka libdlna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdlna library.

%description static -l pl.UTF-8
Statyczna biblioteka libdlna.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

%{__make} -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -fpic -Isrc"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libdlna.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdlna.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdlna.so
%{_includedir}/dlna.h
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdlna.a
