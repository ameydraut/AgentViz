import Dashboard from "./pages/Dashboard"
import {BrowserRouter , Routes, Route} from "react-router-dom"
import SessionDetails from "./pages/SessionDetails";

function App(){
  return(
    <BrowserRouter>

    <Routes>

      <Route
      path = "/"
      element = {<Dashboard />} />

      <Route
      path = "/session/:session_id"
      element = {<SessionDetails /> }/>

  </Routes>

  </BrowserRouter>
  );
}

export default App;