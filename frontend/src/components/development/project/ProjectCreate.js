import {useState} from "react";
import {useUser} from "../UserProvider";
import axios from "axios";

function ProjectCreate() {
    const [projectName, setProjectName] = useState('');
    const {currentUser} = useUser();

    async function handleSubmit() {
        const postData = {
            head: currentUser.id,
            name: projectName
        };
        try {
            await axios.post('http://localhost:8000/api/development/project/create/', postData);
            setProjectName('');
        } catch (error) {
            console.log('pc', error)
        }
    }

    return (
            <>
                <input
                        type="text"
                        value={projectName}
                        onChange={(e) => setProjectName(e.target.value)}
                        placeholder="Введите название проекта"
                />
                <p>
                    <button onClick={handleSubmit}>
                        Создать проект
                    </button>
                </p>
            </>
    )

}

export default ProjectCreate;
