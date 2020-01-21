import React, {Component} from 'react';
import './App.css';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import TextField from 'material-ui/TextField';
import RaisedButton from 'material-ui/RaisedButton';
import Paper from 'material-ui/Paper';
import Display from "./components/Display";

const style = {
    marginLeft: 12,
};

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            lista: '',
            tiempo: undefined
        };
    };

    obtenerLista() {
        fetch('http://34.95.243.180:80/criba', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({lista: this.textField.getValue()})
        })
            .then(response => response.json())
            .then(data => this.setState(data));
    }

    onEnterPress = e => {
        if (e.key === 'Enter') {
            this.obtenerLista();
        }
    };

    render() {
        const tiempoComponent = this.state.tiempo !== undefined ?
            <Display lista={this.state.lista} tiempo={this.state.tiempo}/> :
            null;

        return (
            <MuiThemeProvider>
                <div className="centerize">
                    <Paper zDepth={1} className="content">
                        <h2>Cálculo de la cantidad de números primos</h2>
                        <TextField ref={ref => this.textField = ref} onKeyUp={this.onEnterPress.bind(this)}
                                   hintText="Escriba un valor N."/>
                        <RaisedButton  label="Calcular" style={style} onClick={this.obtenerLista.bind(this)}/>
                        {tiempoComponent}
                    </Paper>
                </div>
            </MuiThemeProvider>
        );
    }
}

export default App;
