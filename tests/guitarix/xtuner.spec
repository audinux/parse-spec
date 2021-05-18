Name:    xtuner
Version: 0.0.1
Release: 1%{?dist}
Summary: Tuner for Jack Audio Connection Kit
License: GPLv2+

URL:     https://github.com/brummer10/XTuner

# git clone https://github.com/brummer10/XTuner
# cd XTuner
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz XTuner.tar.gz XTuner/*
# rm -rf XTuner

Source0: XTuner.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: cairo-devel
BuildRequires: liblo-devel
BuildRequires: fftw-devel
BuildRequires: libsigc++20-devel
BuildRequires: zita-resampler-devel
BuildRequires: desktop-file-utils

%description
Tuner for Jack Audio Connection Kit

%prep
%autosetup -n XTuner

%build

%set_build_flags

%make_build CXXFLAGS="%build_cxxflags -I/usr/include/cairo -I/usr/include/sigc++-2.0/ -I/usr/%{_lib}/sigc++-2.0/include" STRIP=true

%install 

%make_install INSTALL_DIR=/usr/%{_lib}/lv2 STRIP=true

desktop-file-install                         \
  --add-category="Audio"                     \
  --delete-original                          \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/XTuner.desktop

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/XTuner.desktop
%{_datadir}/pixmaps/XTuner.png

%changelog
* Mon Sep 21 2020 Yann Collette <ycollette.nospam@free.fr> - 0.0.1-1
- Initial spec file - master / 9c686c90f845c066e2d4ef72d6335f0a428d3a25
