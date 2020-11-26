import React, { Component } from 'react';
import Habit from './habit';
import HabitAddForm from './habitAddForm';

class Habits extends Component {
    render() {
        console.log('habits')
        return (
            <>
                <HabitAddForm onAdd={this.props.onAdd} />
                <ul>
                    {
                        this.props.habits.map(habit =>
                            <Habit
                                key={habit.id}
                                habit={habit}
                                onIncrement={this.props.onIncrement}
                                onDecrement={this.props.onDecrement}
                                onDelete={this.props.onDelete}
                            />)
                                //넘겨줄값을 태그속 어트리뷰트로 지정해 넘겨 줌
                    }
                </ul>
                <button className="habit-reset" onClick={this.props.onReset}>reset All</button>
            </>
        );
    }
}

export default Habits;