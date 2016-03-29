Name:软件包名
Version:游版本号
Release:发行编号	1%{?dist}
Summary:一行简短的软件包介绍
Group:指定软件包组
License:授权协议，必须是开源许可证。
URL:该软件包的项目主页
Source0:软件源码包的 URL 地址。
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
      #$RPM_BUILD_ROOT 代替 %{buildroot}
BuildRequires:编译软件包所需的依赖包列表，以逗号分隔。
Requires:安装软件包时所需的依赖包列表，以逗号分隔

%description程序的详细/多行描述，请使用美式英语   

%prep  程序的详细/多行描述，请使用美式英语
%setup -q

%build  包含构建阶段执行的命令，构建完成后便开始后续安装
%configure
make %{?_smp_mflags}

%install 包含安装阶段执行的命令。
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean 清理安装目录的命令
rm -rf %{buildroot}
 
%files 需要被打包/安装的文件列表
%defattr(-,root,root,-)
%doc

%changelog




