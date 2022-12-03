import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import TweetData from "./datafile";
import Dropdown from "./dropdown";

function App(){
  return (
    <>
      <Router>
        <Routes>
          <Route  path="/" element={<Dropdown />} />
          <Route exact path="/datafile" element={<TweetData />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
