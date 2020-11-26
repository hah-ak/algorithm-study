import './App.css';
import React, { Component, StrictMode } from 'react';
import Test from './components/test';

class App extends Component {
    render() {
        return (
            <StrictMode>
                <Test />
            </StrictMode>
        )
    }
}
export default App;
