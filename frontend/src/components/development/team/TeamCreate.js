import {useState} from "react";
import {useUser} from "../UserProvider";
import axios from "axios";

function TeamCreate() {
    const [teamName, setTeamName] = useState('');
    const {currentUser} = useUser();

    async function handleSubmit() {
        const postData = {
            lead: currentUser.id,
            name: teamName
        }
        try {
            await axios.post('http://localhost:8000/api/development/team/create/', postData);
            setTeamName('');
        } catch (error) {
            console.error('tc', error);
        }
    }

    return (
            <>
                <input
                        type="text"
                        value={teamName}
                        onChange={(e) => setTeamName(e.target.value)}
                        placeholder="Введите название команды"
                />
                <p>
                    <button onClick={handleSubmit}>
                        Создать команду
                    </button>
                </p>
            </>
    )
}

export default TeamCreate;