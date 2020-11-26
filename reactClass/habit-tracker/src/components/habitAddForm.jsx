// purecomponent or memo는 state나 props의 변화가 없다면 render를 불려지는걸 막아줌.
// 정확하게는 object내부의 값이 아닌 그 자체 형태의 변경이 없는 경우를 말한다.
import React, { memo } from 'react';
// memo는 purecomponent처럼 props의 변화가 없으면 불러 오지 않음
const habitAddForm = memo(props => {
    const formRef = React.createRef()
    const inputRef = React.createRef()
    const onSubmit = event => {
        event.preventDefault()
        const name = this.inputRef.current.value
        name && this.props.onAdd(name)
        //form 태그의 ref값이 있어야 reset()이 가능하다. 현재 위치를 알아야 사용하기때문.
        this.formRef.current.reset()
    }
    
    return (
        <>
            <form ref = {formRef} className="add-form" onSubmit={onSubmit}>
                <input ref={inputRef} type="text" className='add-input' placeholder='habit'/>
                <button className="add-button">Add</button>
            </form>
        </>
    );
})

export default habitAddForm;