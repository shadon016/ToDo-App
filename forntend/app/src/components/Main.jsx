import React, { useState } from 'react'


const Main = () => {
    const [task, setTask] = useState([]);
    const [addTask, setaddTask] = useState('');

    const newAddedTask = (td) => {
        task.push(td);
        setTask([...task]);
        console.log(task)
    }
    return (
        <div>
            <div>
                <input type="text" value={addTask} placeholder='Add todo...' onChange={(e) => setaddTask(e.target.value)} />
                <input type="button" value='add' onClick={() => newAddedTask(addTask)} />
            </div>
            <div>
                <h3>Task List</h3>
                {task.map((taskData) => (
                    <div>
                        <p>{taskData}</p>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Main;