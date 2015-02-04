Name:		startactive
Summary:	KDE User Interface for mobile Devices
Version:	0.4
Release:	1
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		http://plasma-active.org/
Source0:	%{name}-%{version}.tar.xz
Patch1:		0001-For-KDE4-on-openSUSE-the-dotfolder-is-called-.kde4.patch
Patch2:		0002-use-kwin-instead-of-kwinactive.patch
Patch4:		0004-explicitly-start-all-lnusertemp-modules.patch
Patch5:		0005-make-sure-dbus-is-started-and-encironment-variables-.patch
#Patch6:		add-correct-lib-suffix.patch
BuildRequires:	task-kde4-devel
Requires:	plasma-mobile = 0.5

%description
Starter Program for Plasma Active

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%defattr(755,root,root)
%_kde_bindir/startactive
%_kde_bindir/setup-kde-skel
%_kde_bindir/startactive.bin
%defattr(644,root,root)
%dir %_kde_appsdir
%dir %_kde_appsdir/ksplash
%dir %_kde_appsdir/ksplash/Themes
%_kde_appsdir/ksplash/Themes/qmldefault
%_kde_appsdir/startactive
# TODO: review systemd services
%dir %{_libdir}/systemd
%dir %{_libdir}/systemd/user
%{_libdir}/systemd/user/*
