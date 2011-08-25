Name:       abiword
Summary:    Lean and fast full-featured word processor
Version:    2.8.6
Release:    %mkrel 3
Group:      Office
URL:        http://www.abisource.com/
License:    GPLv2+
Source0:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
Source1:    abiword.desktop
Patch0:     abiword-2.8.0-linkage.patch
Patch1:     abiword-2.8.2-fix-build.patch
Patch2:		abiword-2.8.6-libwpd.patch
Patch3:		abiword-2.6.0-boolean.patch
Patch4:		abiword-2.8.6-gcc46.patch
Patch5:		abiword.desktop.patch
BuildRoot:  %_tmppath/%name-%version-buildroot
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	libglade2-devel
BuildRequires:	goffice-devel >= 0.7.7
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	libgsf-1-devel >= 1.14.9
BuildRequires:	wv-devel >= 1.2.0
BuildRequires:	enchant-devel >= 1.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	gucharmap-devel
BuildRequires:	cairo-devel
BuildRequires:	gtk+2-devel >= 2.12.0
BuildRequires:	librsvg2-devel >= 2.16.0
BuildRequires:	libxslt-devel
BuildRequires:	libwpg-devel >= 0.1.0
BuildRequires:	libwpd-devel >= 0.8.0
BuildRequires:	libwps-devel >= 0.1.0
BuildRequires:	libgsf-devel
BuildRequires:  readline-devel
BuildRequires:	gtkmathview-devel >= 0.7.5
BuildRequires:	libpsiconv-devel
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	loudmouth-devel >= 1.0.1
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	libsoup-2.4-devel
BuildRequires:	libwmf-devel
BuildRequires:	boost-devel >= 1.33.0
BuildRequires:	asio
BuildRequires:	ots-devel
BuildRequires:	link-grammar-devel >= 4.2.1
BuildRequires:	aiksaurusgtk-devel

Obsoletes:	abiword-plugin-abicollab < 2.7.2
Obsoletes:	abiword-plugin-abicommand < 2.7.2
Obsoletes:	abiword-plugin-abigimp < 2.7.2
Obsoletes:	abiword-plugin-abigoffice < 2.7.2
Obsoletes:	abiword-plugin-abigrammar < 2.7.2
Obsoletes:	abiword-plugin-abimathview < 2.7.2
Obsoletes:	abiword-plugin-abipsion < 2.7.2
Obsoletes:	abiword-plugin-aiksaurus < 2.7.2
Obsoletes:	abiword-plugin-babelfish < 2.7.2
Obsoletes:	abiword-plugin-freetranslation < 2.7.2
Obsoletes:	abiword-plugin-google < 2.7.2
Obsoletes:	abiword-plugin-graphics < 2.7.2
Obsoletes:	abiword-plugin-impexp < 2.7.2
Obsoletes:	abiword-plugin-ots < 2.7.2
Obsoletes:	abiword-plugin-shell < 2.7.2
Obsoletes:	abiword-plugin-urldict < 2.7.2
Obsoletes:	abiword-plugin-wikipedia < 2.7.2
Obsoletes:	abiword-plugin-gdict < 2.7.2
Obsoletes:	%{_lib}abiword < 2.7.2

Suggests:	abiword-doc

%description
AbiWord is a cross-platform, open source, lean and fast full-featured word
processor. It works on Most Unix systems, Microsoft Windows and Mac OS X.

Abiword with the GNOME front-end is part of the GNOME Office Suite. 
See http://www.gnomeoffice.org for details.

%package devel
Summary:	Devel files for Abiword
Group:	Development/Other
Requires:	%{name} = %{version}

%description devel
This pacakage contains devel files for Abiword, mainly header files
and pkg files.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p0

# needed by patch0
libtoolize --copy --force
autoreconf -fi
 
%build
%define Werror_cflags %nil
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
rm -fr %buildroot
%makeinstall_std

find %buildroot -name *.la|xargs rm

desktop-file-install --vendor="" \
	--remove-category="X-Red-Hat-Base" \
	--dir %buildroot%{_datadir}/applications \
	%buildroot%{_datadir}/applications/%name.desktop

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%{_bindir}/abiword
%{_datadir}/abiword-2.8
%{_libdir}/libabiword-2.8.so
%dir %{_libdir}/abiword-2.8
%dir %{_libdir}/abiword-2.8/plugins
%{_libdir}/abiword-2.8/plugins/*.so
%{_mandir}/man1/abiword.1.*
%{_datadir}/applications/*.desktop
%{_iconsdir}/*.png

%files devel
%defattr(-,root,root)
%{_includedir}/abiword-2.8
%{_libdir}/pkgconfig/abiword-2.8.pc
