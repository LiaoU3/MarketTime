%global __requires_exclude ^python3.13dist\\(datetime\\)$

Name:           MarketTime
Version:         %{version}
Release:        1%{?dist}
Summary:        A Python module for stock and future market time detection

License:        MIT
URL:            https://github.com/LiaoU3/MarketTime
Source0:        MarketTime-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3 >= 3.10, python3-setuptools
Requires:       python3 >= 3.10

%description
MarketTime is a Python module designed to track and detect market time in Taiwan,
focusing on stock and futures markets. It provides functionalities to manage and
analyze market time data, including determining whether the market is open,
retrieving the next and last market open times, and checking for expiration
days in futures markets.

%prep
%setup -q

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root=%{buildroot} --optimize=1

%files
%defattr(-,root,root,-)
%{python3_sitelib}/MarketTime*
%doc README.md LICENSE

%changelog
* Fri Mar 21 2025 Vincent Liao <vincent932693@gmail.com> - 1.1.3-1
- Initial RPM package for MarketTime
