Summary:	Nagios Image Packs
Name:		nagios-imagepaks
Version:	1.0
Release:	%mkrel 5
License:	Open Source
Group:		Networking/WWW
URL:		http://www.nagios.org/download/extras.php
Source0:	http://dl.sourceforge.net/nagios/imagepak-base.tar.gz
Source1:	http://dl.sourceforge.net/nagios/imagepak-bernhard.tar.gz
Source2:	http://dl.sourceforge.net/nagios/imagepak-cook.tar.gz
Source3:	http://dl.sourceforge.net/nagios/imagepak-didier.tar.gz
Source4:	http://dl.sourceforge.net/nagios/imagepak-remus.tar.gz
Source5:	http://dl.sourceforge.net/nagios/imagepak-satrapa.tar.gz
Source6:	http://dl.sourceforge.net/nagios/imagepak-werschler.tar.gz
Source7:	http://glen.alkohol.ee/pld/nagios/imagepak-pld-20050402.4.tar.bz2
Source8:	mandriva.png
Requires:	nagios-www
BuildArch:	noarch
BuildRequires:	imagemagick
BuildRequires:	gd-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%define		_logodir	%{_datadir}/nagios/www/images/logos

%description
Image packs are provided so that you have some colorful OS and device images to
beautify your CGIs in Nagios. Each pack includes GIF, JPEG, PNG, and GD2
versions of each icon.

%prep

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_logodir}/{bernhard,cook}
tar -xz -C %{buildroot}%{_logodir} -f %{SOURCE0}
tar -xz -C %{buildroot}%{_logodir}/bernhard --strip-components=1 -f %{SOURCE1}
tar -xz -C %{buildroot}%{_logodir}/cook -f %{SOURCE2}
tar -xz -C %{buildroot}%{_logodir} -f %{SOURCE3}
tar -xz -C %{buildroot}%{_logodir} -f %{SOURCE4}
tar -xz -C %{buildroot}%{_logodir} -f %{SOURCE5}
tar -xz -C %{buildroot}%{_logodir} -f %{SOURCE6}
tar -xj -C %{buildroot}%{_logodir}/base --strip-components=1 -f %{SOURCE7}

# shiny mandriva icon
install -m 644 %{SOURCE8} %{buildroot}%{_logodir}/base/mandriva.png
convert %{SOURCE8} %{buildroot}%{_logodir}/base/mandriva.gif
convert %{SOURCE8} %{buildroot}%{_logodir}/base/mandriva.jpg
pngtogd2  %{SOURCE8} %{buildroot}%{_logodir}/base/mandriva.gd2 0 1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_logodir}/*
