Name:           libfdk-aac
Version:        0.1.4
Release:        5%{?dist}
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library
License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        http://downloads.sourceforge.net/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz
Patch0:         fdk-aac-git.patch

%description
Fraunhofer FDK Advanced Audio Coding Codec Library for Android.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn fdk-aac-%{version}
%patch0 -p1

%build
CXXFLAGS="%{optflags} -std=gnu++98"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license NOTICE
%doc ChangeLog
%{_libdir}/*.so.*

%files devel
%doc documentation/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc

%changelog
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
