import {useEffect, useState} from "react";
import {useParams} from "react-router-dom";
import axios from "axios";

function TeamDetail() {
    const {id} = useParams();
    const [team, setTeam] = useState([]);

    useEffect(() => {
        async function fetchTeam() {
            try {
                const response = await axios.get(`http://localhost:8000/api/development/team/detail/${id}/`)
                setTeam(response.data)
            } catch (error) {
                console.error('ft', error)
            }
        }

        fetchTeam();
    }, [])
    return (
            <div>
                <h2>Команда: {team.name}</h2>
                Тимлид: {team.lead}
                {/*{team.members.map(member => (*/}
                {/*        <li key={member.id}>*/}
                {/*            {member.id}*/}
                {/*        </li>*/}
                {/*))}*/}
            </div>
    )
}

export default TeamDetail;