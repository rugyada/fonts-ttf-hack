Name:		fonts-ttf-hack
Version:	3.003
Release:	1
Summary:	Hack ttf fonts
License:	MIT License Bitstream Vera License
Group:		System/Fonts/True type
Url:		https://sourcefoundry.org/hack/
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
A typeface designed for source code.

%files
%dir %{_datadir}/fonts/TTF/hack
%{_datadir}/fonts/TTF/hack/*.ttf

%prep
%setup -qn %{name}-%{version}

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/hack
install -m 644 ttf/*.ttf %{buildroot}%{_datadir}/fonts/TTF/hack
cp * %{buildroot}%{_datadir}/fonts/TTF/hack
