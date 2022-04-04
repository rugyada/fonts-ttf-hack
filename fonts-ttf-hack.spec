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

%prep
%autosetup -n %{name}-%{version} -p1

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/hack
install -m 644 ttf/*.ttf %{buildroot}%{_datadir}/fonts/TTF/hack
ttmkfdir %{buildroot}%{_datadir}/fonts/TTF/hack > %{buildroot}%{_datadir}/fonts/TTF/hack/fonts.dir
ln -s fonts.dir %{buildroot}%{_datadir}/fonts/TTF/hack/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/hack \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-hack:pri=50

%files
%dir %{_datadir}/fonts/TTF/hack
%{_datadir}/fonts/TTF/hack/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/hack/fonts.dir
%{_datadir}/fonts/TTF/hack/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-hack:pri=50
