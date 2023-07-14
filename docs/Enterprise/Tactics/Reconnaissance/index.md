---
sidebar_position: 1
hide:
  - toc
---

# 侦察目标

=== "侦察目标"

    **对手正试图收集可用于规划未来行动的信息。**

    侦察包括涉及对手主动或被动收集可用于支持目标定位的信息的技术。此类信息可能包括受害组织、基础设施或工作人员/人员的详细信息。攻击者可以利用此信息在攻击者生命周期的其他阶段提供帮助，例如使用收集的信息来计划和执行初始访问，确定入侵后目标的范围并确定其优先级，或者推动和领导进一步的侦察工作。

    ## 技术： 10

    | 编号                                             | 名字                                                  | 描述                                                         |                                                              |
    | -------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | [T1595](https://attack.mitre.org/techniques/T1595) |                                                       | [主动扫描](https://attack.mitre.org/techniques/T1595)        | 攻击者可以执行主动侦察扫描，以收集可在瞄准期间使用的信息。主动扫描是指攻击者通过网络流量探测受害者基础设施的扫描，而不是不涉及直接交互的其他形式的侦察。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1595/001) | [扫描 IP 块](https://attack.mitre.org/techniques/T1595/001)  | 攻击者可能会扫描受害者 IP 块，以收集可在定位期间使用的信息。公共 IP 地址可以按块或一系列顺序地址分配给组织。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1595/002) | [漏洞扫描](https://attack.mitre.org/techniques/T1595/002)    | 攻击者可能会扫描受害者以查找可在定位期间使用的漏洞。漏洞扫描通常会检查目标主机/应用程序的配置（例如：软件和版本）是否可能与攻击者可能试图使用的特定攻击的目标一致。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1595/003) | [单词列表扫描](https://attack.mitre.org/techniques/T1595/003) | 攻击者可能会使用暴力破解和爬网技术以迭代方式探测基础设施。虽然此技术采用与[暴力破解](https://attack.mitre.org/techniques/T1110)类似的方法，但其目标是识别内容和基础结构，而不是发现有效凭据。这些扫描中使用的单词列表可能包含通用的常用名称和文件扩展名或特定于特定软件的术语。攻击者还可以使用从其他侦察技术（例如：收集受害者[组织信息](https://attack.mitre.org/techniques/T1591)或[搜索受害者拥有的网站](https://attack.mitre.org/techniques/T1594)）收集的数据创建自定义的、特定于目标的词表。 |
    | [T1592](https://attack.mitre.org/techniques/T1592) |                                                       | [收集受害者主机信息](https://attack.mitre.org/techniques/T1592) | 攻击者可能会收集有关受害者主机的信息，这些信息可在定位期间使用。有关主机的信息可能包括各种详细信息，包括管理数据（例如：名称、分配的 IP、功能等）以及有关其配置的详细信息（例如：操作系统、语言等）。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1592/001) | [硬件](https://attack.mitre.org/techniques/T1592/001)        | 攻击者可能会收集有关受害者主机硬件的信息，这些信息可在定位期间使用。有关硬件基础结构的信息可能包括各种详细信息，例如特定主机上的类型和版本，以及可能指示添加防御保护的其他组件（例如：卡/生物识别读卡器、专用加密硬件等）的存在。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1592/002) | [软件](https://attack.mitre.org/techniques/T1592/002)        | 攻击者可能会收集有关受害者主机软件的信息，这些信息可以在定位期间使用。有关已安装软件的信息可能包括各种详细信息，例如特定主机上的类型和版本，以及可能存在可能指示附加防御保护的其他组件（例如：防病毒、SIEM 等）。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1592/003) | [固件](https://attack.mitre.org/techniques/T1592/003)        | 攻击者可能会收集有关受害者主机固件的信息，这些信息可在定位期间使用。有关主机固件的信息可能包括各种详细信息，例如特定主机上的类型和版本，这些详细信息可用于推断有关环境中主机的更多信息（例如：配置、用途、年龄/修补程序级别等）。 |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1592/004) | [客户端配置](https://attack.mitre.org/techniques/T1592/004)  | 攻击者可能会收集有关受害者客户端配置的信息，这些信息可在定位期间使用。有关客户端配置的信息可能包括各种详细信息和设置，包括操作系统/版本、虚拟化、体系结构（例如：32 位或 64 位）、语言和/或时区。 |
    | [T1589](https://attack.mitre.org/techniques/T1589) |                                                       | [收集受害者身份信息](https://attack.mitre.org/techniques/T1589) | 攻击者可能会收集有关受害者身份的信息，这些信息可以在定位过程中使用。有关身份的信息可能包括各种详细信息，包括个人数据（例如：员工姓名、电子邮件地址等）以及敏感详细信息（如凭据）。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1589/001) | [凭据](https://attack.mitre.org/techniques/T1589/001)        | 攻击者可能会收集可在目标定位期间使用的凭据。攻击者收集的帐户凭据可能是与目标受害组织直接关联的凭据，或者试图利用用户在个人和企业帐户中使用相同的密码的趋势。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1589/002) | [电子邮件地址](https://attack.mitre.org/techniques/T1589/002) | 攻击者可能会收集可在定位期间使用的电子邮件地址。即使存在内部实例，组织也可能具有面向公众的电子邮件基础结构和员工地址。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1589/003) | [员工姓名](https://attack.mitre.org/techniques/T1589/003)    | 攻击者可能会收集可在定位期间使用的员工姓名。员工姓名用于获取电子邮件地址，以及帮助指导其他侦察工作和/或制作更可信的诱饵。 |
    | [T1590](https://attack.mitre.org/techniques/T1590) |                                                       | [收集受害者网络信息](https://attack.mitre.org/techniques/T1590) | 攻击者可能会收集有关受害者网络的信息，这些信息可以在定位过程中使用。有关网络的信息可能包括各种详细信息，包括管理数据（例如：IP 范围、域名等）以及有关其拓扑和操作的详细信息。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1590/001) | [域属性](https://attack.mitre.org/techniques/T1590/001)      | 攻击者可能会收集有关受害者网络域的信息，这些信息可在定位期间使用。有关域及其属性的信息可能包括各种详细信息，包括受害者拥有的域以及管理数据（例如：名称、注册商等）和更直接的可操作信息，例如联系人（电子邮件地址和电话号码）、公司地址和名称服务器。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1590/002) | [域名解析](https://attack.mitre.org/techniques/T1590/002)    | 攻击者可能会收集有关受害者 DNS 的信息，这些信息可在定位期间使用。DNS 信息可能包括各种详细信息，包括注册的名称服务器以及概述目标子域、邮件服务器和其他主机寻址的记录。DNS、MX、TXT 和 SPF 记录也可能揭示第三方云和 SaaS 提供商的使用，例如 Office 365、G Suite、Salesforce 或 Zendesk。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1590/003) | [网络信任依赖关系](https://attack.mitre.org/techniques/T1590/003) | 攻击者可能会收集有关受害者的网络信任依赖项的信息，这些信息可在定位期间使用。有关网络信任的信息可能包括各种详细信息，包括已连接（并可能提升）网络访问的第二方或第三方组织/域（例如：托管服务提供商、承包商等）。 |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1590/004) | [网络拓扑](https://attack.mitre.org/techniques/T1590/004)    | 攻击者可能会收集有关受害者网络拓扑的信息，这些信息可在定位期间使用。有关网络拓扑的信息可能包括各种详细信息，包括面向外部和内部网络环境的物理和/或逻辑排列。此信息还可能包括有关网络设备（网关、路由器等）和其他基础设施的详细信息。 |
    |                                                    | [.005](https://attack.mitre.org/techniques/T1590/005) | [IP 地址](https://attack.mitre.org/techniques/T1590/005)     | 攻击者可能会收集受害者的 IP 地址，以便在定位过程中使用。公共 IP 地址可以按块或一系列顺序地址分配给组织。有关分配的 IP 地址的信息可能包括各种详细信息，例如正在使用哪些 IP 地址。IP 地址还可能使攻击者能够获取有关受害者的其他详细信息，例如组织规模、物理位置、Internet 服务提供商以及托管其面向公众的基础设施的位置/方式。 |
    |                                                    | [.006](https://attack.mitre.org/techniques/T1590/006) | [网络安全设备](https://attack.mitre.org/techniques/T1590/006) | 攻击者可能会收集有关受害者网络安全设备的信息，这些信息可在定位期间使用。有关网络安全设备的信息可能包括各种详细信息，例如已部署防火墙、内容过滤器和代理/堡垒主机的存在和细节。攻击者还可能针对有关基于受害者网络的入侵检测系统 （NIDS） 或与防御性网络安全操作相关的其他设备的信息。 |
    | [T1591](https://attack.mitre.org/techniques/T1591) |                                                       | [收集受害者组织信息](https://attack.mitre.org/techniques/T1591) | 攻击者可能会收集有关受害者组织的信息，这些信息可在定位过程中使用。有关组织的信息可能包括各种详细信息，包括部门/部门的名称、业务运营的细节以及关键员工的角色和职责。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1591/001) | [确定物理位置](https://attack.mitre.org/techniques/T1591/001) | 攻击者可能会收集受害者的物理位置，以便在定位过程中使用。有关目标组织物理位置的信息可能包括各种详细信息，包括关键资源和基础结构的存放位置。实际位置也可能表明受害者在哪个法律管辖范围内运作和/或当局。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1591/002) | [业务关系](https://attack.mitre.org/techniques/T1591/002)    | 攻击者可能会收集有关受害者业务关系的信息，这些信息可在定位过程中使用。有关组织业务关系的信息可能包括各种详细信息，包括已连接（并可能提升）网络访问的第二方或第三方组织/域（例如：托管服务提供商、承包商等）。这些信息还可能揭示受害者硬件和软件资源的供应链和运输路径。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1591/003) | [确定业务节奏](https://attack.mitre.org/techniques/T1591/003) | 攻击者可能会收集有关受害者业务节奏的信息，这些信息可以在定位过程中使用。有关组织业务节奏的信息可能包括各种详细信息，包括一周中的工作时间/天数。此信息还可能揭示购买和运送受害者硬件和软件资源的时间/日期。 |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1591/004) | [确定角色](https://attack.mitre.org/techniques/T1591/004)    | 攻击者可能会收集有关受害组织内标识和角色的信息，这些信息可在定位期间使用。有关业务角色的信息可能会揭示各种可定位的详细信息，包括关键人员的可识别信息以及他们有权访问的数据/资源。 |
    | [T1598](https://attack.mitre.org/techniques/T1598) |                                                       | [网络钓鱼获取信息](https://attack.mitre.org/techniques/T1598) | 攻击者可能会发送网络钓鱼消息，以引出可在定位期间使用的敏感信息。信息网络钓鱼是试图诱骗目标泄露信息，通常是凭据或其他可操作的信息。信息[网络钓鱼与网络钓鱼](https://attack.mitre.org/techniques/T1566)的不同之处在于，目标是从受害者那里收集数据，而不是执行恶意代码。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1598/001) | [鱼叉式网络钓鱼服务](https://attack.mitre.org/techniques/T1598/001) | 攻击者可能会通过第三方服务发送鱼叉式网络钓鱼消息，以引出可在定位期间使用的敏感信息。鱼叉式网络钓鱼信息是试图诱骗目标泄露信息，通常是凭据或其他可操作信息。信息鱼叉式网络钓鱼通常涉及社会工程技术，例如冒充有理由收集信息的来源（例如：[建立](https://attack.mitre.org/techniques/T1585)帐户或[泄露帐户](https://attack.mitre.org/techniques/T1586)）和/或发送多条看似紧急的消息。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1598/002) | [鱼叉式网络钓鱼附件](https://attack.mitre.org/techniques/T1598/002) | 攻击者可能会发送带有恶意附件的鱼叉式网络钓鱼邮件，以引出可在定位期间使用的敏感信息。鱼叉式网络钓鱼信息是试图诱骗目标泄露信息，通常是凭据或其他可操作信息。信息鱼叉式网络钓鱼通常涉及社会工程技术，例如冒充有理由收集信息的来源（例如：[建立](https://attack.mitre.org/techniques/T1585)帐户或[泄露帐户](https://attack.mitre.org/techniques/T1586)）和/或发送多条看似紧急的消息。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1598/003) | [鱼叉式网络钓鱼链接](https://attack.mitre.org/techniques/T1598/003) | 攻击者可能会发送带有恶意链接的鱼叉式网络钓鱼邮件，以引出可在定位期间使用的敏感信息。鱼叉式网络钓鱼信息是试图诱骗目标泄露信息，通常是凭据或其他可操作信息。信息鱼叉式网络钓鱼通常涉及社会工程技术，例如冒充有理由收集信息的来源（例如：[建立](https://attack.mitre.org/techniques/T1585)帐户或[泄露帐户](https://attack.mitre.org/techniques/T1586)）和/或发送多条看似紧急的消息。 |
    | [T1597](https://attack.mitre.org/techniques/T1597) |                                                       | [搜索闭源](https://attack.mitre.org/techniques/T1597)        | 攻击者可能会从封闭来源搜索和收集有关受害者的信息，这些信息可以在定位过程中使用。有关受害者的信息可以从信誉良好的私人来源和数据库中购买，例如付费订阅技术/威胁情报数据馈送。攻击者还可能从信誉较差的来源（如暗网或网络犯罪黑市）购买信息。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1597/001) | [威胁英特尔供应商](https://attack.mitre.org/techniques/T1597/001) | 攻击者可能会从威胁情报供应商处搜索私有数据，以获取可在目标定位期间使用的信息。威胁情报供应商可能会提供付费源或门户，这些源或门户提供的数据比公开报告的数据更多。尽管可能会编辑敏感详细信息（例如客户名称和其他标识符），但此信息可能包含有关违规的趋势，例如目标行业、归因声明和成功的 TTP/对策。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1597/002) | [购买技术数据](https://attack.mitre.org/techniques/T1597/002) | 攻击者可能会购买有关受害者的技术信息，这些信息可以在瞄准过程中使用。有关受害者的信息可以在信誉良好的私人来源和数据库中购买，例如付费订阅扫描数据库的馈送或其他数据聚合服务。攻击者还可能从信誉较差的来源（如暗网或网络犯罪黑市）购买信息。 |
    | [T1596](https://attack.mitre.org/techniques/T1596) |                                                       | [搜索开放技术数据库](https://attack.mitre.org/techniques/T1596) | 攻击者可以搜索免费提供的技术数据库，以获取有关受害者的信息，这些信息可以在瞄准目标时使用。有关受害者的信息可以在在线数据库和存储库中找到，例如域/证书的注册以及从流量和/或扫描中收集的网络数据/工件的公共集合。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1596/001) | [DNS/被动 DNS](https://attack.mitre.org/techniques/T1596/001) | 攻击者可能会在 DNS 数据中搜索有关受害者的信息，这些信息可以在定位期间使用。DNS 信息可能包括各种详细信息，包括注册的名称服务器以及概述目标子域、邮件服务器和其他主机寻址的记录。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1596/002) | [谁是](https://attack.mitre.org/techniques/T1596/002)        | 攻击者可能会在公开的WHOIS数据中搜索有关受害者的信息，这些信息可以在定位过程中使用。WHOIS数据由负责分配和分配域名等互联网资源的区域互联网注册管理机构（RIR）存储。任何人都可以向WHOIS服务器查询有关已注册域的信息，例如分配的IP块，联系信息和DNS名称服务器。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1596/003) | [数字证书](https://attack.mitre.org/techniques/T1596/003)    | 攻击者可能会搜索公共数字证书数据，以获取可在定位期间使用的受害者信息。数字证书由证书颁发机构 （CA） 颁发，用于以加密方式验证签名内容的来源。这些证书（例如用于加密 Web 流量（HTTPS SSL/TLS 通信）的证书）包含有关已注册组织的信息，例如名称和位置。 |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1596/004) | [内容分发网络](https://attack.mitre.org/techniques/T1596/004) | 攻击者可能会搜索有关受害者的内容分发网络 （CDN） 数据，这些数据可在定位期间使用。CDN 允许组织托管来自分布式、负载平衡的服务器阵列的内容。CDN 还允许组织根据请求者的地理区域自定义内容交付。 |
    |                                                    | [.005](https://attack.mitre.org/techniques/T1596/005) | [扫描数据库](https://attack.mitre.org/techniques/T1596/005)  | 攻击者可能会在公共扫描数据库中搜索有关受害者的信息，这些信息可以在定位过程中使用。各种在线服务不断发布互联网扫描/调查的结果，通常会收集活动 IP 地址、主机名、开放端口、证书甚至服务器横幅等信息。 |
    | [T1593](https://attack.mitre.org/techniques/T1593) |                                                       | [搜索开放网站/域](https://attack.mitre.org/techniques/T1593) | 攻击者可能会搜索免费提供的网站和/或域，以获取有关受害者的信息，这些信息可以在定位过程中使用。有关受害者的信息可以在各种在线网站上找到，例如社交媒体、新网站或托管有关业务运营信息的网站，例如雇用或请求/奖励合同。 |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1593/001) | [社交媒体](https://attack.mitre.org/techniques/T1593/001)    | 攻击者可能会在社交媒体上搜索有关受害者的信息，这些信息可以在定位过程中使用。社交媒体网站可能包含有关受害组织的各种信息，例如业务公告以及有关员工的角色、位置和兴趣的信息。 |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1593/002) | [搜索引擎](https://attack.mitre.org/techniques/T1593/002)    | 攻击者可能会使用搜索引擎来收集有关受害者的信息，这些信息可以在定位过程中使用。搜索引擎服务通常抓取在线网站以索引上下文，并且可以为用户提供专门的语法来搜索特定关键字或特定类型的内容（即文件类型）。 |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1593/003) | [代码存储库](https://attack.mitre.org/techniques/T1593/003)  | 攻击者可能会在公共代码存储库中搜索有关受害者的信息，这些信息可以在定位期间使用。受害者可以将代码存储在各种第三方网站的存储库中，例如GitHub，GitLab，SourceForge和BitBucket。用户通常通过 Web 应用程序或命令行实用程序（如 git）与代码存储库进行交互。 |
    | [T1594](https://attack.mitre.org/techniques/T1594) |                                                       | [搜索受害者拥有的网站](https://attack.mitre.org/techniques/T1594) | 攻击者可能会搜索受害者拥有的网站，以获取可在定位过程中使用的信息。受害者拥有的网站可能包含各种详细信息，包括部门/部门名称、实际位置以及有关关键员工的数据，例如姓名、角色和联系信息（例如：[电子邮件地址](https://attack.mitre.org/techniques/T1589/002)）。这些网站还可能包含突出显示业务运营和关系的详细信息。 |

=== "Reconnaissance"

    The adversary is trying to gather information they can use to plan future operations.

    Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.

    **Techniques: 10**

    | ID                                                 | Name                                                  | Description                                                  |                                                              |
    | -------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | [T1595](https://attack.mitre.org/techniques/T1595) |                                                       | [Active Scanning](https://attack.mitre.org/techniques/T1595) | Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1595/001) | [Scanning IP Blocks](https://attack.mitre.org/techniques/T1595/001) | Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1595/002) | [Vulnerability Scanning](https://attack.mitre.org/techniques/T1595/002) | Adversaries may scan victims for vulnerabilities that can be used during targeting. Vulnerability scans typically check if the configuration of a target host/application (ex: software and version) potentially aligns with the target of a specific exploit the adversary may seek to use. |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1595/003) | [Wordlist Scanning](https://attack.mitre.org/techniques/T1595/003) | Adversaries may iteratively probe infrastructure using brute-forcing and crawling techniques. While this technique employs similar methods to [Brute Force](https://attack.mitre.org/techniques/T1110), its goal is the identification of content and infrastructure rather than the discovery of valid credentials. Wordlists used in these scans may contain generic, commonly used names and file extensions or terms specific to a particular software. Adversaries may also create custom, target-specific wordlists using data gathered from other Reconnaissance techniques (ex: [Gather Victim Org Information](https://attack.mitre.org/techniques/T1591), or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)). |
    | [T1592](https://attack.mitre.org/techniques/T1592) |                                                       | [Gather Victim Host Information](https://attack.mitre.org/techniques/T1592) | Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, language, etc.). |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1592/001) | [Hardware](https://attack.mitre.org/techniques/T1592/001)    | Adversaries may gather information about the victim's host hardware that can be used during targeting. Information about hardware infrastructure may include a variety of details such as types and versions on specific hosts, as well as the presence of additional components that might be indicative of added defensive protections (ex: card/biometric readers, dedicated encryption hardware, etc.). |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1592/002) | [Software](https://attack.mitre.org/techniques/T1592/002)    | Adversaries may gather information about the victim's host software that can be used during targeting. Information about installed software may include a variety of details such as types and versions on specific hosts, as well as the presence of additional components that might be indicative of added defensive protections (ex: antivirus, SIEMs, etc.). |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1592/003) | [Firmware](https://attack.mitre.org/techniques/T1592/003)    | Adversaries may gather information about the victim's host firmware that can be used during targeting. Information about host firmware may include a variety of details such as type and versions on specific hosts, which may be used to infer more information about hosts in the environment (ex: configuration, purpose, age/patch level, etc.). |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1592/004) | [Client Configurations](https://attack.mitre.org/techniques/T1592/004) | Adversaries may gather information about the victim's client configurations that can be used during targeting. Information about client configurations may include a variety of details and settings, including operating system/version, virtualization, architecture (ex: 32 or 64 bit), language, and/or time zone. |
    | [T1589](https://attack.mitre.org/techniques/T1589) |                                                       | [Gather Victim Identity Information](https://attack.mitre.org/techniques/T1589) | Adversaries may gather information about the victim's identity that can be used during targeting. Information about identities may include a variety of details, including personal data (ex: employee names, email addresses, etc.) as well as sensitive details such as credentials. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1589/001) | [Credentials](https://attack.mitre.org/techniques/T1589/001) | Adversaries may gather credentials that can be used during targeting. Account credentials gathered by adversaries may be those directly associated with the target victim organization or attempt to take advantage of the tendency for users to use the same passwords across personal and business accounts. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1589/002) | [Email Addresses](https://attack.mitre.org/techniques/T1589/002) | Adversaries may gather email addresses that can be used during targeting. Even if internal instances exist, organizations may have public-facing email infrastructure and addresses for employees. |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1589/003) | [Employee Names](https://attack.mitre.org/techniques/T1589/003) | Adversaries may gather employee names that can be used during targeting. Employee names be used to derive email addresses as well as to help guide other reconnaissance efforts and/or craft more-believable lures. |
    | [T1590](https://attack.mitre.org/techniques/T1590) |                                                       | [Gather Victim Network Information](https://attack.mitre.org/techniques/T1590) | Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1590/001) | [Domain Properties](https://attack.mitre.org/techniques/T1590/001) | Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more directly actionable information such as contacts (email addresses and phone numbers), business addresses, and name servers. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1590/002) | [DNS](https://attack.mitre.org/techniques/T1590/002)         | Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS, MX, TXT, and SPF records may also reveal the use of third party cloud and SaaS providers, such as Office 365, G Suite, Salesforce, or Zendesk. |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1590/003) | [Network Trust Dependencies](https://attack.mitre.org/techniques/T1590/003) | Adversaries may gather information about the victim's network trust dependencies that can be used during targeting. Information about network trusts may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access. |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1590/004) | [Network Topology](https://attack.mitre.org/techniques/T1590/004) | Adversaries may gather information about the victim's network topology that can be used during targeting. Information about network topologies may include a variety of details, including the physical and/or logical arrangement of both external-facing and internal network environments. This information may also include specifics regarding network devices (gateways, routers, etc.) and other infrastructure. |
    |                                                    | [.005](https://attack.mitre.org/techniques/T1590/005) | [IP Addresses](https://attack.mitre.org/techniques/T1590/005) | Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP addresses may also enable an adversary to derive other details about a victim, such as organizational size, physical location(s), Internet service provider, and or where/how their publicly-facing infrastructure is hosted. |
    |                                                    | [.006](https://attack.mitre.org/techniques/T1590/006) | [Network Security Appliances](https://attack.mitre.org/techniques/T1590/006) | Adversaries may gather information about the victim's network security appliances that can be used during targeting. Information about network security appliances may include a variety of details, such as the existence and specifics of deployed firewalls, content filters, and proxies/bastion hosts. Adversaries may also target information about victim network-based intrusion detection systems (NIDS) or other appliances related to defensive cybersecurity operations. |
    | [T1591](https://attack.mitre.org/techniques/T1591) |                                                       | [Gather Victim Org Information](https://attack.mitre.org/techniques/T1591) | Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1591/001) | [Determine Physical Locations](https://attack.mitre.org/techniques/T1591/001) | Adversaries may gather the victim's physical location(s) that can be used during targeting. Information about physical locations of a target organization may include a variety of details, including where key resources and infrastructure are housed. Physical locations may also indicate what legal jurisdiction and/or authorities the victim operates within. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1591/002) | [Business Relationships](https://attack.mitre.org/techniques/T1591/002) | Adversaries may gather information about the victim's business relationships that can be used during targeting. Information about an organization’s business relationships may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access. This information may also reveal supply chains and shipment paths for the victim’s hardware and software resources. |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1591/003) | [Identify Business Tempo](https://attack.mitre.org/techniques/T1591/003) | Adversaries may gather information about the victim's business tempo that can be used during targeting. Information about an organization’s business tempo may include a variety of details, including operational hours/days of the week. This information may also reveal times/dates of purchases and shipments of the victim’s hardware and software resources. |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1591/004) | [Identify Roles](https://attack.mitre.org/techniques/T1591/004) | Adversaries may gather information about identities and roles within the victim organization that can be used during targeting. Information about business roles may reveal a variety of targetable details, including identifiable information for key personnel as well as what data/resources they have access to. |
    | [T1598](https://attack.mitre.org/techniques/T1598) |                                                       | [Phishing for Information](https://attack.mitre.org/techniques/T1598) | Adversaries may send phishing messages to elicit sensitive information that can be used during targeting. Phishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Phishing for information is different from [Phishing](https://attack.mitre.org/techniques/T1566) in that the objective is gathering data from the victim rather than executing malicious code. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1598/001) | [Spearphishing Service](https://attack.mitre.org/techniques/T1598/001) | Adversaries may send spearphishing messages via third-party services to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1598/002) | [Spearphishing Attachment](https://attack.mitre.org/techniques/T1598/002) | Adversaries may send spearphishing messages with a malicious attachment to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages. |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1598/003) | [Spearphishing Link](https://attack.mitre.org/techniques/T1598/003) | Adversaries may send spearphishing messages with a malicious link to elicit sensitive information that can be used during targeting. Spearphishing for information is an attempt to trick targets into divulging information, frequently credentials or other actionable information. Spearphishing for information frequently involves social engineering techniques, such as posing as a source with a reason to collect information (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)) and/or sending multiple, seemingly urgent messages. |
    | [T1597](https://attack.mitre.org/techniques/T1597) |                                                       | [Search Closed Sources](https://attack.mitre.org/techniques/T1597) | Adversaries may search and gather information about victims from closed sources that can be used during targeting. Information about victims may be available for purchase from reputable private sources and databases, such as paid subscriptions to feeds of technical/threat intelligence data. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1597/001) | [Threat Intel Vendors](https://attack.mitre.org/techniques/T1597/001) | Adversaries may search private data from threat intelligence vendors for information that can be used during targeting. Threat intelligence vendors may offer paid feeds or portals that offer more data than what is publicly reported. Although sensitive details (such as customer names and other identifiers) may be redacted, this information may contain trends regarding breaches such as target industries, attribution claims, and successful TTPs/countermeasures. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1597/002) | [Purchase Technical Data](https://attack.mitre.org/techniques/T1597/002) | Adversaries may purchase technical information about victims that can be used during targeting. Information about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to feeds of scan databases or other data aggregation services. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets. |
    | [T1596](https://attack.mitre.org/techniques/T1596) |                                                       | [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596) | Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1596/001) | [DNS/Passive DNS](https://attack.mitre.org/techniques/T1596/001) | Adversaries may search DNS data for information about victims that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1596/002) | [WHOIS](https://attack.mitre.org/techniques/T1596/002)       | Adversaries may search public WHOIS data for information about victims that can be used during targeting. WHOIS data is stored by regional Internet registries (RIR) responsible for allocating and assigning Internet resources such as domain names. Anyone can query WHOIS servers for information about a registered domain, such as assigned IP blocks, contact information, and DNS nameservers. |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1596/003) | [Digital Certificates](https://attack.mitre.org/techniques/T1596/003) | Adversaries may search public digital certificate data for information about victims that can be used during targeting. Digital certificates are issued by a certificate authority (CA) in order to cryptographically verify the origin of signed content. These certificates, such as those used for encrypted web traffic (HTTPS SSL/TLS communications), contain information about the registered organization such as name and location. |
    |                                                    | [.004](https://attack.mitre.org/techniques/T1596/004) | [CDNs](https://attack.mitre.org/techniques/T1596/004)        | Adversaries may search content delivery network (CDN) data about victims that can be used during targeting. CDNs allow an organization to host content from a distributed, load balanced array of servers. CDNs may also allow organizations to customize content delivery based on the requestor’s geographical region. |
    |                                                    | [.005](https://attack.mitre.org/techniques/T1596/005) | [Scan Databases](https://attack.mitre.org/techniques/T1596/005) | Adversaries may search within public scan databases for information about victims that can be used during targeting. Various online services continuously publish the results of Internet scans/surveys, often harvesting information such as active IP addresses, hostnames, open ports, certificates, and even server banners. |
    | [T1593](https://attack.mitre.org/techniques/T1593) |                                                       | [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593) | Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts. |
    |                                                    | [.001](https://attack.mitre.org/techniques/T1593/001) | [Social Media](https://attack.mitre.org/techniques/T1593/001) | Adversaries may search social media for information about victims that can be used during targeting. Social media sites may contain various information about a victim organization, such as business announcements as well as information about the roles, locations, and interests of staff. |
    |                                                    | [.002](https://attack.mitre.org/techniques/T1593/002) | [Search Engines](https://attack.mitre.org/techniques/T1593/002) | Adversaries may use search engines to collect information about victims that can be used during targeting. Search engine services typical crawl online sites to index context and may provide users with specialized syntax to search for specific keywords or specific types of content (i.e. filetypes). |
    |                                                    | [.003](https://attack.mitre.org/techniques/T1593/003) | [Code Repositories](https://attack.mitre.org/techniques/T1593/003) | Adversaries may search public code repositories for information about victims that can be used during targeting. Victims may store code in repositories on various third-party websites such as GitHub, GitLab, SourceForge, and BitBucket. Users typically interact with code repositories through a web application or command-line utilities such as git. |
    | [T1594](https://attack.mitre.org/techniques/T1594) |                                                       | [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594) | Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: [Email Addresses](https://attack.mitre.org/techniques/T1589/002)). These sites may also have details highlighting business operations and relationships. |