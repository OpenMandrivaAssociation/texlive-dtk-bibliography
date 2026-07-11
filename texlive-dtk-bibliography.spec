%global tl_name dtk-bibliography
%global tl_revision 78985

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2026~02
Release:	%{tl_revision}.1
Summary:	Bibliography of Die TeXnische Komodie
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/dtk-bibliography
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk-bibliography.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk-bibliography.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains the bibliography for "Die TeXnische Komodie", the
journal of the German-speaking TeX User Group. It is updated on a
quarterly basis.

