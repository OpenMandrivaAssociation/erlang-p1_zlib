%global srcname p1_zlib
# The Fedora Erlang convention is to avoid separating the debug symbols:
# https://fedoraproject.org/wiki/User:Peter/Erlang_Packaging_Guidelines
%global debug_package %{nil}
%define _disable_ld_no_undefined 1

Name:       erlang-%{srcname}
Version:    1.0.0
Release:    %mkrel 2
Group:      Development/Erlang
Summary:    Native zlib driver for Erlang

License:    GPLv2
URL:        https://github.com/processone/ezlib/
Source0:    https://github.com/processone/ezlib/archive/%{version}.tar.gz
Patch0:     ldflags.patch

BuildRequires: erlang-eunit
BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros
BuildRequires: zlib-devel

Requires: erlang-erts


%description
A native zlib driver for Erlang, used by ejabberd.


%prep
%autosetup -n ezlib-%{version}


%build
%configure --enable-nif
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -Dpm644 -t $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/ebin ebin/* 
install -pm755 priv/lib/ezlib_drv.so \
    $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/


%files
%license COPYING
%{_erllibdir}/%{srcname}-%{version}



%changelog
* Sat May 07 2016 neoclust <neoclust> 1.0.0-2.mga6
+ Revision: 1010436
- imported package erlang-p1_zlib

