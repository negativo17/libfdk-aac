Name:           libfdk-aac
Version:        0.1.4
Release:        4%{?dist}
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library

License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/
Source0:        http://downloads.sourceforge.net/opencore-amr/fdk-aac/fdk-aac-%{version}.tar.gz

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

%build
%if 0%{?fedora} > 23 || 0%{?rhel} > 8
# Override C++ flags for GCC 6+
export CXXFLAGS="%{optflags} -Wno-narrowing"
%endif

%configure --disable-static

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
* Wed Apr 20 2016 Simone Caronni <negativo17@gmail.com> - 0.1.4-4
- Override C++ flags for GCC 6+.

* Tue Apr 19 2016 Simone Caronni <negativo17@gmail.com> - 0.1.4-3
- Fix package summary and source URL.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 0.1.4-2
- Fix license and description.

* Fri Nov 13 2015 Simone Caronni <negativo17@gmail.com> - 0.1.4-1
- First build.
