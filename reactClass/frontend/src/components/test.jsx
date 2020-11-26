import React, { Component } from 'react';
import axios from 'axios'

class Test extends Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
        
            // const res = await fetch('http://127.0.0.1:8000/api/');
            const res = axios.get('/api/')
            const posts = (await res).data;
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div>
                {this.state.posts.map(item => (
                    <div key={item.id}>
                        <h1>{item.title}</h1>
                        <span>{item.content}</span>
                    </div>
                ))}
            </div>
        );
        
    }
}

export default Test;