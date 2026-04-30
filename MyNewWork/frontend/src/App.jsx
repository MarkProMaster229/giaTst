import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [user, setUser] = useState([])
  const [event, setevent] = useState([])
  const [furcona, setfurcona] = useState([])
  const [fine, setfine] = useState([])


  const give_full_people = () => {
    fetch('http://localhost:5000/fullPeople',{
      method: 'GET',
      headers:{
        'Content-Type': 'application/json'
      },
    })
    //only post!
    .then(response => response.json())
    .then(data => {
    console.log("Данные от сервера:", data);
    console.log("Массив users:", data.users); 
    setUser(data.users);
    setevent(data.event);
    setfurcona(data.fursona);
    setfine(data.fine);
    })
  }


  //first route for get from server
  const RetBoard = () => {
    fetch('http://localhost:5000/mainLabel', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    })
      .then(response => response.json())
      .then(data => {
        //this data wich server, but i guess what need give data?

      })
  }




  return (
    <>
      <div>
        <header className='MyheaderForWeb'>
          <div className='ButtonAll'>
            <button onClick={give_full_people}>
              about people
            </button>
          </div>

        </header>
<div>
    <h3>Список пользователей:</h3>
    {user.map((oneUser, index) => (
        <p key={index}>{JSON.stringify(oneUser)}</p>
    ))}
</div>
      </div>

    </>
  )
}

export default App
