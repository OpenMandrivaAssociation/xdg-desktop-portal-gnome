Name:		xdg-desktop-portal-gnome
Version:	46.2
Release:	2
Summary:	A backend implementation for xdg-desktop-portal
License:	LGPL-2.1-or-later
Group:		Graphical desktop/GNOME
URL:		https://gitlab.gnome.org/GNOME/xdg-desktop-portal-gnome
Source0:	https://download.gnome.org/sources/xdg-desktop-portal-gnome/%{url_ver}/%{name}-%{version}.tar.xz
# Fix slow startup when using other DEs in multi-DE installation (mga#31855)
Patch0: 	add-onlyin-key-to-portal-descriptor.patch

BuildRequires:  gettext
BuildRequires:	meson
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.44
BuildRequires:	pkgconfig(gnome-bg-4)
BuildRequires:	pkgconfig(gnome-desktop-4)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk4) >= 4.0
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(xdg-desktop-portal)
Requires: dbus-common
Requires:	xdg-desktop-portal
# Not yet (angry)
#Supplements:	gnome-shell
Provides: xdg-desktop-portal-implementation

%description
A backend implementation for xdg-desktop-portal for the GNOME
desktop environment.

%prep
%autosetup -p1

%build
%meson -Dsystemduserunitdir=%{_userunitdir}
%meson_build

%install
%meson_install

%find_lang %{name}

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files -f %{name}.lang
%license COPYING
%doc NEWS README.md
%{_userunitdir}/xdg-desktop-portal-gnome.service
%{_libexecdir}/xdg-desktop-portal-gnome
%{_datadir}/applications/xdg-desktop-portal-gnome.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.gnome.service
%{_datadir}/glib-2.0/schemas/xdg-desktop-portal-gnome.gschema.xml
%{_datadir}/xdg-desktop-portal/portals/gnome.portal
