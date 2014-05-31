#sbs-git:slp/unmodified/libpng libpng 1.2.46 fcaa793c53a17a30625312c0e4e6de51383f2deb
Name:       libpng
Summary:    A library of functions for manipulating PNG image format files
Version:    1.2.50
Release:    2
Group:      System/Libraries
License:    zlib
URL:        http://www.libpng.org/pub/png/
Source0:    ftp://ftp.simplesystems.org/pub/png/src/libpng-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  zlib-devel

%description
The libpng package contains a library of functions for creating and
manipulating PNG (Portable Network Graphics) image format files.  PNG
is a bit-mapped graphics format similar to the GIF format.  PNG was
created to replace the GIF format, since GIF uses a patented data
compression algorithm.

Libpng should be installed if you need to manipulate PNG format image
files.



%package devel
Summary:    Development tools for programs to manipulate PNG image format files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libpng = %{version}-%{release}
Requires:   zlib-devel

%description devel
The libpng-devel package contains header files and documentation necessary
for developing programs using the PNG (Portable Network Graphics) library.



%prep
%setup -q -n %{name}-%{version}

%build

export CFLAGS+=" -fvisibility=hidden"
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 
rm -rf $RPM_BUILD_ROOT/usr/share/man
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
/usr/share/license/%{name}
%manifest libpng.manifest
%{_libdir}/libpng*.so.*

%files devel
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libpng*.so
%{_libdir}/pkgconfig/*

