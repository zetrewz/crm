import {useEffect, useState} from "react";
import axios from "axios";

function ProjectList() {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        async function fetchFolders() {
            try {
                const response = await axios.get('http://localhost:8000/api/development/project/list/');
                setProjects(response.data)
            } catch (error) {
                console.error('pl', error)
            }
        }

        fetchFolders();
    }, [])

    return (
            <div>
                <h2>Список проектов:</h2>
                <ul>
                    {projects.map(project => (
                            <li key={project.id}>
                                {project.name}
                            </li>
                    ))}
                </ul>
            </div>
    )
}

export default ProjectList;