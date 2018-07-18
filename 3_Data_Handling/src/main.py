from src import numpy_lec as nl

"""
 Created by IntelliJ IDEA.
 Project: 3_Data_Handling
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-14
 Time: 오전 2:07
"""

"""

< Numpy >
- Numerical Python
- 파이썬의 고성능 과학 계산용 패키지
- Matrix 와 Vector 같은 Array 연산의 사실상의 표준
////
- 일반 list 에 비해 빠르고, 메모리 효율적
- for 문, list comprehension 등의 반복문 없이 데이터 배열에 대한 처리를 지원
- 선형대수와 관련된 다양한 기능을 제공
- 내부가 C 로 되어있기 때문에, 특히 array 연산에서 매우 빠르다.
- C, C++, 포트란 등의 언어와 통합 가능

"""

"""

[ numpy_lec.py ]


== (1) :: ndarray ==

- numpy 는 np.array 함수를 활용하여 배열을 생성함 -> ndarray
- numpy 는 하나의 데이터 타입만 넣을 수 있음 (Dynamic typing not supposed)
- (초기에 타입을 미리 설정하면, 반드시 해당 타입으로만 핸들링 가능하다.)
- C 의 Array 를 사용하여 배열을 생성하기에 매우 빠르다.
( ndarray > list comprehension > for loop 순으로 빠르다. )
- 하지만 concat 과 같이 할당을 하는 경우는 list 보다 느리다. (연속된 메모리를 찾아야 하기 때문)

< 1. reshape >
- Array 의 shape 를 변경함. (갯수는 동일)

< 2. flatten >
- 다차원의 array 를 1차원 array 로 변환

< 3. indexing >
- list 와 달리 2차원 배열에서 [0, 0] 과 같은 표기법을 제공함
- 2차원 Matrix 의 경우, 앞은 row, 뒤는 col 을 의미함

< 4. slicing >
- list 와 달리 row 와 col 부분을 나눠서 slicing 이 가능함
- Matrix 의 부분 집합을 추출할 때 유용함
- 보통 x : y 로 나타낸다. (시작과 끝 부분)
- 하지만 x : y : z 로 나타낼 수 있는데, x 는 row, y 는 col, z 는 'step' 이다.
- (즉, z 에 조건을 넣어서 step 간격으로 추출할 수 있다.)

< 5. arange >
- array 의 범위를 지정하여, 값의 list 를 생성
- 보통 np.arange(30) 과 같이 쓰지만, np,arange(0, 30, 2) 와 같이 (시작, 끝 step) 으로 생성할 수 있다.

< 6. zeros, ones, empty >
- zeros : 0 으로 가득 찬 ndarray 생성
- ones : 1 로 가득 찬 ndarray 생성
- empty : shape 만 주어지고, 비어있는 ndarray 생성
(memory initialization 이 되지 않음)

< 7. something_like >
- 기존 ndarray 의 shape 크기만큼 1, 0, 또는 empty array 를 반환

< 8. identity >
- 단위 행렬(i 행렬) 을 생성함 (n 은 row 의 갯수이다)

< 9. eye >
- 대각선의 value 가 1 인 행렬을 생성함 (k 인자의 값을 통해 시작 index 의 변경이 가능하다.)

< 10. diag >
- 대각 행렬의 값을 추출함 (k 인자의 값을 통해 시작 index 의 변경이 가능하다.)

< 11. random sampling >
- 데이터 분포에 따른 sampling 으로 array 생성
(lower boundary, upper boundary, sample size) 로 생성
m = np.random.uniform(0, 1, 10).reshape(2, 5) // Uniform Distribution
m = np.random.normal(0, 1, 10).reshape(2, 5) // Normal Distribution


== (2) :: Operation Functions ==

- numpy 는 많은 계산식을 지원한다.
- 특히, 축을 알 수 있게 해주는 "axis" 가 아주 중요하다.
(축이 늘어날 수록, 기존에 있던 축들은 한 칸씩 뒤로 밀려난다.
즉, 새로 생기는 축이 항상 0 이 된다.)

- 다양한 수학 연산자를 제공함 ...
exponential : exp, log, power, sqrt, ...
trigonometric : sin, cos, tan, arcsin, arccos, atctan, ...
hyperbolic : sinh, cosh, tanh, arcsinh, arccosh, arctang, ...

< 1. axis >
- 모든 operation function 을 수행할 때 기준이 되는 dimension 축
- (2, 3, 4) 라는 shape 가 있을 때, (2: axis=0, 3: axis=1, 4: axis=2)

< 2. sum >
- ndarray 의 element 들 간의 합을 구함
- list 의 sum 과 동일

< 3. mean & std >
- ndarray 의 element 들 간의 평균(mean) 또는 표준 편자(standard deviation) 를 구할 수 있음

< 4. concatenate >
- concatenate 를 통해 원하는 axis 를 기준으로 두 ndarray 를 결합할 수 있다.
- np.concatenate((*matrix), axis=k) 에서 axis 를 통해 concat 을 시행할 축을 결정할 수 있다.
- 하지만 numpy 에서 concat 은 느린 편이다 !
(만약, 큰 데이터가 주어진 상황이라면, numpy 의 concatenate 를 사용하는 것은 비효율적이다. -> list 가 더 효율적이다.)


== (3) :: Array Operations ==

- numpy 는 array 간의 기본적인 사칙 연산을 지원함
- shape 가 서로 다른 배열 간 연산을 지원하는 기능인 broadcasting 이 중요

< 1. basic operations >
- matrix 의 shape 가 같다면, 기본적인 사칙 연산을 지원함

< 2. dot product >
- Matrix 의 기본 product 연산 (행렬의 곱)
m = np.dot(matrix_a, matrix_b)

< 3. transpose >
- Matrix 의 전치 행렬 (transpose)
m = np.transpose(matrix)

< 4. broadcasting >
- shape 이 서로 다른 배열 간의 연산을 지원함
- Scalar - Vector 외에도, Vector - Matrix 간의 연산도 지원


== (4) :: Comparisons ==

< 1. all & any >
- ndarray 의 데이터 전부(and) 또는 일부(or) 가 조건에 만족하는지의 여부 반환

< 2. where >
- 조건에 만족하는 index 값을 추출한다
np.where(condition, True, False)

np.where(m > 10, 7, 8)  // 10 보다 큰 index 에선 7, 작은 index 에선 8 추출
np.where(m > 10)  // 10 보다 큰 element 가 존재하는 index 반환

< 3. argmax & argmin >
- array 내 최대값 또는 최소값의 index 를 반환 (axis 를 기준으로 반환한다.)
m = np.argmax(m, axis=1)
m = np.argmin(m, axis=0)


== (5) :: Boolean & Fancy Index ==

< 1. boolean index >
- numpy 는 특정 배열에서 특수한 조건에서의 추출한 값을 다시 배열 형태로 추출할 수 있음
- Comparison Operation 함수들도 모두 사용 가능
m2 = m[m > 3]  // 조건이 True (m > 3) 인 index 의 element 만을 추출

< 2. fancy index (take) >
- numpy 는 배열 index 의 value 를 이용하여 값을 추출할 수 있음
- 이 때, index 로 사용될 배열은 반드시 integer 로 선언되어야 한다.
- Matrix 형태의 데이터에도 사용 가능하다.
m = np.array([2, 4, 6, 8], dtype=np.float64)
arr = np.array([0, 0, 1, 3, 2, 1], dtype=int)
print(np.take(m, arr))
print(m[arr])
> [2, 2, 4, 8, 6, 4]

"""

