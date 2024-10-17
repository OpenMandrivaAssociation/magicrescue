Name:           magicrescue
Version:        1.1.9
Release:        4
Summary:        Tries to recover files
License:        GPLv2+
Group:          Archiving/Other
URL:            https://jbj.rapanden.dk/magicrescue/
Source0:        http://jbj.rapanden.dk/magicrescue/release/%name-%version.tar.gz
Conflicts:	safecat
Requires:       binutils
Requires:       gzip
Requires:       mencoder
Requires:	mpg123
BuildRequires:  gdbm-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Magic Rescue scans a block device for file types it knows how to recover and
calls an external program to extract them.  It looks at "magic bytes" in file
contents, so it can be used both as an undelete utility and for recovering a
corrupted drive or partition.  As long as the file data is there, it will find
it. It works on any file system.

%prep
%setup -q

%build
# XXX: This is not a GNU autoconf script
export CFLAGS="%{optflags}"
./configure --prefix=%{_prefix}
%{make}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
%makeinstall PREFIX=%{buildroot}/%{_prefix}
# move man pages to the right directory
mv %{buildroot}%{_prefix}/man %{buildroot}%{_datadir}
# move binaries from /usr/share
mv %{buildroot}%{_datadir}/magicrescue/tools/inputseek %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/magicrescue/tools/safecat %{buildroot}%{_bindir}
mv %{buildroot}%{_datadir}/magicrescue/tools/textextract %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING README 
%{_datadir}/magicrescue/recipes/*
%{_mandir}/man1/*
%defattr(0755,root,root,0755)
%{_bindir}/*
%{_datadir}/magicrescue/tools/*


%changelog
* Tue Apr 12 2011 Funda Wang <fwang@mandriva.org> 1.1.9-3mdv2011.0
+ Revision: 652962
- build with db 5.1

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.9-2mdv2011.0
+ Revision: 612791
- the mass rebuild of 2010.1 packages

* Tue Apr 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.1.9-1mdv2010.1
+ Revision: 534189
- New version 1.1.9

* Wed Dec 30 2009 Jérôme Brenier <incubusss@mandriva.org> 1.1.8-1mdv2010.1
+ Revision: 484226
- new version 1.1.8

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.6-2mdv2010.0
+ Revision: 439698
- rebuild

* Sat Feb 28 2009 Emmanuel Andry <eandry@mandriva.org> 1.1.6-1mdv2009.1
+ Revision: 346114
- New version 1.1.6

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.1.5-3mdv2009.0
+ Revision: 251670
- rebuild

* Tue Feb 05 2008 Funda Wang <fwang@mandriva.org> 1.1.5-1mdv2008.1
+ Revision: 162532
- New version 1.1.5

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 31 2007 David Walluck <walluck@mandriva.org> 1.1.4-3mdv2008.0
+ Revision: 56777
- rebuild for %%mkrel
- fix BuildRequires


* Thu Sep 29 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdk
- fix #18915

* Thu Mar 24 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.1.4-1mdk
- from Dominik Grafenhofer <dominik@grafenhofer.at> : 
	- First build

