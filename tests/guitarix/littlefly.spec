Name:    littlefly
Version: 1.0.0
Release: 1%{?dist}
Summary: A LV2 Overdrive/Distortion pedal simulation
License: GPLv2+
URL:     https://github.com/brummer10/LittleFly.lv2

# ./littlefly-source.sh <tag>
# ./littlefly-source.sh v1.0

Source0: LittleFly.lv2.tar.gz
Source1: littlefly-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: libsigc++20-devel

%description
A LV2 Overdrive/Distortion pedal simulation

%prep
%autosetup -n LittleFly.lv2

%build

%set_build_flags

%make_build STRIP=true

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

%files
%doc README.md
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 27 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
