import React from 'react';
import { Component } from 'react';
import './app.css';
import Habits from './components/habits';
import Navbar from './components/navbar';

class App extends Component {
  state = {
    habits: [
        {id: 1, name:'Reading', count : 0},
        {id: 2, name:'Running', count : 0},
        {id: 3, name:'Coding', count : 0}
      ]
    }
  // callback함수들 ( 어떤 이벤트에 의해서 실행되거나, 다른 함수의 인자로써 이용되는 함수)
  // arrowfunction들이 콜백함수가 된다
  handleIncrement = habit => {
    const habits = this.state.habits.map(item =>{
      if(item.id === habit.id) {
        return {...habit, count:habit.count + 1}
      }
      return item
    })
    this.setState({habits}) //habits: habits와 동일
  }

  handleDecrement = habit => {
    const habits = this.state.habits.map(item =>{
      if(item.id === habit.id) {
        const count = habit.count - 1
        return {...habit, count: count < 0 ? 0 : count}
      }
      return item
    })
    this.setState({habits})
  }

  handleDelete = habit => {
      const habits = this.state.habits.filter(item => item.id !== habit.id)
      //filter를 통해 현재 id와 다른 것만 골라내서 habits에 복사함
      this.setState({habits})
  }

  handleAdd = name => {
    const habits = [...this.state.habits, {id: Date.now(), name: name, count: 0}]
    this.setState({habits: habits})
  }

  handleReset = () => {
    const habits = this.state.habits.map(habit => {
      if (habit.count !== 0) {
        const count = 0
        return {...habit, count}
      }
      return habit
    })
    this.setState({habits})
  }
  render() {
    return (
      <>
        <Navbar totalCount={this.state.habits.filter(item => item.count > 0).length} />
        <Habits 
        habits={this.state.habits}
        onIncrement={this.handleIncrement}
        onDecrement={this.handleDecrement}
        onDelete={this.handleDelete}
        onAdd={this.handleAdd}
        onReset={this.handleReset}
        />
      </>
    )
  }
}

// function App() {
//   // const name = 'kyc'
//   return (
//     // <React.Fragment>
//     <>
//       {/* <h1>hello {name}</h1>
//       <h1>hello 2 {name}</h1>
//       {name && <h1>hello </h1>} */}
//       <Habits />
//     </>
//     // </React.Fragment>
//   );
// }

export default App;
