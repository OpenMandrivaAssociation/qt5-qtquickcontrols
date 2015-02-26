%define api 5
%define major %api

%define qtminor 4
%define qtsubminor 1

%define qtversion %{api}.%{qtminor}.%{qtsubminor}

%define qttarballdir qtquickcontrols-opensource-src-%{qtversion}
%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtquickcontrols
Version:	%{qtversion}
Release:	1
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
Source0:	http://download.qt-project.org/official_releases/qt/%{api}.%{qtminor}/%{version}/submodules/%{qttarballdir}.tar.xz
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	pkgconfig(Qt5Gui) = %{version}
BuildRequires:	pkgconfig(Qt5Quick) = %{version}
BuildRequires:	qt5-qtquick-private-devel = %{version}

%description
Qt Quick Controls.

%files
%{_qt5_prefix}/qml/QtQuick/Controls
%{_qt5_prefix}/qml/QtQuick/Layouts
%{_qt5_prefix}/qml/QtQuick/Dialogs
%{_qt5_prefix}/qml/QtQuick/PrivateWidgets
%{_qt5_exampledir}/quick/dialogs

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5
%make

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
