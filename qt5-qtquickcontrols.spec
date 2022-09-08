%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtquickcontrols
Version:	5.15.6
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtquickcontrols-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtquickcontrols-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Source100:	%{name}.rpmlintrc
# From KDE
# [currently no patches]
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qmake5 = %{version}
BuildRequires:	pkgconfig(Qt5Gui) = %{version}
BuildRequires:	pkgconfig(Qt5Quick) = %{version}
BuildRequires:	pkgconfig(Qt5Widgets) = %{version}
BuildRequires:	pkgconfig(Qt5Sql) = %{version}
BuildRequires:	qt5-qtquick-private-devel = %{version}
BuildRequires:	qt5-qtqmlmodels-private-devel
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt Quick Controls.

%files
%{_qt5_prefix}/qml/QtQuick/Controls
%{_qt5_prefix}/qml/QtQuick/Dialogs
%{_qt5_prefix}/qml/QtQuick/Extras
%{_qt5_prefix}/qml/QtQuick/PrivateWidgets

#------------------------------------------------------------------------------
%package examples
Summary:	Examples for the QtQuick Controls library
Group:		Development/KDE and Qt

%description examples
Examples for the QtQuick Controls library.

%files examples
%{_qt5_prefix}/examples/quickcontrols

#------------------------------------------------------------------------------

%prep
%autosetup -n %(echo %qttarballdir |sed -e 's,-opensource,,') -p1
%{_qt5_prefix}/bin/syncqt.pl -version %{version}

%build
%qmake_qt5
%make_build

#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}
