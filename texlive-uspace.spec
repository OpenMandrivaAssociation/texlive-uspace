%global tl_name uspace
%global tl_revision 63123

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.05
Release:	%{tl_revision}.1
Summary:	Giving meaning to various Unicode space characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uspace
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uspace.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uspace.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX package that gives meaning to various Unicode space characters.

