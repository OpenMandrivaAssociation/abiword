%define Werror_cflags %nil
%define api %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1
#define _disable_lto 1

Summary:	Lean and fast full-featured word processor
Name:		abiword
Version:	3.0.6
Release:	3
License:	GPLv2+
Group:		Office
Url:		https://www.abisource.com/
#Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
Source0:	https://gitlab.gnome.org/World/AbiWord/-/archive/release-%{version}/AbiWord-release-%{version}.tar.bz2
Source100:	abiword.rpmlintrc
Patch3:		abiword-3.0.2-clang.patch

BuildRequires:	asio
BuildRequires:	autoconf
BuildRequires:	automake 
BuildRequires:	libtool 
BuildRequires:	m4
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:  flex
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libwmf)
BuildRequires:	psiconv-devel
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(aiksaurus-1.0)
BuildRequires:	pkgconfig(cairo-pdf)
BuildRequires:	pkgconfig(cairo-ps)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libecal-2.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libgoffice-0.10)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libical)
BuildRequires:  pkgconfig(libidn)
BuildRequires:	pkgconfig(libots-1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libwpd-0.10)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libwps-0.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(link-grammar)
BuildRequires:	pkgconfig(loudmouth-1.0)
BuildRequires:	pkgconfig(mathview-frontend-libxml2)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(rasqal)
BuildRequires:	pkgconfig(redland)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(wv-1.0)
BuildRequires:  t1lib1-devel

Suggests:	abiword-doc

%description
AbiWord is a cross-platform, open source, lean and fast full-featured word
processor. It works on Most Unix systems, Microsoft Windows and Mac OS X.

Abiword with the GNOME front-end is part of the GNOME Office Suite.
See http://www.gnomeoffice.org for details.

%files
%{_bindir}/abiword
%{_datadir}/abiword-%{api}
%dir %{_libdir}/abiword-%{api}
%dir %{_libdir}/abiword-%{api}/plugins
%{_libdir}/abiword-%{api}/plugins/*.so
%{_libdir}/libAiksaurusGtk3--export-dynamic.so
# this isnt a devel lib
%{_libdir}/libabiword-%{api}.so
%{_datadir}/applications/*.desktop
#{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
#{_datadir}/telepathy/clients/AbiCollab.client
%{_datadir}/appdata/abiword.appdata.xml
%{_iconsdir}/hicolor/*/*
%{_mandir}/man1/abiword.1.*

#----------------------------------------------------------------------------

%package devel
Summary:	Devel files for Abiword
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
This pacakage contains devel files for Abiword, mainly header files
and pkg files.

%files devel
%{_includedir}/abiword-%{api}
%{_libdir}/libAiksaurusGtk3.so
%{_libdir}/pkgconfig/abiword-%{api}.pc

#----------------------------------------------------------------------------

%prep
%autosetup -n AbiWord-release-%{version} -p1

%build
#export CC=gcc
#export CXX="g++ -std=gnu++11"
# If linked with LLD - crying about: /lib64/crti.o is incompatible with elf32-i386
# which means that the code has hardcoded -L/usr/lib, i.e. it tries to search in a 32-bit path. 
# This has to be fixed manually (and it's a lot of work), so we change the linker to bfd or gold or mold.
export LDFLAGS="-fuse-ld=bfd"
#autoreconf -fiv
./autogen.sh
enable_dynamic=yes %configure \
	--disable-static \
	--enable-plugins \
	--enable-emacs-keybinding \
	--enable-vi-keybinding \
	--enable-clipart \
	--enable-templates \
	--enable-collab-backend-xmpp \
	--enable-collab-backend-tcp \
	--enable-collab-backend-sugar \
	--enable-collab-backend-service \
	--with-gio \
	--with-goffice

%make_build

%install
%make_install

desktop-file-install --vendor="" \
	--remove-category="X-Red-Hat-Base" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop


