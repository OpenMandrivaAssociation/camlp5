Name:		camlp5
Version:	8.05.02
Release:	2
Summary:	A preprocessor-pretty-printer of OCaml
License:	BSD
Group:		Development/Other
URL:		https://camlp5.github.io/
Source0:	https://github.com/camlp5/camlp5/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	camlp5-META
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
# Stream/Genlex removed from OCaml 5 stdlib
BuildRequires:	camlp-streams-devel
# Optional deps (rresult/bos/re/pcre2) are only needed for the testsuite

%description
Camlp5 is a preprocessor-pretty-printer for OCaml.
It is the continuation of the classical Camlp4 with new features.
This version supports OCaml 4.08 through 5.5.

%prep
%autosetup -p1
# Upstream hardcodes testsuite packages into every ocamlfind -package line.
# Only camlp-streams is required to build/install (Stream/Genlex for OCaml 5+).
sed -i 's/C5PACKAGES="compiler-libs,compiler-libs.common,camlp-streams,rresult,bos,re,pcre2"/C5PACKAGES="compiler-libs,compiler-libs.common,camlp-streams"/' configure
sed -i 's/C5PACKAGES="compiler-libs,compiler-libs.common,rresult,bos,re,pcre2"/C5PACKAGES="compiler-libs,compiler-libs.common"/' configure

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
