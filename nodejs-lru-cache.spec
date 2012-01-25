%define		git_hash 83b610b
%define		pkg	lru-cache
Summary:	A cache object that deletes the least recently used items
Name:		nodejs-%{pkg}
Version:	1.0.4
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-lru-cache
# download from https://github.com/isaacs/node-lru-cache/tarball/%%{version}
Source0:	isaacs-node-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	44deb216a31c660704f130671025be23
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cache object that deletes the least recently used items.

%prep
%setup -qc
mv isaacs-node-%{pkg}-*/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p lib/%{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}.js
