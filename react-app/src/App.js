import { BrowserRouter, Switch } from 'react-router-dom';

import NavBar from './components/NavBar';


function App() {

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path="/" exact={true}>
          <h1>hi from the route</h1>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
