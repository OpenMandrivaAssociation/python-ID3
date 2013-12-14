%define fname id3-py
%define oname id3

Name:      python-%{oname}
Version:   1.2
Release:   18
Source0:   http://id3-py.sourceforge.net/%{fname}_%{version}.tar.bz2
Summary:   Python module for manipulating ID3 information tags on MP3 audio files
License:   GPLv2+
Group:     Development/Python
Url:       http://id3-py.sourceforge.net
Requires:  python
BuildArch: noarch
BuildRequires: python-devel

%description
This is a simple Python module for retrieving and setting so-called ID3
tags on MP3 compressed audio files through an object-oriented interface.
MP3 players generally use this simple information for display track title,
artist name, and album title while playing the sound file.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
python setup.py install --root %{buildroot}

%files
%doc CHANGES COPYING README id3-tagger.py
%{py_puresitedir}/ID3.py*
%{py_puresitedir}/*.egg-info


