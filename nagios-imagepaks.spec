Summary:	Nagios Image Packs
Name:		nagios-imagepaks
Version:	1.0
Release:	6
License:	Open Source
Group:		Networking/WWW
URL:		https://www.nagios.org/download/extras.php
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


%changelog
* Tue Dec 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-5mdv2009.1
+ Revision: 321455
- adaptation for new nagios web files location

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-4mdv2009.0
+ Revision: 253547
- rebuild

* Wed Jan 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2008.1
+ Revision: 157185
- add shiny mandriva icon

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2008.0
+ Revision: 13807
- Import nagios-imagepaks



* Wed Apr 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.1
- initial Mandriva package (pld import)
