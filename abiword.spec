# BUILD OPTIONS: 1 for yes, 0 for no
%define enable_debug 0
%define enable_optimize 1
%define enable_perl 1
%define enable_jpeg 1

# PLUGIN OPTIONS: 1 for yes, 0 for no
%define enable_abicollab 1
%define enable_abicommand 1
%define enable_abidash 1
%define enable_abipsion 1
%define enable_aiksaurus 1
%define enable_babelfish 1
%define enable_eg 1
%define enable_freetranslation 1
%define enable_festvox 0
%define enable_gda 0
%define enable_gdict 1
%define enable_goffice 1
%define enable_shell 1
%define enable_urldict 1
%define enable_wikipedia 1
# import/export
%define enable_pdf 1
%define enable_wordperfect 1
# graphics  
%define enable_rsvg 1
#search
%define enable_eps 0
%define enable_google 1

%if %{enable_debug}
# This makes sure the binaries are UNSTRIPPED!
%define __os_install_post       %{nil}
# This gives extra debuggin and huge binaries
%{expand:%%define optflags %{optflags} %([ ! $DEBUG ] && echo '-g3')}
%endif

%if %{enable_abicollab}
%define plugin_abicollab --enable-abicollab
%else
%define plugin_abicollab --disable-abicollab
%endif

%if %{enable_aiksaurus}
%define plugin_aiksaurus --enable-aiksaurus
%else
%define plugin_aiksaurus --disable-aiksaurus
%endif

%if %{enable_gdict}
%define plugin_gdict --enable-gdict
%else
%define plugin_gdict --disable-gdict
%endif

%if %{enable_babelfish}
%define plugin_babelfish --enable-babelfish
%else
%define plugin_babelfish --disable-babelfish
%endif

%if %{enable_urldict}
%define plugin_urldict --enable-urldict
%else
%define plugin_urldict --disable-urldict
%endif

%if %{enable_wikipedia}
%define plugin_wikipedia --enable-wikipedia
%else
%define plugin_wikipedia --disable-wikipedia
%endif

%if %{enable_freetranslation}
%define plugin_freetranslation --enable-freetranslation
%else
%define plugin_freetranslation --disable-freetranslation
%endif 

%if %{enable_festvox}
%define plugin_festvox --enable-festvox
%else
%define plugin_festvox --disable-festvox
%endif

%if %{enable_shell}
%define plugin_shell --enable-shell
%else
%define plugin_shell --disable-shell
%endif

%if %{enable_eg}
%define plugin_tests --enable-eg
%else
%define plugin_tests --disable-eg
%endif

%if %{enable_google}
%define plugin_google --enable-google
%else
%define plugin_google --disable-google
%endif

%if %{enable_abidash}
%define plugin_abidash --enable-abidash
%else
%define plugin_abidash --disable-abidash
%endif

%if %{enable_abipsion}
%define plugin_abipsion --enable-abipsion
%else
%define plugin_abipsion --disable-abipsion
%endif

%if %{enable_gda}
%define plugin_gda --enable-gda
%else
%define plugin_gda --disable-gda
%endif

%if %{enable_pdf}
%define plugin_pdf --enable-pdf
%else
%define plugin_pdf --disable-pdf
%endif

%define version_flag ABI_BUILD_VERSION=%version
%define Aname %{name}-2.5
%define Sname AbiSuite-2.5
%define iconname abiword.png  
%define release 3

