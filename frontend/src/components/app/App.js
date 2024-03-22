import './App.css';
import {UserProvider} from "../development/UserProvider";
import ProjectList from "../development/project/ProjectList";
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Home from "../development/Home";
import TeamList from "../development/team/TeamList";
import TeamDetail from "../development/team/TeamDetail";
import TeamCreate from "../development/team/TeamCreate";

function App() {
    return (
            <UserProvider>
                <Router>
                    <Routes>
                        <Route path="/" element={<Home/>}/>
                        <Route path="/development/project/list" element={<ProjectList/>}/>
                        <Route path="/development/team/list" element={<TeamList/>}/>
                        <Route path="/development/team/detail/:id" element={<TeamDetail/>}/>
                        <Route path="/development/team/create/" element={<TeamCreate/>}/>
                    </Routes>
                </Router>
            </UserProvider>

    );
}

export default App;
