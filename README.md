# 몰?루랭

**몰?루랭**은 [엄랭 개발자님의 바람](https://www.youtube.com/watch?v=G0psQ54f5zE&lc=Ugzm8Rp4pIHcmrjPqVF4AaABAg.9XqbgJQ_IxR9XxEjAMdCGI)에서 착안하여 **몰?루** 밈을 바탕으로 만들어진 프로그래밍 언어입니다.

# 문?법

## 스택

**몰?루랭**에서 모든 변수는 스택에 저장되며, 명령을 사용할 때 변수의 위치는 스택의 맨 위인 1에서부터 세서 쓰게 됩니다.

위치가 1인 경우 생략할 때도 있습니다.

<br/>

## 몰루

`몰`과 `루`는 **몰?루랭**에서 가장 중요한 두 단어입니다.

모든 명령은 `몰`로 시작해서 `루`로 끝납니다.

따라서 `루`와 다음 `몰` 사이의 말은 모두 주석입니다.

`몰` 바로 다음에 나오는 기호에 따라 명령이 정해지고, 그 뒤에 나오는 `.`의 개수가 명령의 인자가 됩니다.

<br/>

## 몰?루

`몰?루`는 스택에 수를 추가하는 명령입니다.

- `몰?루`는 0을 추가합니다.

- `몰?...루`와 같이 쓰면 스택의 맨 위에 3을 추가합니다.

- `몰?... . ..루`와 같이 쓰면 차례로 3, 1, 2를 추가합니다. 맨 위에는 2가 옵니다.

<br/>

## 몰!루

`몰!루`는 스택의 수를 출력하고 스택에서 제거하는 명령입니다.

- `몰!루`는 맨 위의 수를 출력합니다.

- `몰!..루`와 같이 쓰면 위에서 두 번째에 있는 수를 출력할 수 있습니다.

<br/>

## 몰.루와 몰,루

`몰.루`는 스택의 수를 복제하는 명령입니다.

- `몰.루`는 맨 위의 수를 복제합니다.

- `몰....루` 또는 `몰. ...루`와 같이 쓰면 위에서 세 번째에 있는 수를 복제해 스택의 맨 위에 추가합니다.

<br/>

`몰,루`는 스택의 수를 옮기는 명령입니다.

- `몰,루`는 위에서 두 번째에 있는 수를 맨 위로 옮깁니다.

- `몰,....루`와 같이 쓰면 위에서 네 번째에 있는 수를 맨 위로 옮깁니다.

- `몰,.. ...루`와 같이 쓰면 위에서 두 번째에 있는 수와 세 번째에 있는 수를 서로 바꿉니다.

<br/>

## 몰;루

`몰;루`는 스택의 수를 제거하는 명령입니다.

- `몰;루`는 맨 위의 수를 제거합니다.

- `몰;..루`와 같이 쓰면 위에서 두 번째에 있는 수를 제거합니다.

<br/>

## 몰+루, 몰-루, 몰\*루 그리고 몰/루

`몰+루`는 스택의 수를 더하는 명령입니다.

- `몰+루`는 맨 위의 수와 두 번째 수를 더합니다.

- `몰+..루`와 같이 쓰면 맨 위의 수에 2를 더합니다.

사용된 하나 또는 두 개의 수는 스택에서 제거됩니다.

나머지 사칙연산도 모두 같은 규칙으로 빼고, 곱하고, 나눕니다.

<br/>

나누기의 순서는 아래와 같습니다.

- `몰/루`는 맨 위의 수**를** 두 번째 수**로** 나눕니다.

- `몰/...루`와 같이 쓰면 맨 위의 수를 3으로 나눕니다.

<br/>

## 몰{}루와 몰~루

`몰{}루`는 스택에 명령 덩어리를 추가하는 명령입니다.

`몰~루`는 스택의 명령 덩어리를 실행합니다.

```
몰{
  몰?루
  몰.루
  몰+.루
  몰!루
}루
몰~루
```

위 코드는 스택에 다음과 같은 일련의 명령 덩어리를 추가합니다.

- 스택에 0을 추가한다
- 스택 맨 위의 수를 복제한다
- 스택 맨 위의 수에 1을 더한다
- 스택 맨 위의 수를 출력한다

실행한다면 그 결과로 1이 출력되고 스택에 0이 추가될 것입니다.

```
몰{}루
몰?루
몰~루
```

만약 위처럼 수를 실행한다면 오류가 발생합니다.

```
몰{}루
몰*...루
```

위처럼 명령 덩어리를 연산할 때도 오류가 발생합니다.

대신 `몰~...루`를 통해 명령 덩어리의 반복 횟수를 지정할 수 있습니다.