Name:       abiword
Summary:    Lean and fast full-featured word processor
Version:    2.5.1
Release:    %mkrel %release
Group:      Office
URL:        http://www.abisource.com/
License:    GPL
Source0:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.bz2
Source1:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-plugins-%{version}.tar.bz2
Source2:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-extras-%{version}.tar.bz2
Source3:    http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-docs-%{version}.tar.bz2
Patch0:     %name-plugins-2.5.1-poppler.patch
Patch1:     abiword-2.4.5-xap_UnixApp.patch
# Patch2,3 from upstream bug report #10977
Patch2:     %{name}-2.5.1-fix-goffice-0.4.0-build.patch
Patch3:     %{name}-plugins-2.5.1-fix-goffice-0.4.0-build.patch
BuildRoot:  %_tmppath/%name-%version-buildroot
BuildRequires:  ImageMagick
BuildRequires:  bzip2-devel
BuildRequires:  libtool-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libwmf-devel >= 0.2.1
BuildRequires:  wv-devel
BuildRequires:  enchant-devel
BuildRequires:  texinfo
BuildRequires:  lcms-devel
BuildRequires:  fribidi-devel >= 0.10.4
BuildRequires:  libglade2.0-devel
BuildRequires:  libgnomeui2-devel
BuildRequires:  libgnomeprintui-devel
BuildRequires:  libgsf-devel >= 1.13.3
BuildRequires:  link-grammar-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libhowl-devel
BuildRequires:  ots-devel >= 0.5.0
BuildRequires:  gtkmathview >= 0.7.5
BuildRequires:  libgtkmathview-devel >= 0.7.5
BuildRequires:	gucharmap-devel
%if %{enable_eps} 
BuildRequires:  libeps0-devel
%endif
%if %{enable_abicommand}
BuildRequires:  libtermcap-devel 
BuildRequires:  libreadline-devel
%endif
%if %{enable_perl}
BuildRequires:  perl >= 5.005
%endif
%if %{enable_gdict}
BuildRequires:  gdict
%endif
%if %{enable_aiksaurus}
BuildRequires:  aiksaurusgtk-devel
%endif
%if %{enable_gda}
BuildRequires:  gnome-db2.0-devel
%endif
%if %{enable_goffice}
BuildRequires: goffice-devel >= 0.4.0
%endif
%if %{enable_rsvg}
BuildRequires:  librsvg-devel
%endif 
%if %{enable_pdf}
BuildRequires:  libpoppler-devel
%endif
%if %{enable_wordperfect}
BuildRequires:  libwpd-devel >= 0.8.0
%endif 
%if %{enable_abipsion}
BuildRequires:  libpsiconv-devel
%endif
Obsoletes:  %{name}-plugin-gdkpixbuf
Provides:  %{name}-plugin-gdkpixbuf
 

%description
AbiWord is a cross-platform, Open Source Word Processor developed
by the people at AbiSource, Inc. and by developers from around the world.

It is a lean and fast full-featured word processor. It works on Most Unix
systems, Microsoft Windows and Mac OS X. Features include:

   * Basic character formatting (bold, underline, italics, etc.)
   * Paragraph alignment
   * Spell-check
   * Import of MS Word and RTF documents
   * Export to RTF, Text, HTML, and LaTeX formats
   * Interactive rulers and tabs
   * Styles
   * Unlimited undo/redo
   * Multiple column control
   * Widow/orphan control
   * Find/Replace
   * Images
   * Tables

More features are available through the use of plugins, which are
packaged separately. Also more import and export filters are
available by installing the abiword-plugin-impexp package.
Help files are available in a few languages which rae available as
for example abiword-doc-de.

Abiword with the GNOME front-end is part of the GNOME Office Suite. 
See http://www.gnomeoffice.org for details.

%package devel
Summary:	Devel files for Abiword
Group:	Development/Other
Requires:	%{name} = %{version}

%description devel
This pacakage contains devel files for Abiword, mainly header files
and pkg files.

%package doc-de
Summary:    German documentation and helpfiles for Abiword
Group:      Office
Requires:   %{name}

%description doc-de
German documentation and helpfiles for Abiword.

%package doc-en
Summary:    English documentation and helpfiles for Abiword
Group:      Office
Requires:   %{name}

%description doc-en
English documentation and helpfiles for Abiword.

%package doc-fr
Summary:    French documentation and helpfiles for Abiword
Group:      Office
Requires:   %{name}

%description doc-fr
French documentation and helpfiles for Abiword.

%package doc-pl
Summary:    Polish documentation and helpfiles for Abiword
Group:      Office
Requires:   %{name}

%description doc-pl
Polish documentation and helpfiles for Abiword.

%if %{enable_abicollab}
%package plugin-abicollab
Summary:    A real-time collaborative editing feature to AbiWord
Group:      Office
Requires:   %{name} = %{version}

%description plugin-abicollab
This plugin offers a real-time collaborative editing feature to AbiWord.
%endif

%if %{enable_abicommand}
%package plugin-abicommand
Summary:    This plugin offers a command line interface to AbiWord
Group:      Office
Requires:   %{name} = %{version}

%description plugin-abicommand
This plugin offers a command line interface to AbiWord.
%endif

%if %{enable_perl}
%package perl
Summary:    Perl Bindings Module
Group:      Development/Libraries
Requires:   perl >= 5.005
Requires:   %{name} = %{version}

%description perl
Perl Module containing classes for AbiWord Scripting.
%endif

%if %{enable_babelfish}
%package plugin-babelfish
Summary:    Plugin to allow abiword to show babelfish translations
Group:      Office
Requires:   %{name} = %{version}
 
