Summary:	A cross platform comic reader and library manager
Name:		yacreader
Version:	8.5.0
Release:	1
License:	GPL3+
URL:		http://www.yacreader.com/
Source0:	https://bitbucket.org/luisangelsm/yacreader/downloads/%{name}-%{version}-src.tar.xz
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  qt5-qtdeclarative
BuildRequires:	pkgconfig(poppler-qt5)

%description
A cross platform comic reader and library manager.

%prep
%setup -q

%build
%qmake_qt5
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/*
%{_datadir}/*
