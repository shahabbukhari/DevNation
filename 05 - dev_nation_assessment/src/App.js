import React,{useState, useEffect} from 'react';
import './App.css';
import Profile from "./Profile";

function App() {
  const [stu, setStu] = useState([])
  const [que, setQue] = useState("")  

  async function getUser(url) {
    const stuData = await fetch(url)
    const gotData = await stuData.json() 
    setStu(gotData.students)
  }

  function find(students) {
    return (students.filter( (student) => ((student.lastName.concat(student.firstName)).toLowerCase()).includes(que) ))
  }


  useEffect( () => {
    getUser("https://api.hatchways.io/assessment/students")
  }, [])


  return (
    <>
    <input type="text" className='user_input' placeholder='Search by names' onChange={ (e) => setQue((e.target.value).toLowerCase()) }/>
    <Profile students={find(stu)}/>
    </>
  );
}

export default App;