%define major	0
%define libname	%mklibname gestures %{major}
%define devname	%mklibname -d gestures

Summary:	ChromiumOS libgestures modified to compile for Linux
Name:		libgestures
Version:	0.1
Release:	0.1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://chromium.googlesource.com/chromiumos/platform/gestures/
Source0:	%{name}.tar.bz2
BuildRequires:	jsoncpp-devel
BuildRequires:	gtest-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	udev-devel

%description
Gesture recognizer library

%package -n	%{libname}
Summary:	libgestures library from ChromiumOS
Group:		System/Libraries

%description -n	%{libname}
Gesture recognizer library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn %{name}

%build
sed -i 's!LIBDIR = /usr/lib!LIBDIR = %{_libdir}!g' Makefile
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}

%files -n %{devname}
%{_includedir}/gestures/*.h
%{_libdir}/%{name}.so
