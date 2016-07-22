%define Werror_cflags %nil
%define api %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Lean and fast full-featured word processor
Name:		abiword
Version:	3.0.1
Release:	3
License:	GPLv2+
Group:		Office
Url:		http://www.abisource.com/
Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
Source100:	abiword.rpmlintrc
Patch1:		abiword-3.0.0-librevenge.patch
Patch2:		abiword-3.0.0-libwp.patch
Patch3:		abiword-3.0.1-libwps-0.4.patch
Patch4:		abiword-3.0.1-gnutls.patch
BuildRequires:	asio
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-common
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libwmf-devel
BuildRequires:	psiconv-devel
BuildRequires:	readline-devel
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(aiksaurus-1.0)
BuildRequires:	pkgconfig(cairo-pdf)
BuildRequires:	pkgconfig(cairo-ps)
BuildRequires:	pkgconfig(champlain-0.12)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gaiksaurus-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libgoffice-0.10)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libots-1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
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
%{_libdir}/libAiksaurusGtk3*.so
# this isnt a devel lib
%{_libdir}/libabiword-%{api}.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%{_datadir}/telepathy/clients/AbiCollab.client
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
%{_libdir}/pkgconfig/abiword-%{api}.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
autoreconf -fiv
enable_dynamic=yes %configure \
	--disable-static \
	--enable-default-plugins \
	--enable-emacs-keybinding \
	--enable-vi-keybinding \
	--enable-clipart \
	--enable-templates \
	--enable-collab-backend-xmpp \
	--enable-collab-backend-tcp \
	--enable-collab-backend-sugar \
	--enable-collab-backend-service \
	--with-gio \
	--with-goffice \
	--with-inter7eps \
	--with-libtidy \
	--enable-plugins="wml goffice freetranslation latex eml gimp mif loadbindings babelfish wpg openxml mswrite wordperfect mathview urldict presentation pdb psion collab google paint hancom xslfo opendocument openwriter t602 iscii wmf ots command sdw gdict opml clarisworks kword pdf grammar passepartout applix aiksaurus wikipedia hrtext s5 docbook"

%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="X-Red-Hat-Base" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop


