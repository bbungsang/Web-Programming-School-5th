## 가운데 정렬
#### 가로 가운데 정렬
- **부모** 의 가운데로 정렬

```css
#parent {

}

#child {
  width: 500px;
  margin: 0 auto;
}
```

#### 부모의 가로/세로 가운데 정렬
1. 부모 요소의 `height`와 `line-height`의 값이 같을 경우, 내부의 요소들은 세로 가운데로 정렬

```css
#parent {
  height: 60px;
  line-height: 60px;
}

#child {
  width: 500px;
  margin: 0 auto;
}
```

2. 자식 요소를 `absolute` 포지션으로 설정하고, 상단과 왼쪽어서 각각 부모의 50%만큼 이동한 뒤, 자시느이 높이와 가로의 -50%만큼을 다시 위와 왼쪽으로 이동
(단, transform을 사용할 경우, 픽셀이 깨져보일 수 있음)

```css
#parent {

}

#child {
  position: absolute;
  width: 200px;
  height: 100px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```


## Atom Sass Pakage Install & Settings
- `sass autocompile`를 검색하고 설치한다.
- `settings` 에서 `compressed`, `compact`, `nested`, `expanded` 체크 후, 관리가 편하도록 `../css/`와 같이 저장 경로를 변경한다.
