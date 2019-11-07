#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdesdk-kioslaves
Version  : 19.08.3
Release  : 14
URL      : https://download.kde.org/stable/applications/19.08.3/src/kdesdk-kioslaves-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/kdesdk-kioslaves-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/kdesdk-kioslaves-19.08.3.tar.xz.sig
Summary  : KDE SDK KIO-Slaves
Group    : Development/Tools
License  : GPL-2.0
Requires: kdesdk-kioslaves-data = %{version}-%{release}
Requires: kdesdk-kioslaves-lib = %{version}-%{release}
Requires: kdesdk-kioslaves-license = %{version}-%{release}
Requires: kdesdk-kioslaves-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : perl

%description
kio_perldoc - A kioslave interface to the imbedded Perl documentation.
Version: 0.9.1

%package data
Summary: data components for the kdesdk-kioslaves package.
Group: Data

%description data
data components for the kdesdk-kioslaves package.


%package lib
Summary: lib components for the kdesdk-kioslaves package.
Group: Libraries
Requires: kdesdk-kioslaves-data = %{version}-%{release}
Requires: kdesdk-kioslaves-license = %{version}-%{release}

%description lib
lib components for the kdesdk-kioslaves package.


%package license
Summary: license components for the kdesdk-kioslaves package.
Group: Default

%description license
license components for the kdesdk-kioslaves package.


%package locales
Summary: locales components for the kdesdk-kioslaves package.
Group: Default

%description locales
locales components for the kdesdk-kioslaves package.


%prep
%setup -q -n kdesdk-kioslaves-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573166946
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573166946
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdesdk-kioslaves
cp %{_builddir}/kdesdk-kioslaves-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/kdesdk-kioslaves/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
cp %{_builddir}/kdesdk-kioslaves-19.08.3/perldoc/COPYING %{buildroot}/usr/share/package-licenses/kdesdk-kioslaves/d6458d52bfead6f1399b865f1aeea0caa639ef6c
pushd clr-build
%make_install
popd
%find_lang kio5_perldoc

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kio_perldoc/pod2html.pl

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/kio/perldoc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdesdk-kioslaves/a21ac62aee75f8fcb26b1de6fc90e5eea271854c
/usr/share/package-licenses/kdesdk-kioslaves/d6458d52bfead6f1399b865f1aeea0caa639ef6c

%files locales -f kio5_perldoc.lang
%defattr(-,root,root,-)

