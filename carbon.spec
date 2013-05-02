%define name carbon
%define version 0.9.10
%define unmangled_version 0.9.10
%define release 1

Summary: Backend data caching and persistence daemon for Graphite
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: Apache Software License 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Chris Davis <chrismd@gmail.com>
Url: https://launchpad.net/graphite
Requires: python-twisted

%description
Carbon is one of the components of Graphite, and is responsible for receiving metrics over the network and writing them down to disk using a storage backend. 

%prep
%setup -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