%description plugin-babelfish
Installing this plugin will allow abiword fetch babelfish translations 
for selected text.
%endif

%if %{enable_urldict}
%package plugin-urldict
Summary:    Plugin to allow abiword to use dict through a web browser
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-urldict
Installing this plugin will allow abiword to use dict through a web 
browser on selected text.
%endif 

%if %{enable_festvox}
%package plugin-festvox
Summary:    Plugin for festvox
Group:      Office
Requires:   %{name} = %{version}

%description plugin-festvox
Plugin for festvox
%endif

%if %{enable_gdict}
%package plugin-gdict
Summary:    Plugin to allow abiword to use gdict
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-gdict
Plugin to allow abiword to use gdict
%endif

%package plugin-abigimp
Summary:    Enables editing of your images in The GIMP
Group:      Office
Requires:   %{name} = %{version}

%description plugin-abigimp
Installing this plugin will allow AbiWord to transfer images to The GIMP for
editing.

%if %{enable_shell}
%package plugin-shell
Summary:    Enables redirection of shell output into AbiWord
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-shell
Installing this plugin will allow AbiWord to read output of shell commands.
%endif

%if %{enable_wikipedia}
%package plugin-wikipedia
Summary:    Plugin to allow abiword to connect with WikiPedia
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-wikipedia
Plugin to allow abiword to connect with WikiPedia.
%endif

%if %{enable_freetranslation}
%package plugin-freetranslation
Summary:    Plugin to allow abiword to connect with freetranslation
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-freetranslation
Plugin to allow abiword to connect with freetranslation.
%endif

%if %{enable_aiksaurus}
%package plugin-aiksaurus
Summary:    Plugin to allow abiword to connect with AikSaurus
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-aiksaurus
Plugin to allow abiword to connect with AikSaurus, a thesaurus
library (currently English only).
%endif

%package plugin-ots
Summary:    Plugin to summarize text
Group:      Office
Requires:   ots >= 0.5.0
Requires:   %{name} = %{version}

%description plugin-ots
Installing this plugin will allow abiword to summarize text with
the help from ots (open text summarizer).

%if %{enable_gda}
%package plugin-gda
Summary:    Plugin to import from databases
Group:      Office
Requires:   gda2.0
Requires:   gnome-db2.0
Requires:   %{name} = %{version}

%description plugin-gda
Installing this plugin will allow abiword to import from databases through
gda and gnome-db. 
%endif

%package plugin-graphics
Summary:    Plugins to allow abiword to import images
Group:      Office
Requires:   %{name} = %{version}

%description plugin-graphics
Installing these plugins will allow abiword to import several image types,
like jpeg, bmp or rsvg.

%package plugin-impexp
Summary:    Plugins to allow abiword to import file types from other wordprocessors
Group:      Office
Requires:   %{name} = %{version}

%description plugin-impexp
Installing these plugins will allow abiword to import and/or export file
types from other wordprocessors, like OpenOffice/StarOffice(5/6), WordPerfect,
Kword, etc.
This package also provides plugins to import LaTeX, PDF, nroff and docbook
documents, as well as the import and export of html/xhtml documents.
Support to import MS Word documents is built into the main package.

%if %{enable_google}
%package plugin-google
Summary:    Plugins allows Google search for selected text
Group:      Office
Requires:   %{name} = %{version} 

%description plugin-google
Plugins allows Google search for selected text
%endif

%if %{enable_abidash}
%package plugin-abidash
Summary:    Plugin template for a notification style plugin
Group:      Office
Requires:   %{name} = %{version}  

%description plugin-abidash
New plugin template for a notification style plugin. 
Can be used to make a dashbaord plugin
%endif

%if %{enable_abipsion}
%package plugin-abipsion
Summary:    Plugin allowing import/export from Psion PDA
Group:      Office
Requires:	%{name} = %{version}

%description plugin-abipsion
Plugin allowing import/export from Psion PDA
%endif

%if %{enable_goffice}
%package plugin-abigoffice
Summary:    Plugin to create Gnome Office components
Group:      Office
Requires:   %{name} = %{version}
Requires:   goffice >= 0.4.0
Provides:	%{name}-abigochar = %{version}-%{release}
Obsoletes:	%{name}-abigochar

%description plugin-abigoffice
Plugin allowing the creation of Gnome Office components
%endif

%package plugin-abigrammar
Summary:    Plugin to allow grammar checking
Group:      Office
Requires:   link-grammar
Requires:   %{name} = %{version}

