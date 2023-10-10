%global commit0 4de681c193d45b14f87efc30e3e3f02d389387b5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20231006

Name:           libfdk-aac
Version:        2.0.2
Release:        3.%{date}git%{shortcommit0}%{?dist}
Epoch:          1
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library
License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        https://github.com/mstorsjo/fdk-aac/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Provides:       fdk-aac = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-free = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-free%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac-free < %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Fraunhofer FDK Advanced Audio Coding Codec Library for Android.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-free-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-free-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac-free-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n fdk-aac-%{commit0}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license NOTICE
%doc ChangeLog
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.%{version}

%files devel
%doc documentation/*
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/fdk-aac.pc

%changelog
* Tue Oct 10 2023 Simone Caronni <negativo17@gmail.com> - 1:2.0.2-3.20231006git4de681c
- Update to latest snapshot.

* Sat Mar 11 2023 Simone Caronni <negativo17@gmail.com> - 1:2.0.2-2.20220531git3f864cc
- Update to latest snapshot.

* Fri Sep 17 2021 Simone Caronni <negativo17@gmail.com> - 1:2.0.2-1
- Update to 2.0.2.

* Sun Apr 25 2021 Simone Caronni <negativo17@gmail.com> - 1:2.0.1-2
- Be more explicit about library sonames.

* Sun Oct 20 2019 Simone Caronni <negativo17@gmail.com> - 1:2.0.1-1
- Update to 2.0.1.

* Fri Mar 01 2019 Simone Caronni <negativo17@gmail.com> - 1:2.0.0-1
- Update to 2.0.0.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1:0.1.6-2
- Add GCC build requirement.

* Fri Jun 29 2018 Simone Caronni <negativo17@gmail.com> - 1:0.1.6-1
- Update to 0.1.6.
- Clean up SPEC file.

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
