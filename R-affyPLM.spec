%define		packname	affyPLM

Summary:	Methods for fitting probe-level models
Name:		R-%{packname}
Version:	1.38.0
Release:	2
License:	LGPL v2+
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	bffb6a94e493311a4cb0f9cc53b696e0
Patch0:		bogus-deps.patch
URL:		http://bioconductor.org/packages/release/bioc/html/affyPLM.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-BiocGenerics
BuildRequires:	R-affy
BuildRequires:	R-preprocessCore-devel
BuildRequires:	R-gcrma
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-Biobase
Requires:	R-BiocGenerics
Requires:	R-affy
Requires:	R-preprocessCore
Suggests:	R-gcrma
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package that extends and improves the functionality of the base affy
package. Routines that make heavy use of compiled code for speed.
Central focus is on implementation of methods for fitting probe-level
models and tools using these models. PLM based quality assessment
tools.

%prep
%setup -q -c -n %{packname}
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/affyPLM.so
