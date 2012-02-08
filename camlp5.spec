Name:		camlp5
Version:	6.03
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
make world.opt

%install
make install \
    LIBDIR=%{buildroot}%{_libdir}/ocaml \
    MANDIR=%{buildroot}%{_mandir} \
    BINDIR=%{buildroot}%{_bindir}
%__install -m 644 %{SOURCE1} %{buildroot}%{_libdir}/ocaml/camlp5/META

%files
%doc CHANGES DEVEL ICHANGES INSTALL LICENSE README UPGRADING doc/html
%{_libdir}/ocaml/camlp5
%{_bindir}/*
%{_mandir}/man1/*
