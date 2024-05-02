Name:           lem
Version:        2022.12.10
Release:        %autorelease
Summary:        Lem semantic definition language

License:        LGPL-2.0-only
URL:            https://github.com/rems-project/%{name}
Source0:        https://github.com/rems-project/%{name}/archive/2022-12-10/%{name}-2022-12-10.tar.gz

BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-num-devel
BuildRequires:  ocaml-rpm-macros

%global debug_package %{nil}

%description
Lem is a tool for lightweight executable mathematics, for writing, managing, and publishing large-scale portable semantic definitions, with export to LaTeX, executable code (currently OCaml) and interactive theorem provers (currently Coq, HOL4, and Isabelle/HOL, though the generated Coq is not necessarily idiomatic). It is also intended as an intermediate language for generating definitions from domain-specific tools, and for porting definitions between interactive theorem proving systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n lem-2022-12-10 -p1

%build
make

%install
mkdir -p %{buildroot}%{ocamldir}/lem
make install INSTALLDIR=%{buildroot}%{ocamldir} INSTALL_DIR=%{buildroot}/usr
%ocaml_files

%files -f .ofiles
%license LICENSE
%doc README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
