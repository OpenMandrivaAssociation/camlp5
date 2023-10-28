Name:		camlp5
Version:	8.02.01
Release:	1
Summary:	A preprocessor-pretty-printer of ocaml
License:	BSD
Group:		Development/Other
URL:		https://camlp5.github.io/
Source0:	https://github.com/camlp5/camlp5/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	camlp5-META
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
Camlp5 is a preprocessor-pretty-printer of ocaml.
It is the continuation of the classical Camlp4 with new features.
It is compatible with OCaml versions from 3.08.1 to 3.11 included.

%prep
%autosetup -p1

%build
./configure \
	-libdir %{_libdir}/ocaml
%make_build world.opt

%install
%make_install \
    LIBDIR=%{buildroot}%{_libdir}/ocaml \
    MANDIR=%{buildroot}%{_mandir} \
    BINDIR=%{buildroot}%{_bindir}
install -m 644 %{SOURCE1} %{buildroot}%{_libdir}/ocaml/camlp5/META

%files
%doc CHANGES DEVEL ICHANGES INSTALL LICENSE README UPGRADING doc/html
%{_libdir}/ocaml/camlp5
%{_bindir}/*
%{_mandir}/man1/*

