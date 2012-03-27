%define Werror_cflags %nil
%define api %(echo %{version} | cut -d. -f1,2)

Name:       abiword
Summary:    Lean and fast full-featured word processor
Version:    2.9.2
Release:    1
Group:      Office
URL:        http://www.abisource.com/
License:    GPLv2+
Source0:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
# missing header
Source1:	http://svn.abisource.com/abiword/trunk/plugins/collab/backends/telepathy/unix/TelepathyBuddy.h
Patch0:		abiword-2.9.2-glib.patch
Patch1:		abiword-2.9.2-libpng15.patch
Patch2:		abiword-2.9.2-linkage.patch

BuildRequires:	asio
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-common
BuildRequires:	boost-devel
BuildRequires:	jpeg-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libwmf-devel
BuildRequires:	psiconv-devel
BuildRequires:	readline-devel
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(aiksaurus-1.0)
BuildRequires:	pkgconfig(cairo-pdf)
BuildRequires:	pkgconfig(cairo-ps)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gaiksaurus-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libebook-1.2)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libgoffice-0.10)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libots-1)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libwpd-0.9)
BuildRequires:	pkgconfig(libwpg-0.2)
BuildRequires:	pkgconfig(libwps-0.2)
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

%package devel
Summary:	Devel files for Abiword
Group:		Development/Other
Requires:	%{name} = %{version}

%description devel
This pacakage contains devel files for Abiword, mainly header files
and pkg files.

%prep
%setup -q
# missing header
cp %{SOURCE1} plugins/collab/backends/telepathy/unix/
%apply_patches

sed -i -e 's/goffice_req >= 0.10.0/goffice_req/' \
	-e 's/libgoffice-0.10 >= 0.10.0/libgoffice-0.10/' \
	configure plugin-configure.m4 \
	plugins/goffice/plugin.m4 configure.in
 
%build
enable_dynamic=yes %configure2_5x \
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

find %{buildroot} -name *.la|xargs rm

desktop-file-install --vendor="" \
	--remove-category="X-Red-Hat-Base" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/abiword
%{_datadir}/abiword-%{api}
%dir %{_libdir}/abiword-%{api}
%dir %{_libdir}/abiword-%{api}/plugins
%{_libdir}/abiword-%{api}/plugins/*.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%{_datadir}/telepathy/clients/AbiCollab.client
%{_iconsdir}/*.png
%{_mandir}/man1/abiword.1.*

%files devel
%{_includedir}/abiword-%{api}
%{_libdir}/libabiword-%{api}.so
%{_libdir}/pkgconfig/abiword-%{api}.pc

