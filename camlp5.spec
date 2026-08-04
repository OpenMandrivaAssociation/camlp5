%undefine _debugsource_packages
%define debug_package %{nil}
Name:		camlp5
Version:	8.05.02
Release:	14
Summary:	A preprocessor-pretty-printer of OCaml
License:	BSD
Group:		Development/Other
URL:		https://camlp5.github.io/
Source0:	https://github.com/camlp5/camlp5/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	camlp5-META
Source2:	quotedext-nopcre.ml
Source3:	patch-nopcre.py
Source4:	camlp5.rpmlintrc
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
BuildRequires:	python
BuildRequires:	camlp-streams-devel
BuildRequires:	ocaml-rresult-devel
BuildRequires:	ocaml-bos-devel
BuildRequires:	ocaml-re-devel
BuildRequires:	ocaml-pcre2-devel
BuildRequires:	ocaml-fmt-devel

%description
Camlp5 is a preprocessor-pretty-printer for OCaml.
It is the continuation of the classical Camlp4 with new features.
This version supports OCaml 4.08 through 5.5.

%prep
%autosetup -p1
# Prefer full C5 package set when optional deps are available
# (quotedext uses Pcre2; mkcamlp5 needs bos/rresult/re; top needs fmt)

%build
./configure \
	-libdir %{_libdir}/ocaml
%make_build world.opt

%install
# Makefile joins DESTDIR+LIBDIR/BINDIR/MANDIR; do not put buildroot in the dirs
%make_install \
	DESTDIR=%{buildroot} \
	LIBDIR=%{_libdir}/ocaml \
	MANDIR=%{_mandir} \
	BINDIR=%{_bindir}
# topfind path in upstream is wrong when LIBDIR already ends in /ocaml
install -d %{buildroot}%{_libdir}/ocaml
if [ -f etc/topfind.camlp5 ]; then
	cp -a etc/topfind.camlp5 %{buildroot}%{_libdir}/ocaml/
fi
install -d %{buildroot}%{_libdir}/ocaml/camlp5
install -m 644 %{SOURCE1} %{buildroot}%{_libdir}/ocaml/camlp5/META
find %{buildroot} -name .gitignore -delete

%files
%doc CHANGES* DEVEL ICHANGES LICENSE README* UPGRADING doc/html
%{_libdir}/ocaml/camlp5
%{_libdir}/ocaml/topfind.camlp5
%{_bindir}/*
%{_mandir}/man1/*
