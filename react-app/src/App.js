import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Info from './components/Info';


function App() {

  return (
    <BrowserRouter>
      <Switch>
        <Route path="/" exact={true}>
          <Info />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
