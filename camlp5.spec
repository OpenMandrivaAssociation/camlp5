Name:		camlp5
Version:	8.05.02
Release:	1
Summary:	A preprocessor-pretty-printer of OCaml
License:	BSD
Group:		Development/Other
URL:		https://camlp5.github.io/
Source0:	https://github.com/camlp5/camlp5/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	camlp5-META
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
Camlp5 is a preprocessor-pretty-printer for OCaml.
It is the continuation of the classical Camlp4 with new features.
This version supports OCaml 4.08 through 5.5.

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
%doc CHANGES* DEVEL ICHANGES INSTALL LICENSE README* UPGRADING doc/html
%{_libdir}/ocaml/camlp5
%{_bindir}/*
%{_mandir}/man1/*
