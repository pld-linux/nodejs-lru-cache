%define		pkg	lru-cache
Summary:	A cache object that deletes the least recently used items
Name:		nodejs-%{pkg}
Version:	2.3.0
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-lru-cache
Source0:	http://registry.npmjs.org/lru-cache/-/lru-cache-%{version}.tgz
# Source0-md5:	c1fe9e35d5b815987966f02dfa5c46a1
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cache object that deletes the least recently used items.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE AUTHORS
%{nodejs_libdir}/%{pkg}
