import React, {Component} from 'react';
import PropTypes from 'prop-types';

class Display extends Component {

    propTypes = {
        lista: PropTypes.string.isRequired,
        tiempo: PropTypes.number.isRequired
    };

    render() {
        const green = Math.random()%255;
        const red = Math.random()%255;
        const blue = Math.random()%255;
        const textColor = {
            backgroundColor: 'rgb(191, 10, 48)',
            padding: '15px',
            color: '#fffff0'
        };

        return <div style={textColor}>La cantidad de números primos encontrados es "{this.props.lista}" y demoró {this.props.tiempo} microsegundos.</div>
    }
}

export default Display;
