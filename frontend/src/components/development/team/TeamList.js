import {useEffect, useState} from "react";
import axios from "axios";
import {Link} from "react-router-dom";

function TeamList() {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        async function fetchTeams() {
            try {
                const response = await axios.get('http://localhost:8000/api/development/team/list/')
                setTeams(response.data)
            } catch (error) {
                console.error('tl', error)
            }
        }
        fetchTeams();
    }, [])
    return (
            <div>
                <h2>Список команд:</h2>
                <ul>
                    {teams.map(team => (
                            <Link to={`/development/team/detail/${team.id}`} key={team.id}>
                                <p>{team.name}</p>
                            </Link>
                    ))}
                </ul>
            </div>
    )
}

export default TeamList;