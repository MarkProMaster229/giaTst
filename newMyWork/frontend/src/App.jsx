// frontend/src/App.jsx
import React, { useState } from 'react';
import './App.css';

function users()
{
const[nameUser, setName] = useState([])

}


function App() {
  const [message, setMessage] = useState('React работает!');
  const [users, setUsers] = useState([
    { id: 1, name: 'Алексей', login: 'alex' },
    { id: 2, name: 'Лиза', login: 'lisa' }
  ]);


  const handleClick = () => {
    fetch('http://localhost:5000/Mydildo/pay')
      .then(response => response.json())
      .then(data => {
        console.log('Ответ от сервера:', data)
        alert('Проверь консоль (F12)!')
      })
    }
    const data = () =>{
      const dataTest = {      
        name: "Алексей",
        age: 25
    };
    fetch('http://localhost:5000/spermoglot3000',{
      method: 'POST',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(dataTest)
    })
  }
  const [user, UserName] = useState("");
  const Name = () => {
    fetch('http://localhost:5000/NickName', {
      method: 'POST', 
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ nickname: user })
    })
    .then(response => response.json())
  }
    return (
<div>
      <header className='MyHeader'>
        <h1>MyForum</h1>
        <div className='MyButtonInHeader'>
          <button type="submit"> aboutMe </button>
          <button type="submit"> youKnowWhatThis. </button>
        </div>
      </header>
      
    <div className='usingNickName'>
        <h4>привет! тут не нужно регистрирвоаться!</h4>
        <h4>ты можешь взять себе любое имя и использовать его что бы писать на этом форуме</h4>
        <input type="text" value={user} onChange={(e) => UserName(e.target.value)} name = "name"/>
        <button type="submit"> установить ник! </button>
        <button onClick={Name}>
          загрузит
          </button>
    </div>

    <div class="textLabel">
        <h1>yourLabel</h1>
        <textarea name="yourText" rows="5" cols="40">Введите ваш текст здесь...</textarea>
        <p>
          <button type="submit"> отправить сообщение </button>
        </p>
    </div>

    <div className="person">
      <img src="\src\assets\frytigetAero.jpg" width="300" alt="I"/>
    </div>
    <div class="LabelForum">
        <h6>дата: никнейм: </h6>
        <h3>тут появятся новый сообщения всех кто писал на форуме!</h3>
    </div>

    <footer class="MyFooter">
      <p>Everything what you watch this, belog you.</p>
      <p>"MIT license"</p>
    </footer>
</div>
  );
}

export default App;