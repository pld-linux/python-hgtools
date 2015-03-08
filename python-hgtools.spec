#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 classes and setuptools plugin for Mercurial and Git repositories
Summary(pl.UTF-8):	Klasy Pythona 2 oraz wtyczka setuptools do repozytoriów Mercurial oraz Git
# Name must match the python module/package name (as in 'import' statement)
Name:		python-hgtools
Version:	6.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/hgtools
Source0:	https://pypi.python.org/packages/source/h/hgtools/hgtools-%{version}.zip
# Source0-md5:	584d74b81b1efae3604c53086d1a3acb
URL:		https://bitbucket.org/jaraco/hgtools/
# remove BR: python-devel for 'noarch' packages.
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.612
%if %{with python2}
%{?with_tests:BuildRequires:	python-pytest}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
%{?with_tests:BuildRequires:	python3-pytest}
BuildRequires:	python3-setuptools
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
Requires:	python3-modules

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
%{__python} setup.py \
	build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.txt todo.txt
%{py_sitescriptdir}/hgtools
%{py_sitescriptdir}/hgtools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hgtools
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.txt todo.txt
%{py3_sitescriptdir}/hgtools
%{py3_sitescriptdir}/hgtools-%{version}-py*.egg-info
%endif
