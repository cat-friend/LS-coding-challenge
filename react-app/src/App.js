import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Footer from './components/Footer';
import Info from './components/Info';


function App() {

  return (
    <>
      <div>
        <BrowserRouter>
          <Switch>
            <Route path="/" exact={true}>
              <Info />
            </Route>
          </Switch>
        </BrowserRouter>
      </div>
      <Footer />
    </>
  );
}

export default App;
