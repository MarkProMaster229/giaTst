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
    return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>🐾 My Furry Social Network</h1>
      <p>{message}</p>
      <div>
      <button onClick={handleClick}>
        Отправить запрос /Mydildo/pay
      </button>
    </div>
    <button onClick={data}>
      кинуть
    </button>
      
      <div>
        <h2>Пользователи (заглушка)</h2>
        <ul>
          {users.map(user => (
            <li key={user.id}>
              {user.name} (@{user.login})
            </li>
          ))}
        </ul>

      </div>
      
      <button onClick={() => alert('Flask пока не подключён!')}>
        Нажми меня
      </button>
    </div>
  );
}

export default App;