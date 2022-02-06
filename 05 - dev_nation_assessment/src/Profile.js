import React from 'react';

export default function Profile({students}) {
  return (    
    <>
    {students.map( (student) => {
      return (
        <div className="card" key={student.id}>
            <div className="img">
                <img src={student.pic} alt="" />
            </div>
            <div className="details">
                <h1 className='full_name'>{student.firstName + " " + student.lastName}</h1>
                <div className="other_details">
                    <p>Email: {student.email}</p>
                    <p>Company: {student.company}</p>
                    <p>Skill: {student.skill}</p>
                    <p>Average: {(student.grades.reduce( (pre, cur) => parseInt(pre) + parseInt(cur))/((student.grades.length)*100))*100}%</p>
                </div>
            </div>
        </div>
      )
    })}
    </>  
  )
}
