import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [string_name, setName] = useState('')
  const [password, setPassword] =useState('')
  const [regORautoriz, setRegORautoriz] = useState(false)//ну пусть регистрированый юзер - false, тот кому предстоит пройти регистрацию - true хз

  const registration_logic = () => {
    fetch('http://localhost:5000/dataRegORAutoriz',{
      method: 'POST',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
          login: string_name,
          password: password,
          regOrAutor: regORautoriz
        })
    }).then(respounse => respounse.json())
    .then(data => console.log(data))
  };


  return (
<div>
  <div className='registration'>
    <div className='name'>
      <input name='string_name' value={string_name} onChange={(e) => setName(e.target.value)}/>введите имя
      <input name='password' value={password} onChange={(e) => setPassword(e.target.value)}/>введите пароль
      <input type="radio" name = "or" checked={regORautoriz === false} onChange={() => setRegORautoriz(false)} /> авторизироваться
      <input type="radio" name = "or" checked={regORautoriz === true} onChange={() => setRegORautoriz(true)}/>регистрироваться
      <button className='submit' onClick={registration_logic}> выполнить </button>
    </div>

  </div>


</div>
  )
}

export default App
