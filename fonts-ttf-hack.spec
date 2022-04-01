%define pkgname hack-fonts-ttf
%define name Hack
%define extraver -ttf

Summary:	Hack ttf fonts
Name:		fonts-ttf-hack
Version:	v3.003
Release:	1
License:	MIT License Bitstream Vera License
Group:		System/Fonts/True type
Url:		https://sourcefoundry.org/hack/
Source0:	https://github.com/source-foundry/Hack/releases/download/%{version}/%{name}-%{version}-%{extraver}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools

%description
A typeface designed for source code.

%prep
%autosetup -n %{pkgname}-%{version}-%{extraver} -p1

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

