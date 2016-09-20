Summary:	      A cross platform comic reader and library manager.
Name:           yacreader
Version:        8.5.0
Release:        1
License:        GPL3+
URL:            http://www.yacreader.com/
Source0:        https://bitbucket.org/luisangelsm/yacreader/downloads/%{name}-%{version}-src.tar.xz
BuildRequires:  qt5-qtbase-devel, libqt5multimedia-devel, libqt5script-devel, libqt5declarative-devel
BuildRequires:  libpoppler-qt5-devel, libglu-devel, mesa-common-devel, desktop-file-utils

%description
A cross platform comic reader and library manager.

%prep
%setup -q

%build
qmake-qt5
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
#%make_install
INSTALL_ROOT=%{buildroot} make install

%files
%{_bindir}/*
%{_datadir}/*
%doc
