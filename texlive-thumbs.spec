%global tl_name thumbs
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1d
Release:	%{tl_revision}.1
Summary:	Create thumb indexes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thumbs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package puts running, customizable thumb marks in the outer margin,
moving downward as the chapter number (or whatever shall be marked by
the thumb marks) increases. Additionally an overview page/table of thumb
marks can be added automatically, which gives the names of the thumbed
objects, the page where the object/thumb mark first appears, and the
thumb mark itself at its correct position. The thumb marks are useful
for large documents (such as reference guides, anthologies, etc.), where
a quick and easy way to find (for example) a chapter is needed.

