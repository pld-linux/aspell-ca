Summary:	Catalan dictionary for aspell
Summary(ca):	Diccionari catal� per aspell
Summary(pl):	Katalo�ski s�ownik dla aspella
Name:		aspell-ca
Version:	20040130
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ca/aspell6-ca-%{version}-%{subv}.tar.bz2
# Source0-md5:	5dfeebdfbe68556e70abfa95dd775263
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalan dictionary (i.e. word list) for aspell.

%description -l ca
Diccionari catal� (lista de paraules) per aspell.

%description -l pl
Katalo�ski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n aspell6-ca-%{version}-%{subv}

mv -f doc/index.{php,html}

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
%doc Copyright README
%lang(ca) %doc doc/index.*
%{_libdir}/aspell/*
%{_datadir}/aspell/*
