import React, {Component} from 'react';
import PropTypes from 'prop-types';

class Polarity extends Component {

    propTypes = {
        lista: PropTypes.string.isRequired,
        tiempo: PropTypes.number.isRequired
    };

    render() {
        const green = Math.round((this.props.tiempo));
        const red = 255 - green;
        const textColor = {
            backgroundColor: 'rgb(' + red + ', ' + green + ', 0)',
            padding: '15px'
        };

        return <div style={textColor}>La lista es "{this.props.lista}" y demoró {this.props.tiempo} </div>
    }
}

export default Polarity;
