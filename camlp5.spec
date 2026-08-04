Name:		camlp5
Version:	8.05.02
Release:	8
Summary:	A preprocessor-pretty-printer of OCaml
License:	BSD
Group:		Development/Other
URL:		https://camlp5.github.io/
Source0:	https://github.com/camlp5/camlp5/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	camlp5-META
Source2:	quotedext-nopcre.ml
Source3:	patch-nopcre.py
BuildRequires:	make
BuildRequires:	ocaml
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
BuildRequires:	python
BuildRequires:	camlp-streams-devel

%description
Camlp5 is a preprocessor-pretty-printer for OCaml.
It is the continuation of the classical Camlp4 with new features.
This version supports OCaml 4.08 through 5.5.

%prep
%autosetup -p1
# Drop unused testsuite packages from ocamlfind -package lines
sed -i 's/C5PACKAGES="compiler-libs,compiler-libs.common,camlp-streams,rresult,bos,re,pcre2"/C5PACKAGES="compiler-libs,compiler-libs.common,camlp-streams"/' configure
sed -i 's/C5PACKAGES="compiler-libs,compiler-libs.common,rresult,bos,re,pcre2"/C5PACKAGES="compiler-libs,compiler-libs.common"/' configure
# Avoid ocaml-pcre2 (not yet in cooker): reimplement the two call sites without Pcre2
cp -f %{SOURCE2} main/quotedext.ml
cp -f %{SOURCE2} ocaml_src/main/quotedext.ml
python %{SOURCE3}
# mkcamlp5 helper needs bos/rresult/re/pcre2 (not packaged); skip it
sed -i 's/all: $(COUT) META mkcamlp5$(EXE)/all: $(COUT) META/' etc/Makefile
# top/rprint needs fmt (not packaged); skip toplevel integration for now
sed -i 's/DIRS=lib odyl main meta etc top ocpp man/DIRS=lib odyl main meta etc ocpp man/' Makefile
sed -i 's/all: $(COUT) META mkcamlp5$(EXE)/all: $(COUT) META/' scripts/Makefile 2>/dev/null || :

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

%files
%doc CHANGES* DEVEL ICHANGES INSTALL LICENSE README* UPGRADING doc/html
%{_libdir}/ocaml/camlp5
%{_bindir}/*
%{_mandir}/man1/*
