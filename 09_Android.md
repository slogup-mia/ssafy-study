#  Android

## 안드로이드 스튜디오 셋팅

- https://developer.android.com/studio
  - Do not import settings
  - Install Type - Custom - ... - Andorid SDK Location - 탐색이 편한 장소에 넣는다. (보통 C\SDK폴더생성) - ... - Finish 
  - 설치완료 창 -하단 우측 Configure - SDK Manager - Show Pakage Details 체크 ( 버전체크) - Android 9.0 체크해제 (현재 호환이 안되는 기종을 쓰는 유저가 있음) -  Android 7.1.1 (Nougat) - Android for Andorid 25 체크 - Apply
  - Configure - SDK Manager에서  Android SDK Location 이 잘 잡혀있는지 다시 확인 필수 
  - New Project - Empty Activity 가 가장 편리 - ★ Package name에 example 이 들어가면 구글플레이에 배포 불가하므로 네이밍 필수 - ★ Minimum API level 을 API 25: Android 7.1.1 (Nougat) 로 버전 맞춤 (  인스톨할때  Android 7.1.1 (Nougat) 로 설치했으므로) 
  - 프로젝트 환경을 Android -> Project로 변경 (편리) - 싱크 완료까지 기다리기
  - File- Setting - Editer - General -  Auto Import  - Add unambiguous import.... / Optimize import... 모두 활성화 



- 우측 상단 AVD Manager(emulator) 클릭- 모바일 사이즈 Pixel (보편 사이즈) 선택 - Nougat 7.1.1 (버전에 맞게) Download(최초실행시) - ... - Action ▶ 클릭