%description plugin-abigrammar
Plugin to allow grammar checking of English documents using
link-grammar as a syntactic parser of English.

%package plugin-abimathview
Summary:    Plugin to import and edit MathML documents
Group:      Office
Requires:   gtkmathview >= 0.7.5
Requires:   %{name} = %{version}

%description plugin-abimathview
Plugin to import and edit MathML documents

%package plugin-olpctoolbar
Summary:    Floating toolbar for using on the OLPC system
Group:      Office
Requires:   %{name} = %{version}

%description plugin-olpctoolbar
Floating toolbar for using on the OLPC system

%prep
%setup -q -n %{name}-%{version}
%setup -D -T -q -a 1
%setup -D -T -q -a 2
%setup -D -T -q -a 3

%patch2 -p0 -b .goffice

cd %{name}-plugins-%{version}
%patch0 -p0 -b .poppler
%patch3 -p0 -b .goffice
cd -
 
%build
rm -Rf libpng

# The main applications
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --enable-gnome --with-sys-wv 

%make %{version_flag} ABI_OPT_DEBUG=%{enable_debug} \
    UNIX_CAN_BUILD_STATIC=0 ABI_OPT_LIBJPEG=1 \
    ABI_OPT_PERL=%{enable_perl} \
    ABI_OPT_OPTIMIZE=%{enable_optimize}

# The plugins
cd %{name}-plugins-%{version}
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --host=%{_target_platform} --target=%{_target} --disable-rpath \
    --enable-all --with-abiword=../ %{plugin_abicollab} \
    %{plugin_abidash} %{plugin_abipsion} %{plugin_aiksaurus} \
    %{plugin_babelfish} %{plugin_festvox} %{plugin_freetranslation} \
    %{plugin_gda} %{plugin_gdict} %{plugin_google} \
    %{plugin_shell} %{plugin_tests} \
    %{plugin_urldict} %{plugin_wikipedia} \
    %{plugin_pdf}

%make
cd -

# The extra stuff don't need build acturally
# cd ../%{name}-extras-%{version}

# now make the docs
cd %{name}-docs-%{version}
ABI_DOC_PROG=$(pwd)/../src/wp/main/unix/%{name} ./make-html.sh
cd -

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
#cd abi

%makeinstall_std

cd %{name}-plugins-%{version}
%make install DESTDIR=$RPM_BUILD_ROOT
cd -

