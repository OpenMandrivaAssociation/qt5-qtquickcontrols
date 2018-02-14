%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtquickcontrols
Version:	5.10.1
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtquickcontrols-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%(echo %{beta} |sed -e "s,1$,,")/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtquickcontrols-everywhere-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Source100:	%{name}.rpmlintrc
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
Examples for the QtQuick Controls library

%files examples
%{_qt5_prefix}/examples/quickcontrols

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5
%make

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
