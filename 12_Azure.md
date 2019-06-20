# Azure

## 개요 

- Microsoft Azure , 마이크로소프트 애저 

- 클라우드 컴퓨팅 플랫폼 

- 대표 서비스 

  - 컴퓨트 : 가상머신 , 앱서비스, 웹사이트, Webjobs
  
  - 모바일 : Mobile Engagement, HockeyApp 
  
  - 스토리지 : Storage, Table, Blob , Queue, File
  
  - 데이터관리 : Azure Search, DocumentDB, Redis Cache, StorSimple, SQL DB , SQL Data Warehouse 
  
  - 메시징 : 이벤트허브, 큐, 토픽, 릴레이
  
  - 미디어 : 인코딩, 콘텐츠보호 스트리밍등에 사용되는 PaaS
  
  - CDN : 오디오, 비디오, 애플리케이션, 이미지, 기타 정적 파일을 위한 글로벌 콘텐츠 전송 네트워크
  
  - 개발자 : Application Insights, Visual Studio Team 
  
  - 관리 : Azure Automation , Microsoft SMA
  
  - 기계학습 : Microsoft Azure Machine Learning (Azure ML)
  
    

##  Cloud Computing 

###  what is Cloud Computing

- 인터넷을 통해 서버, 스토리지, 데이터베이스, 네트워킹, 소프트웨어, 분석, 인텔리전스 등의 컴퓨팅 서비스를 제공하는 것
- 클라우딩 컴퓨팅을 통해 더 빠른 혁신과 유연한 리소스를 제공하고 대규모 경영의 이익 효과를 누릴 수 있다. 
- 일반적으로 사용한 클라우드 서비스에 대해서만 요금을 지불하므로, 운영 비용을 낮추고 인프라를 보다 효율적으로 운영할 수 있다. 
- 그뿐만 아니라, 비즈니스 요구 사항의 변화에 따라 규모를 조정할 수 있다.

###  Benefit

- **비용**
  - HW 및 SW를 구입하고 on-site data center 설치 및 운영하면서 발생하는 지출을 줄일 수 있다. 
  - 서버 랙, 전원 및 냉각에 사용되는 상시 대기 전기세, 인프라 관리를 위한 IT 전문가 비용 등의 비용이 절감된다. 
- **속도**
  - 대부분의 클라우드 컴퓨팅 서비스는 주문형 셀프 서비스로 제공된다. 
  - 따라서 많은 양의 컴퓨팅 리소스도 대부분 몇 번의 마우스 클릭으로 몇 분 만에 프로비전될 수 있다. 
  - 이로써 기업에 많은 유연성이 제공되며, 용량 계획 부담을 덜 수 있다.
- **확장성**
  - 탄력적인 확장은 클라우드 컴퓨팅 서비스의 큰 이점 중 하나
  - 필요한 때에 적절한 지리적 위치에서 대략적인 컴퓨팅 성능, 스토리지, 대역폭 등 적절한 양의 IT 리소스를 제공하는 것을 의미.
- **생산성**
  - 일반적으로 온사이트 데이터 센터에는 하드웨어 설치, 소프트웨어 패치 및 기타 시간이 오래 걸리는 IT 관리 작업 등 많은 “래킹과 스태킹(racking and stacking)”이 필요 
  - 클라우드 컴퓨팅을 사용하면 이러한 작업의 상당수가 불필요
  - 따라서 IT 팀은 더 중요한 비즈니스 목표를 달성하는 데 시간을 투자 가능
- **성능** 
  - 대규모의 클라우드 컴퓨팅 서비스가 전 세계에 위치한 보안 데이터 센터 네트워크에서 실행된다.
  - 이러한 데이터 센터는 최신 세대의 빠르고 효율적인 컴퓨팅 하드웨어로 정기적으로 업그레이드된다. 
  - 따라서 일반 개별 기업이 보유한 데이터 센터와 비교하면 애플리케이션의 네트워크 대기 시간 단축과 규모의 경제 등의 이점 제공 가능
- **안정성**
  - 클라우드 공급자 네트워크의 여러 중복 사이트에 데이터 미러링 가능
  - 따라서 데이터 백업, 재해 복구 및 비즈니스 연속성을 더 쉽게 제공
  - 비용 또한 절약  
- **보안**
  - 많은 클라우드 공급자가 전체적인 보안 태세를 강화하는 광범위한 정책 집합, 기술 및 컨트롤을 제공하여 데이터, 앱 및 인프라를 잠재적인 위협으로부터 보호.



###  Types 

> 모든 클라우드가 같지 않으며 하나의 클라우드 컴퓨팅 유형만이 누구에게나 적합한 것은 아니다. 여러 가지 서로 다른 모델, 유형 및 서비스가 결합되어 사용자에게 적합한 솔루션을 제공한다.
>
> 먼저, 클라우드 서비스를 구현할 클라우드 배포 유형 또는 클라우드 컴퓨팅 아키텍처를 결정해야 한다. 