# install extra stuff
cd %{name}-extras-%{version}
# cliparts
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-2.5/clipart
install -m 644 clipart/*.png $RPM_BUILD_ROOT/%{_datadir}/%{name}-2.5/clipart
# templates
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-2.5/templates
install -m 644 templates/*.awt $RPM_BUILD_ROOT/%{_datadir}/%{name}-2.5/templates
# dictionaries
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}-2.5/dictionary
install -m 644 dictionary/*.xml $RPM_BUILD_ROOT/%{_datadir}/%{name}-2.5/dictionary
cd -

# install the docs
cd %{name}-docs-%{version}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{Aname}/help
cp -rp help/* $RPM_BUILD_ROOT/%{_datadir}/%{Aname}/help/
# some of the help dirs have bad perms (#109261)
find $RPM_BUILD_ROOT/%{_datadir}/%{Aname}/help/ -type d -exec chmod -c o+rx {} \;
cd -

desktop-file-install --vendor="" \
--remove-category="Application" \
--remove-category="X-Red-Hat-Base" \
--add-category="X-MandrivaLinux-Office-Wordprocessors" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
 
#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_datadir}/%{Aname}/Nautilus_View_AbiWord.oaf \
 $RPM_BUILD_ROOT%{_datadir}/%{Aname}/nautilus-abiword-content-view-ui.xml \
 $RPM_BUILD_ROOT%{_datadir}/%{Aname}/system.profile \
 $RPM_BUILD_ROOT%{_datadir}/%{Aname}/AbiWord.exe.MANIFEST \
 $RPM_BUILD_ROOT%{_bindir}/ttftool \
 $RPM_BUILD_ROOT%{_bindir}/ttfadmin.sh
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{Aname}/plugins/*.la

# add uninstalled files
%if %{enable_abicommand}
#cd ../abidistfiles
#cp GNOME_AbiWord_Control_2_4.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/
%else
rm -f $RPM_BUILD_ROOT%{_libdir}/%{Aname}/plugins/libAbiCommand.*
%endif

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc user/wp/readme.txt BiDiReadme.txt COPYING COPYRIGHT.TXT CREDITS.TXT abi2po.pl
%{_bindir}/*
%{_datadir}/%{Aname}/readme.txt 
%{_datadir}/%{Aname}/strings
%{_datadir}/%{Aname}/scripts
%{_datadir}/%{Aname}/system.profile-* 
%{_datadir}/%{Aname}/glade/*
%{_datadir}/%{Aname}/clipart/*
%{_datadir}/%{Aname}/templates/*
%{_datadir}/%{Aname}/dictionary/*
%{_datadir}/mime-info/%{name}.keys
%_datadir/icons/abiword_48.png
%_datadir/applications/abiword.desktop

%files doc-de
%defattr(-,root,root)
#%doc %{name}-docs-%{version}/ABW/de-DE

%files doc-en
%defattr(-,root,root)
#%doc %{name}-docs-%{version}/screenshots/GNOME/en-GB %{name}-docs-%{version}/Tutorials %{name}-docs-%{version}/Manual/en
%doc %{name}-docs-%{version}/ABW/en-US
%doc docs/*.abw docs/*.txt docs/status/*.xsl docs/status/*.xml
%_datadir/%{Aname}/help/en-US

%files doc-fr
%defattr(-,root,root)
%doc %{name}-docs-%{version}/ABW/fr-FR
%_datadir/%{Aname}/help/fr-FR

%files doc-pl
%defattr(-,root,root)
%doc %{name}-docs-%{version}/ABW/pl-PL
%_datadir/%{Aname}/help/pl-PL

%if %{enable_abicollab}
%files plugin-abicollab
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiCollab.*
%endif

%if %{enable_abicommand}
%files plugin-abicommand
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiCommand.*
#%attr(-,root,root) %{_libdir}/bonobo/servers/GNOME_AbiWord_Control_2_4.server
%endif

%if %{enable_gdict}
%files plugin-gdict
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiGdict.*
%endif

%if %{enable_babelfish}
%files plugin-babelfish
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiBabelfish.*
%endif

%if %{enable_urldict}
%files plugin-urldict
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiURLDict.*
%endif

%if %{enable_wikipedia}
%files plugin-wikipedia
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiWikipedia.*
%endif

%if %{enable_freetranslation}
%files plugin-freetranslation
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiFreeTranslation.*
%endif

%if %{enable_aiksaurus}
%files plugin-aiksaurus
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiAikSaurus.*
%endif

%if %{enable_festvox}
%files plugin-festvox
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiFestVox.*
%endif 
 
%files plugin-abigimp
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiGimp.*

%if %{enable_shell}
%files plugin-shell
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiScriptHappy.*
%endif

%files plugin-ots
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiOTS.*
%attr(-,root,root) %_libdir/%{Aname}/plugins/AbiWord/glade/ots.glade

%if %{enable_gda}
%files plugin-gda
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiGDA.* 
%endif

%files plugin-graphics
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiJPEG.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiBMP.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiWMF.*
%if %{enable_rsvg}
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiRSVG.*
%endif

%files plugin-impexp
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiKWord.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiXSLFO.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiLaTeX.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiDocBook.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiMSWrite.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiPalmDoc.*
%if %{enable_pdf}
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiPDF.*
%endif
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiSDW.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiWML.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiXHTML.*
#%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiBZ2.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiOpenDocument.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiOpenWriter.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiCAPI.*
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiPassepartout.*
%if %{enable_wordperfect}
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiWordPerfect.*
%endif
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiApplix.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiClarisWorks.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiEML.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiHRText.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiHancom.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiISCII.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiOPML.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiMIF.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiNroff.so
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiT602.so

%if %{enable_google}
%files plugin-google
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiGoogle.*
%endif

%if %{enable_abidash}
%files plugin-abidash
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiDash.*
%endif

%if %{enable_abipsion}
%files plugin-abipsion
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiPsion.*
%endif

%if %{enable_goffice}
%files plugin-abigoffice
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiGOffice.*
%endif

%files plugin-abigrammar
%attr(-,root,root) %_libdir/%{Aname}/plugins/libAbiGrammar.*

%files plugin-abimathview
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiMathView.so

%files plugin-olpctoolbar
%attr(-,root,root) %{_libdir}/%{Aname}/plugins/libAbiOlpcToolbar.*

%files devel
%attr(-,root,root)
%{_includedir}/%{Aname}/*.h
%{_libdir}/pkgconfig/%{Aname}.pc

%post
%{update_menus}
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_mime_database}

