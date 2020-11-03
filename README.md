# **ROS2 Lecture Examples**

- [HEBE0028]ROS  Fall 2020
- 로봇운영체제 수강생들을 위한 강의에 사용된 예제코드 입니다.
- 👍

---

## Package Name
- 수업 중 패키지 충돌을 피하기 위해 package 명을 본인의 이니셜 등으로 변경하여 사용하세요.
- package를 새로 만들 경우 workspace의 /src 경로에서 생성해야 합니다.
- package 이름을 바꿀 때 (기존 package 변경) 
	- src 폴더의 package 폴더 이름 변경
    - src/<나의패키지> 경로 안의 패키지 폴더 이름 변경
    - src/<나의패키지>/resource 경로 안의 파일명 변경
    - package.xml 상단의 package name 변경
    - setup.cfg 에서 package name 변경
    - setup.py 에서 package name 변경, console_scripts 패키지 경로 변경
    
## Build 할 때 주의 사항
- Visual Studio Prompt 사용
- call c:\dev\ros2_foxy\setup.bat  먼저 실행
- workspace 경로로 가기 (ex. ros2_ws )
- colcon build


---


