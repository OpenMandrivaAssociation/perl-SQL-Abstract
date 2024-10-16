%define upstream_name	 SQL-Abstract
%define upstream_version 1.77

# We need this to avoid circular deps
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DBIx::Class::Storage::Statistics\\)'
%else
%define _requires_exceptions DBIx::Class::Storage::Statistics
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generate SQL from Perl data structures
License:	Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SQL/SQL-Abstract-%{upstream_version}.tar.gz

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
