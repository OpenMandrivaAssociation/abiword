%define Werror_cflags %nil
%define api %(echo %{version} | cut -d. -f1,2)

Name:       abiword
Summary:    Lean and fast full-featured word processor
Version:    2.9.4
Release:    1
Group:      Office
URL:        http://www.abisource.com/
License:    GPLv2+
Source0:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
# missing header
Source1:	http://svn.abisource.com/abiword/trunk/plugins/collab/backends/telepathy/unix/TelepathyBuddy.h
Source100:	abiword.rpmlintrc
Patch0:		abiword-2.9.3-rosa-libebook_h.patch

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

%patch0 -p1

sed -i -e 's/goffice_req >= 0.10.0/goffice_req/' \
	-e 's/libgoffice-0.10 >= 0.10.0/libgoffice-0.10/' \
	configure plugin-configure.m4 \
	plugins/goffice/plugin.m4 configure.in
autoreconf -fiv
 
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
# this isnt a devel lib
%{_libdir}/libabiword-%{api}.so
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%{_datadir}/telepathy/clients/AbiCollab.client
%{_iconsdir}/hicolor/*/*
%{_mandir}/man1/abiword.1.*

%files devel
%{_includedir}/abiword-%{api}
%{_libdir}/pkgconfig/abiword-%{api}.pc



%changelog
* Thu May 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.9.2-2
+ Revision: 798103
- rebuild moved nonversion lib to main pkg

* Tue Mar 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.9.2-1
+ Revision: 787792
- new version 2.9.2
- added missing header file
- added patches from mga
- cleaned up spec

  + Sergey Zhemoitel <serg@mandriva.org>
    - fix requires automake
    - fix desktop patch
    - fix russian name and comments in .desktop and .desktop.patch
    - fix russian name and comments in .desktop

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.8.6-3
+ Revision: 677000
- rebuild

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 2.8.6-2
+ Revision: 662318
- br gsf
- another fixes for gcc 4.6 and new wpd
- add fedora patches to build with latest wpd

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 2.8.6-1mdv2011.0
+ Revision: 549913
- New version 2.8.6

* Sun Apr 18 2010 Funda Wang <fwang@mandriva.org> 2.8.4-1mdv2010.1
+ Revision: 536082
- new version 2.8.4

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 2.8.3-1mdv2010.1
+ Revision: 531235
- new version 2.8.3

* Sun Feb 14 2010 Götz Waschk <waschk@mandriva.org> 2.8.2-2mdv2010.1
+ Revision: 505828
- rebuild for new goffice

* Sat Feb 13 2010 Funda Wang <fwang@mandriva.org> 2.8.2-1mdv2010.1
+ Revision: 505515
- fix file list
- rediff build patch
- new version 2.8.2

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 2.8.1-2mdv2010.1
+ Revision: 489678
- add patch to build with latest goffice
- rebuild for libjpeg v8

* Fri Oct 30 2009 Frederic Crozat <fcrozat@mandriva.com> 2.8.1-1mdv2010.0
+ Revision: 460232
- Release 2.8.1

* Wed Oct 28 2009 Funda Wang <fwang@mandriva.org> 2.8.0-2mdv2010.0
+ Revision: 459700
- add back patch1 (required for bug#53971)

* Tue Oct 27 2009 Frederic Crozat <fcrozat@mandriva.com> 2.8.0-1mdv2010.0
+ Revision: 459590
- Release 2.8.0 final
- Remove patch1, no longer needed

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 2.8.0-0.svn28229.1mdv2010.0
+ Revision: 449695
- fix file list
- New snapshot of 2.8.0 (build with latest goffice)
- enable dynamic building

  + Frederik Himpe <fhimpe@mandriva.org>
    - update to new version 2.7.10

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 2.7.8-3mdv2010.0
+ Revision: 419601
- obsoletes old lib package
- suggests newly introduced doc package

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 2.7.8-2mdv2010.0
+ Revision: 419455
- rebuild for new libjpeg7

* Thu Aug 13 2009 Funda Wang <fwang@mandriva.org> 2.7.8-1mdv2010.0
+ Revision: 415875
- fix linkage of libabiword
- new verison 2.7.8
- new version 2.7.7

* Sun Jul 05 2009 Funda Wang <fwang@mandriva.org> 2.7.6-1mdv2010.0
+ Revision: 392573
- rsvg plugin is not needed with gtk ui
- new version 2.7.6
- fix desktop file installation

  + Frederik Himpe <fhimpe@mandriva.org>
    - Obsoletes abiword-plugin-gdict

* Sun Jun 14 2009 Funda Wang <fwang@mandriva.org> 2.7.4-1mdv2010.0
+ Revision: 385881
- no more static libs
- New version 2.7.4

* Sun May 31 2009 Funda Wang <fwang@mandriva.org> 2.7.2-2mdv2010.0
+ Revision: 381683
- fix description and obsoletes

* Sun May 31 2009 Funda Wang <fwang@mandriva.org> 2.7.2-1mdv2010.0
+ Revision: 381665
- New version 2.7.2
- big refactor of subpackages, all the plugins are merged into main
- abiword-doc will become another sourcerpm

* Wed Apr 01 2009 Funda Wang <fwang@mandriva.org> 2.6.8-3mdv2009.1
+ Revision: 363110
- fix requires on goffice

* Tue Mar 31 2009 Funda Wang <fwang@mandriva.org> 2.6.8-2mdv2009.1
+ Revision: 362975
- enable sugar collab

  + Frederik Himpe <fhimpe@mandriva.org>
    - Don't build gdict plug-in anymore, it's based on gtk+ 1

* Thu Mar 12 2009 Funda Wang <fwang@mandriva.org> 2.6.8-1mdv2009.1
+ Revision: 354219
- BR xslt
- New version 2.6.8

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 2.6.6-1mdv2009.1
+ Revision: 330398
- fix for backports
- enalbe libabiword
- fix format string
- New version 2.6.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Nov 25 2008 Funda Wang <fwang@mandriva.org> 2.6.5-1mdv2009.1
+ Revision: 306542
- disable eps as mht is too broken
- BR tasn
- enalbe eps
- there is no nextgen
- new version 2.6.5

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 2.6.4-4mdv2009.1
+ Revision: 301261
- rebuild for new xcb

* Thu Oct 30 2008 Funda Wang <fwang@mandriva.org> 2.6.4-3mdv2009.1
+ Revision: 298714
- fix upstream bug#11789: crashes when selecting "Create and Modify styles..."

* Thu Jul 17 2008 Funda Wang <fwang@mandriva.org> 2.6.4-2mdv2009.0
+ Revision: 236670
- enable abicollab plugin

* Wed Jul 16 2008 Funda Wang <fwang@mandriva.org> 2.6.4-1mdv2009.0
+ Revision: 236518
- New version 2.6.4

* Sun Jul 06 2008 Funda Wang <fwang@mandriva.org> 2.6.3-2mdv2009.0
+ Revision: 232058
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu May 01 2008 Funda Wang <fwang@mandriva.org> 2.6.3-1mdv2009.0
+ Revision: 199829
- disable abidash
- disable abicollab as it does not build now
- New version 2.6.3

  + Frederik Himpe <fhimpe@mandriva.org>
    - Fix Buildrequires

* Sat Apr 12 2008 Funda Wang <fwang@mandriva.org> 2.6.2-1mdv2009.0
+ Revision: 192619
- fix file list
- New version 2.6.2

* Wed Mar 19 2008 Funda Wang <fwang@mandriva.org> 2.6.0-1mdv2008.1
+ Revision: 188820
- New version 2.6.0

* Sun Mar 16 2008 Funda Wang <fwang@mandriva.org> 2.5.2-2.23119.1mdv2008.1
+ Revision: 188119
- disable abicollab as it is unstable
- BR wps
- New svn snapshot

* Sun Jan 20 2008 Funda Wang <fwang@mandriva.org> 2.5.2-2.21999.4mdv2008.1
+ Revision: 155257
- New license policy
- BR asio

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix description

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 2.5.2-2.21999.3mdv2008.0
+ Revision: 94973
- fix upgrade path from 2007.0/2007.1

* Sun Sep 23 2007 Funda Wang <fwang@mandriva.org> 2.5.2-2.21999.2mdv2008.0
+ Revision: 92339
- create symbolic link
- own corresponding dir
- fix file list of wordperfect plugin
- Fix building of collab plugin
- add asio source (to be singledout after 2008.0)
- fix doc building
- fix permission

* Sat Sep 22 2007 Funda Wang <fwang@mandriva.org> 2.5.2-2.21999.1mdv2008.0
+ Revision: 92207
- suggests doc
- fix br of goffice
- Do not configure when autogen
- fix poppler requires
- New svn snapshot (2.6.0 nearly)
- fix doc attrib

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Aug 22 2007 Funda Wang <fwang@mandriva.org> 2.5.2-1mdv2008.0
+ Revision: 68865
- add missing plugins files
- BR poppler-glib
- BR boost
- New version 2.5.2
- remove unused patches
- add impexp desktop file

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.1-4mdv2008.0
+ Revision: 38600
- rebuild for expat

* Sat May 05 2007 Funda Wang <fwang@mandriva.org> 2.5.1-3mdv2008.0
+ Revision: 22641
- add autogen.sh for now (to be removed in 2.5.2)
- use autogen now.
- Build against goffice 0.4.0
- BuildRequires gucharmap

* Fri May 04 2007 Funda Wang <fwang@mandriva.org> 2.5.1-2mdv2008.0
+ Revision: 22295
- disable goffice integration for now.
- bump ots requirement.
- kill patch2, as abiword should require higher version of ots.

* Thu May 03 2007 Funda Wang <fwang@mandriva.org> 2.5.1-1mdv2008.0
+ Revision: 21244
- goffice >= 0.3.8
- add devel package.
- adopt to new installation dir.
- there is no de documentation any more.
- Added patch to build ots.
- Enable goffice integration.
- rediff patch0.
- Source tarball have been splitted
- New upstream version 2.5.1


* Tue Feb 06 2007 Jérôme Soyer <saispo@mandriva.org> 2.4.6-2mdv2007.0
+ Revision: 116604
- Rebuild for latest wv

* Wed Nov 22 2006 Jérôme Soyer <saispo@mandriva.org> 2.4.6-1mdv2007.1
+ Revision: 86075
- New release 2.4.6 / Remove Patch1 not needed
- Import abiword

* Mon Sep 18 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.5-5mdv2007.0
- add P1 (#25788) thanks to reinout@gmail.com

* Sun Sep 17 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.5-4mdv2007.0
- rebuild

* Wed Aug 02 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.5-3mdv2007.0
- add version BR for abigochart
- add BR libhowl-devel

* Tue Jul 11 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.5-2mdv2007.0
- re-enable abigochart
- BR and R

* Mon Jul 10 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.5-1mdv2007.0
- 2.4.5 (bug-fix release)
- re-enable eg plugins
- temp disale abigochart...does not build with goffice-devel-0.3.0
- xdg

* Wed Jun 14 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.4-6mdv2007.0
- fix crappy paste job

* Tue Jun 13 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.4-5mdv2007.0
- adjust BR (fix build on x86_64, hopefully)

* Mon Jun 12 2006 Charles A Edwards <eslrahc@mandriva.org> 2.4.4-4mdv2007.0
- rebuild
- fix BR when gda Not enabled

* Thu May 11 2006 Jerome Soyer <saispo@mandriva.org> 2.4.4-3mdk
- Add P0 to build with pdf extensions

* Thu May 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.4.4-2mdk
- Fix Buildrequires

* Fri Apr 28 2006 Jerome Soyer <saispo@mandriva.org> 2.4.4-1mdk
- Thks G�tz Waschk
- Thks Reinout van Schouwen
- 2.4.4
- disable build with libeps
- disable pdf export
- disable gda support

* Mon Jan 09 2006 Marcel Pol <mpol@mandriva.org> 2.4.2-1mdk
- from Reinout van Schouwen <reinout@cs.vu.nl>
  - 2.4.2
  - update buildrequires
  - drop gda plugin for now

* Fri Nov 04 2005 Marcel Pol <mpol@mandriva.org> 2.4.1-4mdk
- improve description

* Sun Oct 30 2005 Marcel Pol <mpol@mandriva.org> 2.4.1-3mdk
- rebuild for new wv

* Fri Oct 28 2005 Marcel Pol <mpol@mandriva.org> 2.4.1-2mdk
- reupload

* Tue Oct 18 2005 Marcel Pol <mpol@mandriva.org> 2.4.1-1mdk
- 2.4.1

* Fri Oct 07 2005 Marcel Pol <mpol@mandriva.org> 2.4.0-1mdk
- 2.4.0
- requires gtkmathview > 0.7.5

* Fri Sep 23 2005 Marcel Pol <mpol@mandriva.org> 2.3.99-1mdk
- 2.3.99

* Tue Aug 30 2005 Marcel Pol <mpol@mandriva.org> 2.3.5-1mdk
- 2.3.5
- enable gda and gochart plugins again
- add mathview plugin
- drop mdk 9.2 substitute

* Wed Aug 17 2005 Marcel Pol <mpol@mandriva.org> 2.3.4-5mdk
- reupload SRPM
- split more docs
- disable abigochart for now, build fails

* Sun Jul 31 2005 Marcel Pol <mpol@mandriva.org> 2.3.4-4mdk
- enable openwrite and opendocument plugin
- make doc package per language

* Fri Jul 29 2005 Marcel Pol <mpol@mandriva.org> 2.3.4-3mdk
- From Reinout van Schouwen
  - build docs
- add abiword-doc package

* Wed Jul 27 2005 Marcel Pol <mpol@mandriva.org> 2.3.4-2mdk
- add link-grammar plugin
- aiksaurus is only in English currently
- remove unneeded devel files for plugins

* Wed Jul 27 2005 Marcel Pol <mpol@mandriva.org> 2.3.4-1mdk
- From Reinout van Schouwen <reinout@cs.vu.nl>
  - 2.3.4
  - disable GDA plugin for now, because of antique libgnomedb dependency
  - po2abi.pl removed
  - OpenDocument plugin added, but disabled for now
- update long-title in menufile

* Thu Jun 16 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.3.1-2mdk
- rebuild for new wv library

* Mon Jun 13 2005 Marcel Pol <mpol@mandriva.org> 2.3.1-1mdk
- 2.3.1
- disable openwriter, needs libgsf cvs (Reinout van Schouwen)
- disable unfinished widget plugin
- disable grammar and collab plugin for now
- new source url

* Thu May 12 2005 Marcel Pol <mpol@mandriva.org> 2.3.0-1mdk
- 2.3.0
- parallel make
- add %%mkrel
- drop file and buildrequires for libnautilus-devel, obsolete
- ad goffice plugin for charts
- add PDF import plugin

* Sat Apr 30 2005 Marcel Pol <mpol@mandriva.org> 2.2.7-2mdk
- fix description (Reinout van Schouwen)

* Tue Apr 05 2005 Charles A Edwards <eslrahc@mandrake.org> 2.2.7-1mdk
- 2.2.6

* Sun Mar 06 2005 Marcel Pol <mpol@mandrake.org> 2.2.5-1mdk
- 2.2.5
- provides gdkpixbuf plugin

* Mon Feb 21 2005 Charles A Edwards <eslrahc@mandrake.org> 2.2.4-1mdk
- 2.2.4
- rm pixbuf-plugin...viewer now included in main
- rm Magick-plugin...no longer included in source

* Thu Jan 20 2005 Charles A Edwards <eslrahc@mandrake.org> 2.2.3-2mdk
- rebuild for new readline

* Tue Jan 18 2005 Charles A Edwards <eslrahc@mandrake.org> 2.2.3-1mdk
- 2.2.3

* Tue Jan 04 2005 Marcel Pol <mpol@mandrake.org> 2.2.2-2mdk
- rebuild for new gda

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 2.2.2-1mdk
- 2.2.2

* Fri Dec 03 2004 Charles A Edwards <eslrahc@mandrake.org> 2.2.1-1mdk
- 2.2.1
- mv BR libreadline-devel to abicommand pkg
- drop patch

* Sun Nov 28 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.2.0-2mdk
- add BuildRequires: libnautilus-devel libreadline-devel

* Thu Nov 18 2004 Charles A Edwards <eslrahc@mandrake.org> 2.2.0-1mdk
- 2.2.0 Final

* Fri Nov 12 2004 Marcel Pol <mpol@mandrake.org> 2.1.99-1mdk
- 2.1.99
- revamp configuring of plugins

* Mon Nov 08 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.98-1mdk
- 2.1.98

* Fri Nov 05 2004 Marcel Pol <mpol@mandrake.org> 2.1.96-1mdk
- 2.1.96

* Wed Oct 20 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.91-1mdk
- 2.1.91
- enable/add AbiPsion plugin

* Sat Oct 16 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.90-1mdk
- 2.1.90 (2.2 Beta 1)
- add abidash plugin

* Sat Oct 02 2004 Marcel Pol <mpol@mandrake.org> 2.1.8-1mdk
- 2.1.8
- really disable abimagick-plugin
- explicitly disable psion plugin (compile breaks)

* Thu Sep 09 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.7-1mdk
- 2.1.7
- rediff p
- drop p1 and p2
- abimagick-plugin still causes abort-so-disable

* Sun Sep 05 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.6-2mdk
- disable abimagick-plugin (bug 7211-could find no work-a-round)
- drop patch1

* Sat Sep 04 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.6-1mdk
- 2.1.6
- patch abigimp and abimagick

* Fri Sep 03 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.1.5-2mdk
- fix broken desktop file

* Wed Aug 11 2004 Marcel Pol <mpol@mandrake.org> 2.1.5-1mdk
- 2.1.5
- coquille plugin is gone, part of docbook plugin
- enable aiksaurus again
- add uninstalled files

* Fri Jul 30 2004 Marcel Pol <mpol@mandrake.org> 2.1.3-5mdk
- build against system wv (security fix)

* Thu Jul 29 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.3-4mdk
- rebuild for IM-6.0.4.1

* Thu Jul 22 2004 Marcel Pol <mpol@mandrake.org> 2.1.3-3mdk
- enable Palm inport/export plugin

* Wed Jul 07 2004 Michael Scherer <misc@mandrake.org> 2.1.3-2mdk 
- rebuild for new ImageMagick

* Sat Jun 12 2004 Marcel Pol <mpol@mandrake.org> 2.1.3-1mdk
- 2.1.3
- buildrequires imagemagick
- enable gda plugin again, disable aiksaurus for now

* Sun May 23 2004 Charles A Edwards <eslrahc@mandrake.org> 2.1.2-1mdk
- 2.1.2
- reenable libtoolize
- add and enable google plugin
- enable ImageMagick plugin
- rm all Obsoletes/Provides for abiword2 abisuite
- misc spec clean-up

* Wed Apr 14 2004 Marcel Pol <mpol@mandrake.org> 2.0.6-1mdk
- 2.0.6
- temporarily disable gda and coquille plugins

