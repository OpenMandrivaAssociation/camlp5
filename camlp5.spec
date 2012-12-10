Name:		camlp5
Version:	6.05
Release:	1
Summary:	A preprocessor-pretty-printer of ocaml
License:	BSD
Group:		Development/Other
URL:		http://pauillac.inria.fr/~ddr/camlp5
Source1:	camlp5-META
Source: 	http://pauillac.inria.fr/~ddr/camlp5/distrib/src/%{name}-%{version}.tgz
BuildRequires:	ocaml

%description
Camlp5 is a preprocessor-pretty-printer of ocaml.
It is the continuation of the classical Camlp4 with new features.
It is compatible with OCaml versions from 3.08.1 to 3.11 included.

%prep
%setup -q

%build
./configure -libdir %{_libdir}/ocaml
%__make world.opt

%install
%__make install \
    LIBDIR=%{buildroot}%{_libdir}/ocaml \
    MANDIR=%{buildroot}%{_mandir} \
    BINDIR=%{buildroot}%{_bindir}
%__install -m 644 %{SOURCE1} %{buildroot}%{_libdir}/ocaml/camlp5/META

%files
%doc CHANGES DEVEL ICHANGES INSTALL LICENSE README UPGRADING doc/html
%{_libdir}/ocaml/camlp5
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Mon Mar 26 2012 Andrey Bondrov <abondrov@mandriva.org> 6.05-1
+ Revision: 786980
- New version 6.05

* Wed Feb 08 2012 Andrey Bondrov <abondrov@mandriva.org> 6.03-1
+ Revision: 771856
- New version 6.03, fix license (GPL -> BSD), drop RPM4 junk

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.02.3-1
+ Revision: 690440
- update to new version 6.02.3

* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 6.02.1-1
+ Revision: 645052
- update to new version 6.02.1

* Mon Dec 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 6.02.0-1mdv2011.0
+ Revision: 623295
- downgrade version, as 6.02.1 breaks coq 8.3 build

* Mon Dec 20 2010 Guillaume Rousse <guillomovitch@mandriva.org> 6.02.1-1mdv2011.0
+ Revision: 623279
- update to new version 6.02.1

* Thu Oct 07 2010 Funda Wang <fwang@mandriva.org> 5.15-1mdv2011.0
+ Revision: 583992
- update to new version 5.15
- rebuild

* Thu Jul 15 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.14-1mdv2011.0
+ Revision: 553838
- new version

* Mon Apr 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.13-1mdv2010.1
+ Revision: 533671
- new version, drop useless patch0

* Sat Feb 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.12-3mdv2010.1
+ Revision: 501368
- rebuild for latest ocaml, using debian patches

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.12-2mdv2010.0
+ Revision: 389810
- rebuild

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.12-1mdv2010.0
+ Revision: 379212
- update to new version 5.12

* Mon Dec 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.11-1mdv2009.1
+ Revision: 317603
- new version

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.10-1mdv2009.1
+ Revision: 295545
- update to new version 5.10

* Sat Sep 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.09-2mdv2009.0
+ Revision: 281829
- put back libs directly at the root of ocaml tree, as in Debian, to make camlp5 a transparent replacement of camlp4 (bug #41942)

* Sat Aug 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.09-1mdv2009.0
+ Revision: 272810
- update to new version 5.09

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 5.08-4mdv2009.0
+ Revision: 243428
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.08-2mdv2008.1
+ Revision: 178359
- rebuild

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.08-1mdv2008.1
+ Revision: 175064
- update to new version 5.08

* Sun Jan 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.07-1mdv2008.1
+ Revision: 158626
- update to new version 5.07

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.06-1mdv2008.1
+ Revision: 138818
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.08-2mdv2008.0
+ Revision: 93177
- configure build for using files where they are installed

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.08-1mdv2008.0
+ Revision: 78389
- import camlp5


