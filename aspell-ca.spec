Summary:	Catalan dictionary for aspell
Summary(ca):	Diccionari catalø per aspell
Summary(pl):	Kataloñski s³ownik dla aspella
Name:		aspell-ca
Version:	0.50
%define	subv	2
Release:	1
Epoch:		1
License:	GPL (?)
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ca/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalan dictionary (i.e. word list) for aspell.

%description -l ca
Diccionari catalø per aspell.

%description -l pl
Kataloñski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright
%lang(ca) %doc doc/LLEGEIX
%{_libdir}/aspell/*
%{_datadir}/aspell/*
