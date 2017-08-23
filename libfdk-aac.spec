Name:           libfdk-aac
Version:        0.1.5
Release:        7%{?dist}
Epoch:          1
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library
License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        http://downloads.sourceforge.net/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz

Provides:       fdk-aac = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac < %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Fraunhofer FDK Advanced Audio Coding Codec Library for Android.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn fdk-aac-%{version}

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license NOTICE
%{_libdir}/*.so.*

%files devel
%doc documentation/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc

%changelog
* Tue Aug 22 2017 Simone Caronni <negativo17@gmail.com> - 1:0.1.5-7
- Update to final 0.1.5.

* Sat Oct 08 2016 Simone Caronni <negativo17@gmail.com> - 1:0.1.5-6.20160924gitcb57d89
- Update to latest snapshot.
- Use packaging guidelines for snapshot format.
- Bump Epoch.
- Provide/obsolete fdk-aac.

* Mon Aug 15 2016 Simone Caronni <negativo17@gmail.com> - 0.1.4-5
- Add git patch.
- Fix building with GCC 6.1+.

* Wed Apr 20 2016 Simone Caronni <negativo17@gmail.com> - 0.1.4-4
- Override C++ flags for GCC 6+.

* Tue Apr 19 2016 Simone Caronni <negativo17@gmail.com> - 0.1.4-3
- Fix package summary and source URL.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 0.1.4-2
- Fix license and description.

* Fri Nov 13 2015 Simone Caronni <negativo17@gmail.com> - 0.1.4-1
- First build.
