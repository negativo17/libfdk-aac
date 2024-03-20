Name:           libfdk-aac
Version:        2.0.3
Release:        1%{?dist}
Epoch:          1
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library
License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        https://github.com/mstorsjo/fdk-aac/archive/v%{version}/fdk-aac-%{version}.tar.gz

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
%autosetup -n fdk-aac-%{version}

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
* Wed Mar 20 2024 Simone Caronni <negativo17@gmail.com> - 1:2.0.3-1
- Update to 2.0.3.
- Trim changelog.

* Tue Oct 10 2023 Simone Caronni <negativo17@gmail.com> - 1:2.0.2-3.20231006git4de681c
- Update to latest snapshot.

* Sat Mar 11 2023 Simone Caronni <negativo17@gmail.com> - 1:2.0.2-2.20220531git3f864cc
- Update to latest snapshot.

* Fri Sep 17 2021 Simone Caronni <negativo17@gmail.com> - 1:2.0.2-1
- Update to 2.0.2.

* Sun Apr 25 2021 Simone Caronni <negativo17@gmail.com> - 1:2.0.1-2
- Be more explicit about library sonames.
