Summary:	Additional themes for GAV
Summary(pl):	Dodatkowe motywy dla GAV
Name:		gav-themes
Version:	0.7.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gav/%{name}-%{version}.tar.gz
# Source0-md5:	26a5c0b95f3019b5297f36d572b665d6
URL:		http://gav.sourceforge.net/themes.php
Requires:	gav = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional themes for GAV.

%description -l pl
Dodatkowe motywy dla GAV.

%prep
%setup -q -n themes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/gav/themes

cp -R * $RPM_BUILD_ROOT%{_datadir}/games/gav/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/gav/themes/*