- **Public cloud**
  - 인터넷을 통해 서버 및 스토리지와 같은 컴퓨팅 리소스를 제공하는 타사 [클라우드 서비스 공급자](https://azure.microsoft.com/en-us/overview/choosing-a-cloud-service-provider/)가 소유하고 운영
  - 대표적인 예 : Microsoft Azure
  - 모든 하드웨어, 소프트웨어 및 기타 지원 인프라를 클라우드 공급자가 소유, 관리
  - 사용자는 웹 브라우저를 사용하여 이러한 서비스에 액세스하고 계정을 관리
- **Private cloud**
  - 단일 비즈니스 또는 조직에서 독점적으로 사용되는 클라우드 컴퓨팅 리소스
  - 회사의 실제 온사이트 데이터 센터 내에 배치 가능 
  - 일부 회사에서는 해당 클라우드를 호스트하기 위해 타사 서비스 공급자에 비용을 지급하기도 한다. 
  - 서비스와 인프라가 개인 네트워크에서 유지 관리되는 클라우드
- **Hybrid cloud**
  - 퍼블릭 클라우드와 프라이빗 클라우드 간에 데이터와 응용 프로그램을 공유 및 결합 할 수 있는 기술 
  - 비즈니스에 더 높은 유연성, 더 많은 개발 옵션을 제공하며 기존 인프라, 보안 및 규정 준수를 최적화하도록 지원



##  Cloud Service 

###  Types

- **IaaS**

  - Infrastructure as a service
  - 클라우드 컴퓨팅 서비스의 가장 기본적인 범주
  - 클라우드 공급자로부터 종량제 방식으로 서버와 VM(가상 머신), 스토리지, 네트워크, 운영 체제 등의 IT 인프라를 대여
- **PaaS**
  - Platform as a service
  - 소프트웨어 응용 프로그램을 개발, 테스트, 제공 및 관리하기 위한 주문형 환경을 제공하는 클라우드 컴퓨팅 서비스
  - 개발자가 개발에 필요한 서버, 저장소, 네트워크 및 데이터베이스의 기본 인프라를 설정하거나 관리할 필요 없이 더 쉽고 빠르게 웹앱이나 모바일 앱을 만들 수 있도록 설계됨
- **Serverless**
  - PaaS와 중첩된 서버리스 컴퓨팅은 필요한 서버와 인프라를 지속해서 관리하는 데 시간을 소비하지 않고 앱 기능을 빌드하는 데 초점 
  - 클라우드 공급자가 용량 계획 및 서버 관리
  - 서버리스 아키텍처는 확장성이 높고 이벤트를 기반으로 하며 특정 함수 또는 트리거가 발생하는 경우에만 리소스 사용
- **Saas** 
  - Software as a service
  - 인터넷을 통해 주문형과 일반적인 구독 방식으로 소프트웨어 응용 프로그램을 제공하는 방법
  - 클라우드 공급자는 소프트웨어 애플리케이션과 기본 인프라를 호스트하고 관리하며 소프트웨어 업그레이드 및 보안 패치와 같은 유지 관리를 처리
  - 사용자는 일반적으로 휴대폰, 태블릿 또는 PC에서 웹 브라우저를 사용하여 인터넷을 통해 애플리케이션에 연결합니다.




##   Global Infra

- 데이터 레지던시로 수준높은 복원력을 확보할 수 있다. 
- 동일한 데이터 레지던시 경계 내에서 지역과 가용성영역을 연결하여 높은 가용성과 데이터 복구 및 백업이 가능하다.

![](https://azurecomcdn.azureedge.net/cvt-9220ec323630fcfdae245cb33c654270938df22b468039020675a539f10d1706/images/page/global-infrastructure/regions/understand-regional-architecture.png)



###  Region 

- 애저는 현재(2019.6월 기준) 140개 국가에서 54개의 리전을 사용할 수 있다.
- 정의된 대기 시간별로 나뉨 
- 데이터센터가 지역별 짧은 대기시간 네트워크를 통해 연결되고, 리전은 그 집합을 의미 

###  Geographies

- 두개 이상의 리전을 포함하는 시장
- 데이터 레지던시 및 준수 규정별로 나뉜다. 
- 특정 데이터 레지던시 및 규정 준수 요구사항이 있는 고객은 지오그래피를 통해 데이터 및 응용프로그램을 가까이 유지할 수 있다. 
- 지오그래피는 전용 대용량 네트워킹 인프라와 연결되어 전체 지역에서 발생하는 오류를 커버할 수 있는 내결함성을 갖춘다. 

###  Availability Zones 

- 애저 지역 내에서 물리적으로 분류된 위치 
- 각 가용성 영역(Availability Zone)은 독립된 전원, 냉각 및 네트워킹을 갖춘 하나 이상의 데이터 센터로 구성된다. 
- 가용성영역에서는 가용성이 높고 대기 시간이 짧은 응답을 통해 주요 업무용 애플리케이션을 실행할 수 있다.



##  Azure vs. AWS 

> Microsoft에서 어필하는 Azure의 경쟁력 

- **Pay less**  "Only Azure offers these prigin advantages "

  ![](https://azurecomcdn.azureedge.net/cvt-9220ec323630fcfdae245cb33c654270938df22b468039020675a539f10d1706/images/section/pay-less-with-azure/azure-vs-aws.png)

  - Saving through existing licenses 
  - Free extended security update 

- **"95+% of 500 company use Azure"** by Fortune

  -  30+ years : experience serving enterprise customers
  - 68,000+ partners : The industry’s broadest and most experienced partner network to support your needs
  - 90+ certifications : The most comprehensive set of compliance offerings of any cloud service provider

- **Get peace of mind with the most trusted cloud**

- **Turn your ideas into solutions faster**

- **Gain true consistency across your hybrid environment**

- **Innovate with unmached intelligence**

- **More global regions than any other cloud provider**

- **Make the smart choice for retail**

