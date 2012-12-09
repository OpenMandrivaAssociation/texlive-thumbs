# revision 25506
# category Package
# catalog-ctan /macros/latex/contrib/thumbs
# catalog-date 2012-02-24 13:31:20 +0100
# catalog-license lppl1.3
# catalog-version 1.0m
Name:		texlive-thumbs
Version:	1.0m
Release:	2
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


%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0m-2
+ Revision: 783481
- rebuild without scriptlet dependencies

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0m-1
+ Revision: 783096
- Update to latest release.

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0k-1
+ Revision: 759069
- Update to latest upstream release

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0j-2
+ Revision: 756840
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0j-1
+ Revision: 719737
- texlive-thumbs
- texlive-thumbs
- texlive-thumbs

