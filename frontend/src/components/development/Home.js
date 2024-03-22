import ProjectCreate from "./project/ProjectCreate";
import {Link} from "react-router-dom";
import TeamCreate from "./team/TeamCreate";

function Home() {
    return (
            <>
                <p>Проект</p>
                <ProjectCreate/>
                ---------------------------
                <p>
                    <Link to={`/development/project/list`}>
                        <button>
                            Все проекты
                        </button>
                    </Link>
                </p>
                ////////////////////////////////////////
                <p>Команда</p>
                <TeamCreate/>
                ---------------------------
                <p>
                    <Link to={`/development/team/list`}>
                        <button>
                            Все команды
                        </button>
                    </Link>
                </p>
            </>
    )
}

export default Home;