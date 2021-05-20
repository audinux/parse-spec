# Tag: plugin
# Type: VST
# Category: Audio

# Global variables for github repository
%global commit0 12785bb45db400eeddd79c11d830320a070bb4ca
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    airwindows
Version: 0.0.1
Release: 27%{?dist}
Summary: A set of VST2 plugins
License: MIT
URL:     https://github.com/airwindows/airwindows

Vendor:       Audinux
Distribution: Audinux

Source0: https://github.com/airwindows/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: wget
BuildRequires: unzip
BuildRequires: cmake

%description
A set of VST plugins

%prep
%autosetup -n %{name}-%{commit0}

unzip %{SOURCE1}

# Build a shared lib instead of a module to be able to get debug symnols
sed -i -e "s/MODULE/SHARED/g" plugins/LinuxVST/Helpers.cmake

mkdir -p plugins/LinuxVST/include/vstsdk/
mkdir -p plugins/LinuxVST/include/vstsdk/pluginterfaces/vst2.x/

cp VST_SDK/VST2_SDK/pluginterfaces/vst2.x/*    plugins/LinuxVST/include/vstsdk/pluginterfaces/vst2.x/
cp VST_SDK/VST2_SDK/public.sdk/source/vst2.x/* plugins/LinuxVST/include/vstsdk/

sed -i -e "s/add_subdirectory/include_directories/g"     plugins/LinuxVST/CMakeLists.txt
sed -i -e "s/add_compile_options/#add_compile_options/g" plugins/LinuxVST/CMakeLists.txt

# sources cleanup
rm -rf plugins/MacAU
rm -rf plugins/MacVST
rm -rf plugins/WinVST
rm -rf plugins/*.zip

%build

cd plugins/LinuxVST

%cmake -DCMAKE_BUILD_TYPE=RELEASE

%cmake_build 

%install 

cd plugins/LinuxVST/

install -m 755 -d %{buildroot}%{_libdir}/vst/
install -m 755 %{__cmake_builddir}/*.so %{buildroot}/%{_libdir}/vst/

%files
%doc plugins/LinuxVST/README.md
%license plugins/LinuxVST/LICENSE
%{_libdir}/*

%changelog
* Fri May 07 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-27
- update to 12785bb45db400eeddd79c11d830320a070bb4ca

* Sat Apr 24 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-26
- update to 7337eb6c32be3f00f1f79332e7f3e11434ad1cd6

* Mon Apr 12 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-25
- update to 4f0f40165314f5f0281209eb3f18bd7016b42d75

* Mon Apr 05 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-24
- update to b6d655bad82b89bef1b5c0570e23a96dd443cb29

* Mon Mar 29 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-23
- update to a3569b22e96a8c458f5fed129e611b80793fbe92

* Sun Mar 21 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-22
- update to 450b0c513d9743be4ef9aeed39d01e67111b5a44

* Mon Mar 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-21
- update to e4e38318a41f15515c32ba0c41cda0d824f5580f

* Mon Mar 8 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-20
- update to 7bb7fde13a9c94af242835823b813e6bcd0f20c8

* Mon Mar 1 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-19
- update to 68d733204a1d12a2d05045ed57d973b4a386bc30

* Mon Feb 22 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-18
- update to 3980dcb3d19bb2e2645d1c825fcea1bad3ee7adc

* Mon Feb 15 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-17
- update to 690897408f7ada94fdae90f3cf2a41ce8c9e1080

* Mon Feb 8 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-16
- update to f885ba303eaab68a8de079400c37c9cbf82b37c9

* Mon Feb 1 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-15
- update to 125b760f469e532f701e43602b01dc49c043d72a

* Mon Jan 25 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-14
- update to d8884ef296bc7073e10d19fc6611de6d1ad1b976

* Mon Jan 11 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-13
- update to e36d8abd86ed7fbf6507eff0a1b52fef7db1d5dc

* Wed Jan 6 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-12
- update to 3d92bfb6ea84f32c7d059d77aa83d263293a52b1

* Mon Jan 4 2021 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-11
- update to 57dea44c96ec17445b06d3c45d05fd9af42528bc

* Mon Dec 28 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-10
- update to b155145346207aca5febd9c8820e5c25d41a53b2

* Mon Dec 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-9
- update to cfd9507cae7ff327c36ae36d602487aa6e0857cc

* Mon Dec 14 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-8
- update to 6ed6016b79e43b3c3183d95ed6f4a2de890c284e

* Mon Dec 7 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-7
- update to 5b6c3dbce336f714b885d5b72ddd478f823d0bb8

* Mon Nov 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-6
- update to 2a06dc45b2b19fcce91e9abfeaa7124791868498

* Mon Nov 16 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-5
- update to 8e70eedbaeb7998a276331eb5eeb1015b1bc8807

* Mon Oct 26 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-4
- update to bda54733c70a8857bea04a3511e0c247acee79e1

* Mon Oct 19 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-3
- update to 6eb63993bc6b04b7000846fb9b122e2b6469bddd

* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-2
- update to fa61072ea31a876ab28d80bf5edcae717ab6ddf3 - fix for fedora 33

* Wed Jul 29 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file
