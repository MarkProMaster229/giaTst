import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  
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
      console.log('server return:', data.message);
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

      </div>

    </>
  )
}

export default App
