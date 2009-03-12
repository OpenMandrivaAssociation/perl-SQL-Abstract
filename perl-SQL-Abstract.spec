%define module	SQL-Abstract
%define name	perl-%{module}
%define version 1.50
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
summary:	Generate SQL from Perl data structures
license:	Artistic
group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/SQL/%{module}-%{version}.tar.gz
buildRequires:	perl(Test::Warn)
buildRequires:	perl(Test::Deep)
buildRequires:	perl(Test::Exception)
buildarch:	noarch
buildroot:	%{_tmppath}/%{name}-%{version}

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
%doc Changes
%{perl_vendorlib}/SQL
%{_mandir}/*/*

