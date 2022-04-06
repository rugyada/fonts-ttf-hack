%define name fonts-ttf-hack
%define version 3.003
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary:	Hack ttf fonts
License:	MIT License Bitstream Vera License
Group:		System/Fonts/True type
Url:		https://sourcefoundry.org/hack/
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
A typeface designed for source code.

%files
%dir %{_datadir}/fonts/TTF/hack/
%{_datadir}/fonts/TTF/hack/*

%prep
%setup -qn %{name}-%{version}/fonts/TTF/hack/

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/hack
install -Dm 755  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/hack/
