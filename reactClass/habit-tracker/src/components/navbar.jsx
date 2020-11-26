import React, { PureComponent } from 'react';
import './style.css';

class Navbar extends PureComponent {

    render() {
        return (
            <div>
                <i className='navbar-logo fas fa-leaf'></i>
                <span>habit Tracker</span>
                <span className='navbar-count'>{this.props.totalCount}</span>
                <div id="check-menu">
                    <input id="toggle" type="checkbox"/><label for="toggle">&equiv;</label>
                    <div className="slide-menu">
                        <nav id="category">
                        </nav>
                    </div>
                </div>
            </div>
        );
    }
}

export default Navbar;