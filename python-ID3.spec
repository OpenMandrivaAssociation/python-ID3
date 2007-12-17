%define version 1.2
%define release %mkrel 9
%define fname id3-py
%define oname ID3

Name: python-%oname
Version: %{version}
Release: %{release}
Source0: http://id3-py.sourceforge.net/%{fname}_%{version}.tar.bz2
Summary: Python module for manipulating ID3 information tags on MP3 audio files
License: GPL
Group: Development/Python
Url: http://id3-py.sourceforge.net
Requires: python
BuildRequires: python-devel >= %{pyver}
BuildArch: noarch

%description
This is a simple Python module for retrieving and setting so-called ID3
tags on MP3 compressed audio files through an object-oriented interface.
MP3 players generally use this simple information for display track title,
artist name, and album title while playing the sound file.

%prep
%setup -q -n %fname-%version

%build
#python -c "import ID3"
python setup.py build
%install
rm -rf %buildroot
python setup.py install --root %buildroot

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES COPYING README id3-tagger.py
%py_puresitedir/ID3.py
%py_puresitedir/ID3.pyc
%py_puresitedir/*.egg-info


