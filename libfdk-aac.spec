%global commit0 cb57d89522806f8161fdbc05d1039e1a3ff5ef76
%global date 20160924
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libfdk-aac
Version:        0.1.5
Release:        6%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Epoch:          1
Summary:        Fraunhofer FDK Advanced Audio Coding Codec Library
License:        Software License for The Fraunhofer FDK AAC Codec Library for Android
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        https://sourceforge.net/code-snapshots/git/o/op/opencore-amr/fdk-aac.git/opencore-amr-fdk-aac-%{commit0}.zip#/fdk-aac-%{shortcommit0}.zip

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
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       fdk-aac-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       fdk-aac-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      fdk-aac-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn opencore-amr-fdk-aac-%{commit0}

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
