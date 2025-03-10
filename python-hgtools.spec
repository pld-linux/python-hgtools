#
# Conditional build:
%bcond_with	tests	# test target [pytest-runner doesn't support build-base]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 classes and setuptools plugin for Mercurial and Git repositories
Summary(pl.UTF-8):	Klasy Pythona 2 oraz wtyczka setuptools do repozytoriów Mercurial oraz Git
Name:		python-hgtools
Version:	6.5.1
Release:	9
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/hgtools/
Source0:	https://pypi.python.org/packages/source/h/hgtools/hgtools-%{version}.tar.gz
# Source0-md5:	ce8413687e43d5626cdcfee5024a9bc0
URL:		https://bitbucket.org/jaraco/hgtools/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
%{?with_tests:BuildRequires:	python-backports.unittest_mock}
%{?with_tests:BuildRequires:	python-pytest >= 2.8}
%{?with_tests:BuildRequires:	python-pytest-runner}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm >= 1.9
%endif
%if %{with python3}
%{?with_tests:BuildRequires:	python3-backports.unittest_mock}
%{?with_tests:BuildRequires:	python3-pytest >= 2.8}
%{?with_tests:BuildRequires:	python3-pytest-runner}
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm >= 1.9
BuildRequires:	python3-modules >= 1:3.2
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

%description -l pl.UTF-8
hgtools dobudowuje wtyczkę setuptools_hg dla setuptools. Zapewnia
klasy do przeglądania orazy pracy z repozytoriami systemów kontroli
wersji (VCS) Mercurial oraz Git.

%package -n python3-hgtools
Summary:	Python 3 classes and setuptools plugin for Mercurial and Git repositories
Summary(pl.UTF-8):	Klasy Pythona 3 oraz wtyczka setuptools do repozytoriów Mercurial oraz Git
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-hgtools
hgtools builds on the setuptools_hg plugin for setuptools. hgtools
provides classes for inspecting and working with repositories in the
Mercurial and Git version control systems (VCS).

%description -n python3-hgtools -l pl.UTF-8
hgtools dobudowuje wtyczkę setuptools_hg dla setuptools. Zapewnia
klasy do przeglądania orazy pracy z repozytoriami systemów kontroli
wersji (VCS) Mercurial oraz Git.

%prep
%setup -q -n hgtools-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/hgtools
%{py_sitescriptdir}/hgtools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hgtools
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/hgtools
%{py3_sitescriptdir}/hgtools-%{version}-py*.egg-info
%endif
