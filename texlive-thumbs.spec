# revision 33134
# category Package
# catalog-ctan /macros/latex/contrib/thumbs
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license lppl1.3
# catalog-version 1.0n
Name:		texlive-thumbs
Version:	1.0q
Release:	3
Summary:	Create thumb indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thumbs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package puts running, customizable thumb marks in the outer
margin, moving downward as the chapter number (or whatever
shall be marked by the thumb marks) increases. Additionally an
overview page/table of thumb marks can be added automatically,
which gives the names of the thumbed objects, the page where
the object/thumb mark first appears, and the thumb mark itself
at its correct position. The thumb marks are useful for large
documents (such as reference guides, anthologies, etc.), where
a quick and easy way to find (for example) a chapter is needed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thumbs/thumbs.sty
%doc %{_texmfdistdir}/doc/latex/thumbs/README
%doc %{_texmfdistdir}/doc/latex/thumbs/thumbs-example.pdf
%doc %{_texmfdistdir}/doc/latex/thumbs/thumbs-example.tex
%doc %{_texmfdistdir}/doc/latex/thumbs/thumbs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thumbs/thumbs.drv
%doc %{_texmfdistdir}/source/latex/thumbs/thumbs.dtx
%doc %{_texmfdistdir}/source/latex/thumbs/thumbs.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
