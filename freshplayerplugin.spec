Name:		freshplayerplugin
Version:	0.3.5
Release:	1%{?dist}
Summary:	PPAPI-host NPAPI-plugin adapter

License:	MIT
URL:		https://github.com/i-rinat/freshplayerplugin
Source0:	https://github.com/i-rinat/freshplayerplugin/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	chrpath
BuildRequires:	ragel
BuildRequires:	alsa-lib-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	libX11-devel
BuildRequires:	libconfig-devel
BuildRequires:	libevent-devel
BuildRequires:	openssl-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXcursor-devel
BuildRequires:	pango-devel
BuildRequires:	gtk2-devel
BuildRequires:	mesa-libGLES-devel
BuildRequires:	libvdpau-devel
BuildRequires:	libva-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libv4l-devel
BuildRequires:	soxr-devel

Requires:	google-chrome-stable%{?_isa}

%description
For various reasons Firefox developers are not interested now in implementing
PPAPI in Firefox. However that does not mean it cannot be done.

The main goal of this project is to get PPAPI (Pepper) Flash player working in
Firefox. This can be done in two ways. First one is to implement full PPAPI
interface in Firefox itself. Other one is to implement a wrapper, some kind of
adapter which will look like browser to PPAPI plugin and look like NPAPI plugin
for browser.

%prep
%setup -q

%build
mkdir -p build
pushd build
%{cmake} ..
%{make_build}
popd

%install
install -Dm 755 build/libfreshwrapper-flashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/libfreshwrapper-flashplayer.so
install -Dm 644 data/freshwrapper.conf.example %{buildroot}%{_sysconfdir}/freshwrapper.conf
find %{buildroot} -name "*" -exec chrpath --delete {} \; 2>/dev/null

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ChangeLog README.md doc/*
%license LICENSE COPYING
%{_libdir}/mozilla/plugins/libfreshwrapper-flashplayer.so
%{_sysconfdir}/freshwrapper.conf


%changelog
* Sun Apr 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.3.5-1
- update to 0.3.5

* Mon Dec 21 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.3.4-2
- update to 0.3.4

* Sun Oct 11 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.3.3-1
- update to 0.3.3

* Sun Aug 23 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.3.2-1
- update to 0.3.2

* Fri Jul 17 2015 Leigh Scott <leigh123linux@googlemail.com> - 0.3.1-1
- Initial build

