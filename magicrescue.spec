%define name    magicrescue
%define version 1.1.4
%define release 2mdk
%define Summary Magic Rescue tries to recover files

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL 
Group:          Archiving/Other
URL:            http://jbj.rapanden.dk/magicrescue/
Source0:        %name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot
Conflicts:	safecat
Requires:	mpg123 mencoder gzip binutils

%description
Magic Rescue scans a block device for file types it knows how to recover and
calls an external program to extract them.  It looks at "magic bytes" in file
contents, so it can be used both as an undelete utility and for recovering a
corrupted drive or partition.  As long as the file data is there, it will find
it. It works on any file system.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}
%makeinstall PREFIX=$RPM_BUILD_ROOT/%{_prefix}
# move man pages to the right directory
mv ${RPM_BUILD_ROOT}%{_prefix}/man ${RPM_BUILD_ROOT}%{_datadir}
# move binaries from /usr/share
mv ${RPM_BUILD_ROOT}%{_datadir}/magicrescue/tools/inputseek ${RPM_BUILD_ROOT}%{_bindir}
mv ${RPM_BUILD_ROOT}%{_datadir}/magicrescue/tools/safecat ${RPM_BUILD_ROOT}%{_bindir}
mv ${RPM_BUILD_ROOT}%{_datadir}/magicrescue/tools/textextract ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%{_bindir}/*
%{_datadir}/magicrescue/tools/*
%defattr(0644,root,root,0755)
%{_datadir}/magicrescue/recipes/*
%doc COPYING README
%{_mandir}/man1/*

