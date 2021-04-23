Summary:	PySide version of lupdate/uic/rcc tools
Summary(pl.UTF-8):	Wersja PySide narzędzi lupdate/uic/rcc
Name:		pyside-tools
Version:	0.2.15
Release:	1
License:	GPL v2 (lupdate, rcc), BSD or GPL v2 (uic)
Group:		Development/Tools
#Source0Download: https://github.com/PySide/Tools/releases/
Source0:	https://github.com/pyside/Tools/archive/%{version}/Tools-%{version}.tar.gz
# Source0-md5:	e542b9536bd9d35599ede225c9311cc8
URL:		https://github.com/PySide/Tools
BuildRequires:	QtCore-devel >= 4.5.0
BuildRequires:	QtGui-devel >= 4.5.0
BuildRequires:	QtXml-devel >= 4.5.0
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	python-PySide-devel >= 1.0.6
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	sed >= 4.0
BuildRequires:	shiboken >= 1.1.1
Requires:	QtCore >= 4.5.0
Requires:	QtGui >= 4.5.0
Requires:	QtXml >= 4.5.0
Requires:	python-PySide >= 1.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the PySide version of lupdate, rcc and uic
utilities.

%description -l pl.UTF-8
Ten pakiet zawiera przeznaczone dla PySide wersje narzędzi lupdate,
rcc oraz uic.

%prep
%setup -q -n Tools-%{version}

%{__sed} -i -e '1s,^#!/usr/bin/env python,/usr/bin/python,' pyside-uic

%build
mkdir build
cd build
%cmake .. \
	-DPYTHON_BASENAME=-python%{py_ver} \
	-DPYTHON_SUFFIX=-python%{py_ver}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/pysideuic
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/pysideuic
# don't remove *.py from widget-plugins
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pysideuic/*.py \
	$RPM_BUILD_ROOT%{py_sitedir}/pysideuic/{Compiler,port_v2,port_v3}/*.py
# already installed in mandir
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pysideuic/pyside-uic.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE-uic
%attr(755,root,root) %{_bindir}/pyside-lupdate
%attr(755,root,root) %{_bindir}/pyside-rcc
%attr(755,root,root) %{_bindir}/pyside-uic
%{py_sitedir}/pysideuic
%{_mandir}/man1/pyside-lupdate.1*
%{_mandir}/man1/pyside-rcc.1*
%{_mandir}/man1/pyside-uic.1*
