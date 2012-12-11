%define upstream_name	 SQL-Abstract
%define upstream_version 1.72

# We need this to avoid circular deps
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBIx::Class::Storage::Statistics\\)'
%else
%define _requires_exceptions DBIx::Class::Storage::Statistics
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Generate SQL from Perl data structures
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SQL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Hash::Merge)
BuildRequires:	perl(Getopt::Long::Descriptive)
BuildArch:	noarch

%description
This module was inspired by the excellent L<DBIx::Abstract>.
However, in using that module I found that what I really wanted
to do was generate SQL, but still retain complete control over my
statement handles and use the DBI interface. So, I set out to
create an abstract SQL generation module.

While based on the concepts used by DBIx::Abstract, there are
several important differences, especially when it comes to WHERE
clauses. I have modified the concepts used to make the SQL easier
to generate from Perl data structures and, IMO, more intuitive.
The underlying idea is for this module to do what you mean, based
on the data structures you provide it. The big advantage is that
you don't have to modify your code every time your data changes,
as this module figures it out.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.720.0-2mdv2011.0
+ Revision: 657175
- add br
- rebuild for updated spec-helper

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.720.0-1mdv2011.0
+ Revision: 625281
- update to new version 1.72

* Mon Nov 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.710.0-1mdv2011.0
+ Revision: 597763
- update to 1.71

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.670.0-1mdv2011.0
+ Revision: 552627
- update to 1.67

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.650.0-1mdv2010.1
+ Revision: 536211
- update to 1.65

* Wed Mar 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.630.0-1mdv2010.1
+ Revision: 527171
- update to 1.63

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 1.620.0-1mdv2010.1
+ Revision: 519956
- update to 1.62

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.610.0-1mdv2010.1
+ Revision: 502107
- update to 1.61

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2010.0
+ Revision: 447607
- update to 1.60

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-1mdv2010.0
+ Revision: 432827
- update to 1.58

* Fri Sep 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.570.0-1mdv2010.0
+ Revision: 430469
- update to 1.57

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2010.0
+ Revision: 404412
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.56-1mdv2010.0
+ Revision: 383541
- update to new version 1.56

* Tue May 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.55-1mdv2010.0
+ Revision: 377515
- update to new version 1.55

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.54-1mdv2010.0
+ Revision: 373792
- update to new version 1.54

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.53-1mdv2010.0
+ Revision: 370178
- update to new version 1.53

* Thu Mar 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.50-1mdv2009.1
+ Revision: 354251
- new version

* Thu Jul 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.0
+ Revision: 233435
- new version

* Wed Jul 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.0
+ Revision: 233039
- new version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.22-1mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.22-1mdv2008.0
+ Revision: 23909
- 1.22


* Sun Mar 12 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdk
- New release 1.21

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdk
- New release 1.20
- fix source URL

* Tue Aug 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.19-1mdk
- new release
- rewrite spec file (cpan2rpm sux white bears)

* Thu Mar 17 2005 Bruno Cornec <bcornec@mandrakesoft.org> 1.18-1mdk
- Initial build.

