# Tag: editor
# Type: application
# Category: Audio

Name:    opn2bankeditor
Version: 1.3.0
Release: 2%{?dist}
Summary: A small cross-platform editor of the OPN2 FM banks of different formats
URL:     https://github.com/Wohlstand/OPN2BankEditor
License: GPLv3

Vendor:       Audinux
Distribution: Audinux

# ./opn2bankeditor-source.sh <tag>
# ./opn2bankeditor-source.sh v1.3

Source0: OPN2BankEditor.tar.gz
Source1: opn2bankeditor-source.sh

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: qwt-devel
BuildRequires: desktop-file-utils

%description
A small cross-platform editor of the OPN2 FM banks of different formats

%prep

%setup -qn OPN2BankEditor

sed -i -e "/Categories/d" src/resources/opn2_bank_editor.desktop

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DLIBEXEC_INSTALL_DIR=%{_libexecdir}

%cmake_build

%install

%cmake_install

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Audio \
        --add-category=AudioVideo \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/opn2_bank_editor.desktop

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/opn2_bank_editor.desktop

%files
%doc README.md changelog.txt
%license LICENSE license.txt
%{_bindir}/opn2_bank_editor
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/opn2_bank_editor/*

%changelog
* Thu Oct 1 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-2
- fix for Fedora 33

* Tue Jun 2 2020 Yann Collette <ycollette.nospam@free.fr> - 1.3.0-1
- initial release of the spec file
