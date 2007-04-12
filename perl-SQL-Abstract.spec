%define module	SQL-Abstract
%define name	perl-%{module}
%define version 1.21
%define release 1mdk

Name:		%{name}
Version:	%{version}
Release:	%{release}
summary:	Generate SQL from Perl data structures
license:	Artistic
group:		Development/Perl
source:		http://search.cpan.org/CPAN/authors/id/N/NW/NWIGER/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
buildroot:	%{_tmppath}/%{name}-%{version}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
buildarch:	noarch

%description
This module was inspired by the excellent L<DBIx::Abstract>.
However, in using that module I found that what I really wanted
to do was generate SQL, but still retain complete control over my
statement handles and use the DBI interface. So, I set out to
create an abstract SQL generation module.

While based on the concepts used by L<DBIx::Abstract>, there are
several important differences, especially when it comes to WHERE
clauses. I have modified the concepts used to make the SQL easier
to generate from Perl data structures and, IMO, more intuitive.
The underlying idea is for this module to do what you mean, based
on the data structures you provide it. The big advantage is that
you don't have to modify your code every time your data changes,
as this module figures it out.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/SQL
%{_mandir}/*/*
