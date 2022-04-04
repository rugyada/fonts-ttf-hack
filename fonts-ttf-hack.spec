Name:		fonts-ttf-hack
Version:	3.003
Release:	1
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
%setup -qn %{name}

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/hack
cp * %{buildroot}%{_datadir}/fonts/TTF/hack/

