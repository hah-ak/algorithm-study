import React from 'react';
import ReactDOM from 'react-dom'; // babel을 이용해 브라우저가 읽지 못하는걸 자바스크립트로변화
// 이렇게 만들어진걸 html과 연결해주는게 react-dom
import './index.css';
import App from './app';
import * as serviceWorker from './serviceWorker';
import '@fortawesome/fontawesome-free/js/all.js';
import SimpleHabit from './components/simpleHabit';

ReactDOM.render(
  // <React.StrictMode> 에러를 콘솔에 띄어줌, 배포시에 활성화가 되지 않음.
    <App />,
  // </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
