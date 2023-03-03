#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cryptography_vectors
Version  : 39.0.2
Release  : 124
URL      : https://files.pythonhosted.org/packages/ef/d3/2deb4eb1aac6ba55a093f15a37e5dcf5eaa846741544e0b301776a767311/cryptography_vectors-39.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ef/d3/2deb4eb1aac6ba55a093f15a37e5dcf5eaa846741544e0b301776a767311/cryptography_vectors-39.0.2.tar.gz
Summary  : Test vectors for the cryptography package.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pypi-cryptography_vectors-license = %{version}-%{release}
Requires: pypi-cryptography_vectors-python = %{version}-%{release}
Requires: pypi-cryptography_vectors-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
********************************************
* Instructions for posting to LDAP Servers *
********************************************

%package license
Summary: license components for the pypi-cryptography_vectors package.
Group: Default

%description license
license components for the pypi-cryptography_vectors package.


%package python
Summary: python components for the pypi-cryptography_vectors package.
Group: Default
Requires: pypi-cryptography_vectors-python3 = %{version}-%{release}

%description python
python components for the pypi-cryptography_vectors package.


%package python3
Summary: python3 components for the pypi-cryptography_vectors package.
Group: Default
Requires: python3-core
Provides: pypi(cryptography_vectors)

%description python3
python3 components for the pypi-cryptography_vectors package.


%prep
%setup -q -n cryptography_vectors-39.0.2
cd %{_builddir}/cryptography_vectors-39.0.2
pushd ..
cp -a cryptography_vectors-39.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677859635
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cryptography_vectors
cp %{_builddir}/cryptography_vectors-%{version}/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-cryptography_vectors/de33ead2bee64352544ce0aa9e410c0c44fdf7d9 || :
cp %{_builddir}/cryptography_vectors-%{version}/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-cryptography_vectors/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cryptography_vectors/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
/usr/share/package-licenses/pypi-cryptography_vectors/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
