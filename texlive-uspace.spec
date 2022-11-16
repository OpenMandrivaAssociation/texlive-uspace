Name:		texlive-uspace
Version:	63123
Release:	1
Summary:	Giving meaning to various Unicode space characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uspace
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uspace.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uspace.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX package that gives meaning to various Unicode space
characters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/uspace
%doc %{_texmfdistdir}/doc/latex/uspace

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
