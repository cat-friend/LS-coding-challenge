import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import App from './App';
import configureStore from './store';
import * as loanFunctions from './store/api_library'

const store = configureStore();

window.fetchAllLoans = loanFunctions.fetchAllLoans;
window.fetchOneLoan = loanFunctions.fetchOneLoan;
window.editLoan = loanFunctions.editLoan;
window.postLoan = loanFunctions.postLoan;

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
        <App />
      </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);
