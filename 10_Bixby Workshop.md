#  Bixby Workshop

- 2019.04.16(화)
- 독창성, 잠재가능성, 기능성, 유용성

###  특장점

- Appless : 앱 설치 없이 실행가능 
- 재확인 및 자동결제, 리와인드 기능
- 사용 패턴, 경험에 따라 의사 결정 속도 강화 
- 대화 맥락 기억 
  - 강남역 맛집 찾아줘 -> 중국음식점 -> 주차되는 곳만 찾아줘 : 결과 중 검색 기능인듯

###  Tech.Support

- Bixby Developer Day 
- Office Hour (개발지원팀 면담, 비즈니스 분야 포함)
- [BixbyDevelopersGithub](https://github.com/bixbydevelopers)
- [BixbyOnlineTechSupport](https://support.bixbydevelopers.com/hc/en-us)
- 외 slack, mail 활용



###  Develop Flow

Client -> Bixby Server (ASR -> NLU -> Capsule(Code)) -> External Server(DB) , mobile(Client) (Bixby는 무엇일까요? 사진참고, 진석)

1. Client의 발화 중 중요하게 생각되는 명령과 의도를 파악한다. - Modeling  

2. 코드 안에서 Learning하는 코드를 탐색 (Keyword중심 작업) - Modeling 

3. Business Logic : 처리 (맛집정보를 찾는 open API 돌리기, 외부 서버 활용
   - 여기까지가 우리가 기본적으로 구현해야하는 부분 
4. Bixby UI, UX 작업 
   - 이 또한 중요하다. 

5. 자연어에 대한 Training 

| Modeling                                                     | Biz Logic                                                    | UI/UX                         | Training                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------------------- | ----------------------------- |
| Concept<br/>발화변수, 발화 인식 및 발화 결과를 리턴할 깨 필요한 값 | Javascript code                                              | Bixby Views                   | 발화 Training<br/>NL Training |
| Actions<br/>발화함수, 액션 코드에 따라 발화를 자르고 분류함  | : 컨셉, 액션을 바탕으로 서비스 코드 구현 <br/>서비스 API 연동 | : 라이브러리가 제공된다.      | Debug<br/>동작확인            |
| `.bxb`                                                       | `.js`                                                        | `.view.bxb`<br/>`.layout.bxb` |                               |

- `.bxb` : 코드가 길어지면 코드파악 및 탐색이 힘든 Json 파일의 단점을 보완
- `.view.bxb` : 개략적인 레이아웃 
- `.layout.bxb` : CSS와 유사한 역할, 세부적인 레이아웃



###  Bixby Studio

- [BixbySampleCode](https://bixbydevelopers.com/dev/docs/sample-capsules/samples)

  

File- NewCapsule- CapsuleID (서버에서 특정하기위한 ID) : `팀아이디.프로젝트명`

ex) example.plus : 예시코드  

ex) playground.plus : 스튜디오 내에서만 개발. 단말실행 및 배포는 안한다. 

ex) teamname.plus 



Developers.com- Teams & Capsule- Create Team

상단 CurrentTeam : 팀네임 그대로 create Project 에 가져와서 생성

``` bxb
capsule {
  id (playground.testtt)
  version (0.1.0)
  format (3) 
//   format 은 현재 3으로 사용하면 된다. 
  targets {
    target (bixby-mobile-en-US) {enabled (false)}  // 지원닫음 
//     어떤 타겟을 대상으로 할 것인가? 모바일인지, 스피커인지, 영어인지, 한국어인지.
//     위 코드 ; 내 캡슐은 빅스비 환경에서 모바일 단말, 영어 환경에서 들어왔다, 라고 명시되어있음
    target (bixby-mobile-ko-KR) {enabled (true)} //지원열기
//     언어코드는 일반적인 랭귀지코드 사용하면 됨
//     리소스 -new - training - training 언어 선택 가능 , 만약 언어를 enable False처리해놓으면 training 언어가 닫혀있음을 확인할 수 있다. 
  }
}
```

`/models` : 디렉토리 생성 

`/resource` : UI UX 정보



code, mocels, resource 폴더가 기본

/scenario/scenario.md

``` markdown
##  시나리오 
- 7더하기 3은 얼마일까? 
- 내가 궁금한데 2 더하기 3을 알려줘 
- 더하기 해줘 7더하기 0


##  모델링 
- plusoperation (Utterance Function = Action)
- calculation (Action Type)
- 키워드 파악 및 변수명 설정 : 7=LeftOperand, '더하기'=Operator, 3=RightOperand (Input Concept) *여기서 Operator는 생략해도 된다. 왜?????????
- Results (Structure): (Output Concept)

```

create new file - fileType : Model - Template : Action - Name :PlusOperation 

``` bxb
action (PlusOperation) {
  description (__DESCRIPTION__)
  collect {
    input (__INPUT_NAME__) {
      type (__INPUT_TYPE__)
      min (Optional) max (One)
    }
  }
  output (__OUTPUT__)
}

```

models/action , models/concept 

concept - model - integer - name : LeftOperand, RightOperand

models/action/ - new file - model - structure - Results ( =  action/ plusoper...bxb /output (Results)이므로 이름 맞춤 )





비즈니스모델 로직생성 하기

code/ - new - action javascript - PlusOperation.js

``` javascript
module.exports.function = function plusOperation (leftOperand,rightOperand ) {
  const console = require('console');
  const result = leftOperand + rightOperand;
  const operatorName = '더하기';
  console.log('result is' + result);
  
  const result = {
    operator: operatorName,
    result: result
  };
  return result; 
}
```

resources/endpoints /

resource/training/  - adding New Training  : 시나리오.md 중 시나리오 복붙

training - 추가된 시나리오 NL - 7 클릭 - LeftOperand , 3클릭 - RightOperand - Done

compile NL Model : 자연어처리 

Open in Simulator - RunNL : 결과 볼 수 있다. 



views list 또한 개발센터에 있음- BixbyViews (ex. resultview .. ) 







###  단말테스트 

좌측 구름모양 submission - create new submission 

단말에서 - 빅스비 클라이언트 실행 - 좌측 세로3점 클릭 - 설정 - 빅스비 버전 빠르게 여러번 터치 : 개발자 버전 활성화 - 뒤로 - 개발자옵션 - 디바이스로 테스트하기 활성 - revision ID - 입력 - `2019-1..` - 로그인 : 빅스비 개발센터(스튜디오를 로그인한) 계정 - 음성으로 테스트 

일반모드로 빅스비를 사용하려면 개발자모드를 비활성해야 한다. 

