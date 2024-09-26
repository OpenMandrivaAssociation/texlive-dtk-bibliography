Name:		texlive-dtk-bibliography
Version:	72281
Release:	1
Summary:	Bibliography of "Die TeXnische Komodie"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dtk-bibliography
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk-bibliography.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtk-bibliography.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains the bibliography for "Die TeXnische
Komodie", the journal of the German-speaking TeX User Group. It
is updated on a quarterly basis.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/dtk-bibliography
%{_texmfdistdir}/bibtex/bib/dtk-bibliography
%doc %{_texmfdistdir}/doc/bibtex/dtk-bibliography

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
