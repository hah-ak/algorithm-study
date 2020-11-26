import React, { useState, useRef } from 'react';
import { useCallback } from 'react';


const SimpleHabit = (props) => { // 함수는 속에 들어있는 전체가 계속사용된다.
    const [count, setCount] = useState(0); // 실제 사용할 값과 set해줄 것
        // usestate는 reacthook의 모듈로, 업데이트가 일어나는 함수 임에도 변수를 계속 저장해둔다.
    
    const handleIncrement = useCallback(() => { // callback함수도 마찬가지
        setCount(count + 1);
    })

    const spanRef = useRef() // createref면 계속해서 생성을 하나, useRef로 메모리에 저장해서 계속 사용
    // react hook을 이용해 함수속 변수나, 콜백함수들을 중복해서 계속 불러오는 것을 막음.
    return (
        <li className="habit">
          <span ref={spanRef} className="habit-name">Reading</span>
          <span className="habit-count">{count}</span>
          <button
            className="habit-button habit-increase"
            onClick={handleIncrement}
          >
            <i className="fas fa-plus-square"></i>
          </button>
        </li>
      );
}
export default SimpleHabit;
