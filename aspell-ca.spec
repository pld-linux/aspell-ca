Summary:	Catalan dictionary for aspell
Summary(ca.UTF-8):	Diccionari català per aspell
Summary(pl.UTF-8):	Kataloński słownik dla aspella
Name:		aspell-ca
Version:	2.1.5
%define	subv	1
Release:	2
Epoch:		2
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ca/aspell6-ca-%{version}-%{subv}.tar.bz2
# Source0-md5:	153d26f724866909c6faf49eecefe8b3
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
BuildRequires:	which
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalan dictionary (i.e. word list) for aspell.

%description -l ca.UTF-8
Diccionari català (lista de paraules) per aspell.

%description -l pl.UTF-8
Kataloński słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-ca-%{version}-%{subv}

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
%doc Copyright README doc/ChangeLog
%{_prefix}/lib/aspell/ca-*.*
%{_prefix}/lib/aspell/ca.alias
%{_prefix}/lib/aspell/catalan.alias
%{_prefix}/lib/aspell/catalan-general.alias
%{_prefix}/lib/aspell/catalan-valencia.alias
%{_datadir}/aspell/ca.dat
%{_datadir}/aspell/ca_affix.dat
