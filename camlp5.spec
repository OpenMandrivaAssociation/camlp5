%define name	camlp5
%define version	4.08
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A preprocessor-pretty-printer of ocaml
Source: 	http://pauillac.inria.fr/~ddr/camlp5/%{name}-%{version}.tgz
URL:		http://pauillac.inria.fr/~ddr/camlp5
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Camlp5 is a preprocessor-pretty-printer of ocaml.
It is the continuation of the classical Camlp4 with new features.
It is compatible with OCaml versions from 3.08.1 to 3.11 included.

%prep
%setup -q

%build
./configure
make world.opt

%install
rm -rf %{buildroot}
make install \
    LIBDIR=%{buildroot}/%{ocaml_sitelib} \
    MANDIR=%{buildroot}%{_mandir} \
    BINDIR=%{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES DEVEL ICHANGES INSTALL LICENSE README UPGRADING doc/html
%{ocaml_sitelib}/camlp5
%{_bindir}/*
%{_mandir}/man1/*