"""

< Pandas >
- 구조화된 데이터의 처리를 지원하는 Python 라이브러리 (Python 계의 엑셀)
- Numpy 와 통합하여, 강력한 "스프레드시트" 처리 기능을 제공
- 인덱싱, 연산용 함수, 전처리 함수 등을 제공함
- numpy 의 wrapper 이다.

"""

"""

[ pandas_lec_1.ipynb ]

== (1) :: Series ==

- Column Vector 를 표현하는 object
- numpy.ndarray 의 서브 클래스이다.
- index 타입을 핸들링 할 수 있다.
- example_obj = pd.Series(data)
- data 에는 list, dict 값 모두 들어갈 수 있다.
(만약 dict 를 넣을 땐, 앞에는 index 값, 뒤에는 value 값이 삽입된다.)


== (2) :: Dataframe ==

- Data table 전체를 포함하는 Object
- numpy 의 서브클래스이기 때문에 numpy 의 함수들을 사용 할 수 있다.
- numpy 의 array 와 유사하다.
- 각각의 col 은 서로 다른 type 을 가진다.
- Matrix 로 가정을 하며, 따라서 당연히 row 와 col 의 값이 존재하고 접근할 수 있다.
- Size mutable 로 변경 가능하다. (insert 및 delete 로 size 가 유동적으로 변한다.)

- loc 을 통해 해당 위치의 데이터를 추출할 수 있고, (index 의 위치를 실제 value 값을 기준으로 절대적으로 잡는다.)
- iloc 을 통해 해당 index 의 데이터를 추출할 수 있다. (index 의 위치를 '처음' 을 기준으로 상대적으로 잡는다.)


== (3) :: Selection & Drop ==

- Selection : data 를 가져옴
- Drop  : data 를 없앰
(pandas 는 쉽게 data 를 못 지운다. 반드시 drop(~, inplace=True) 를 붙여줘야 한다 !)

>> Selection
- head(n) 으로 n 개의 데이터를 추출할 수 있다.
- 하나의 col 을 추출할 경우는 series 객체를 추출하게 된다.
- 여러개의 col 을 추출할 경우는 data frame 객체를 추출하게 된다.

>> Drop
- index 번호로 drop 가능
- drop 이 반영되게 하려면 drop(inplace=True) 옵션을 붙일 것 !
- 한 개 이상의 data 를 drop 하고 싶을 땐 list 로 묶는다.
- 원하는 col 을 지울 수 있다. (반드시 axis 를 넣어줘야 하며, 2차원일 경우 axis=1 이다.)


== (4) :: Dataframe Operations ==
- Operation type : add, sub, div, mul

>> Series Operation
- index 기준으로 연산 수행
- 겹치는 index 가 없을 경우 NaN 값으로 반환

>> Dataframe Operation
- col 과 index 를 모두 고려하여 연산 수행
- fill_value=k 의 인자를 넣어줌으로써 NaN 일 경우의 값 설정 가능

- sereis + dataframe 일 경우 col 을 기준으로 broadcasting 이 발생함
- axis 를 인자로 넣으면, axis 를 기준으로 broadcasting 이 발생한다.


== (5) :: Lambda, Map, Apply ==
- pandas 에서 굉장히 실용적임

>> Map for series
- pandas 의 series 타입의 data 에도 map 함수 사용 가능
- function 대신 dict, sequence 자료형 등으로 대체 가능
- dict 타입을 이용하여 map 을 사용하면, 해당 index 의 값을 바꿔준다. (유용하게 데이터 변환 가능)
- size 가 같다면, 같은 위치의 값들끼리 연산한다.


>> Apply for dataframe
- map 과 달리, series 전체 col 에 해당 함수를 적용시킨다.
- series data 로 입력받아 handling 가능하다.
- 내장 연산 함수를 사용할 때도 똑같은 효과를 거둘 수 있다.
- mean, std 등 사용 가능하다.
- scalar 값 이외에 series 값도 반환 가능하다.

>> Applymap for dataframe
- series 단위가 아닌, 전체 element 단위로 함수를 적용시킨다.
(기본 map 은 series 데이터의 element 하나하나에 적용한다.)
- series 단위에 apply 를 적용시킬 때와 같은 효과


== (6) :: Pandas Built-in Functions ==
- describe : numeric type 데이터의 요약 정보를 보여줌.
- unique : series data 의 유일한 값을 list 로 반환함.
(category 형 데이터가 몇 개 인지 모를 경우 유용하다.)
- sum : 기본적인 col 또는 row 값의 합 연산.
(axis 를 기준으로 값을 추출할 수 있다.)
- isnull : col 또는 row 값의 NaN (null) 값의 index 를 반환한다.
- sort_values : col 값을 기준으로 data 를 sorting.
(ascending 인자를 통해 오름차순, 내림차순 구분 가능하다.)
- corr, cov, corrwith : 상관계수와 공분산을 구하는 함수.

"""


def main():
    print("\n#############################[ 1. numpy_lec.py ]#############################")
    nl.numpy_lec()


if __name__ == "__main__":
    main()
