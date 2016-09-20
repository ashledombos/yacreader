Name:           yacreader
Version:        8.5.0
Release:        19.1
Summary:	A cross platform comic reader and library manager.

License:        GPL3+
#URL:            
Source0:        	https://bitbucket.org/luisangelsm/yacreader/downloads/yacreader-%{version}-src.tar.xz



BuildRequires: qt5-qtbase-devel, libqt5multimedia-devel, libqt5script-devel, libqt5declarative-devel, libunarr-devel, libpoppler-qt5-devel, libglu-devel, mesa-common-devel, desktop-file-utils

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



%changelog
* Sat Oct 24 2015 herr_k
