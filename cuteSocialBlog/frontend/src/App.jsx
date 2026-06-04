import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [string_name, setName] = useState('')
  const [password, setPassword] = useState('')
  const [regORautoriz, setRegORautoriz] = useState(false)//ну пусть регистрированый юзер - false, тот кому предстоит пройти регистрацию - true хз
  //я запутался в ебучий false true
  const [correctDataToBackend, setCorrectDataToBackend] = useState(true)
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
    }).then(response => response.json())
    //договоримся со мной - должен придти с бека че то типо doneRegOrAutoreg = true или false 
    //если юзер своими лапками натыкал не туда например отправил запрос как регстрацию надо это обработать
    //можно в состоянии фиксировать что было возвращено
    .then(data => {
      setCorrectDataToBackend(data.doneRegOrAutoreg);
      //я тут подумал если успешно прошла авторизация я верну сюда че то 
      
    })
  };


  return (
<div>
  <div className='registration'>
    <div className='name'>
      <input name='string_name' value={string_name} onChange={(e) => setName(e.target.value)}/>введите имя
      <input name='password' value={password} onChange={(e) => setPassword(e.target.value)}/>введите пароль
      <input type="radio" name = "or" checked={regORautoriz === true} onChange={() => setRegORautoriz(true)} /> авторизироваться
      <input type="radio" name = "or" checked={regORautoriz === false} onChange={() => setRegORautoriz(false)}/>регистрироваться
      <button className='submit' onClick={registration_logic}> выполнить </button>
      <label className='testLabel'>
  {correctDataToBackend === true ? "Успешно залогинился!" : "Что-то пошло не так..."}
</label>

    </div>

  </div>


</div>
  )
}

export default App
