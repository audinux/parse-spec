# Tag: plugin
# Type: plugin, LV2
# Category: Audio

Name:    ams-lv2
Version: 1.2.2
Release: 3%{?dist}
Summary: AMS LV2 set of plugins (from Alsa Modular Synth)
License: GPLv2+
URL:     https://github.com/blablack/ams-lv2

Source0: https://github.com/blablack/ams-lv2/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: python2
BuildRequires: gtkmm24-devel
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: lvtk
BuildRequires: fftw-devel

%description
AMS LV2 set of plugins synth (from Alsa Modular Synth)

%prep
%autosetup -n %{name}-%{version}

sed -i -e "s/lvtk-plugin-1/lvtk-plugin-2/g" wscript
sed -i -e "s/lvtk-ui-1/lvtk-ui-2/g" wscript
sed -i -e "s/lvtk-gtkui-1/lvtk-gtkui-2/g" wscript

for Files in src/*.cpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done
for Files in src/*.hpp ; do sed -i -e "s/lvtk-1/lvtk-2/g" $Files; done

# For Fedora 29
%if 0%{?fedora} >= 29
  find . -type f -exec sed -i -e "s/env python/env python2/g" {} \;
%endif

%build

%set_build_flags

./waf configure --destdir=%{buildroot} --libdir=%{_libdir}
./waf

%install 
./waf -j1 install --destdir=%{buildroot}

%files
%doc README.md THANKS
%license LICENSE
%{_libdir}/lv2/*

%changelog
* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-3
- fix debug build

* Wed Apr 22 2020 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-2
- update for Fedora 32

* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.2.2-1
- update 1.2.2-1

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- update for Fedora 29

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.2.1-1
- Initial build
