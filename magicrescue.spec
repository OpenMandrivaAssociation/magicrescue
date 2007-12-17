Name:           magicrescue
Version:        1.1.4
Release:        %mkrel 3
Summary:        Tries to recover files
License:        GPL 
Group:          Archiving/Other
URL:            http://jbj.rapanden.dk/magicrescue/
Source0:        %name-%version.tar.bz2
Conflicts:	safecat
Requires:       binutils
Requires:       gzip
Requires:       mencoder
Requires:	mpg123
BuildRequires:  db1-devel

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
%makeinstall PREFIX=$RPM_BUILD_ROOT/%{_prefix}
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
