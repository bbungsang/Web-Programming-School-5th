## Field Options
#### null
###### Field.null
- True 면 장고는 데이터베이스에 NULL 값으로 공백을 저장할 것입니다. Default는 False 입니다.
- **CharField**, **TextField** 와 같은 문자열 기반 필드에서 null 의 사용을 지양하세요.
- 문자열 기반 필드가 null=True 를 가진다면, `no data`의 의미인 `NULL`과 `empty string`의 2개의 값을 가지게 됨을 의미합니다.
- `no data`의 2개의 값을 가지는 것은 불필요한 일이며, 장고는 관례로 `NULL`이 아닌 `empty string`을 사용합니다.
- 하나의 예외 사항으로, CharField가 **unique=True** 와 **blank=True** 를 둘 다 가진다면, 공백의 값과 여러 객체를 저장할 때, unique의 제약을 피하기 위해 **null=True** 가 요구되어집니다.
- 만약 BooleanField에 null 값을 받고 싶다면 **NullBooleanField** 를 사용하세요.
