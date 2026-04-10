// frontend/src/App.jsx
import React, { useEffect, useState } from 'react';
import './App.css';

function users()
{
const[nameUser, setName] = useState([])

}


function App() {
  const [forumMessade, usingMassade] = useState("");
  const [user, UserName] = useState("");
  const Message = () => {
    fetch('http://localhost:5000/message',{
      method: 'POST',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ messageJso: forumMessade, nameUsers:user})
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'NoNickname') {
      alert('никнейм не введён!');
      console.log('Сервер вернул:', data.message);
    }
  })
  }
const [forboardUser, setForboardUser] = useState([]);
const [forboardMessade, setForboardMessade] = useState([]);
const [forboardDatatime, setForboardDatatime] = useState([]);
  const RetBoard = () =>{
    fetch('http://localhost:5000/returnMessage',{
      method: 'GET',
      headers:{
        'Content-Type': 'application/json'
      },
    })
    .then(response => response.json())
    .then(data => {
    console.log('Полученные сообщения:', data);
    const nicknames = data.map(item => item.nickname);
    const messages = data.map(item => item.message);
    const datetimes = data.map(item => item.date);

    setForboardUser(nicknames);
    setForboardMessade(messages);
    setForboardDatatime(datetimes);
    

  })
}
  useEffect(() => {
    RetBoard();
  }, []);
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
    </div>

    <div class="textLabel">
        <h1>yourLabel</h1>
        <textarea value={forumMessade} onChange={(e) => usingMassade(e.target.value)}/>
        <p>
          <button onClick={Message}>
            отправить смс! 
          </button>
        </p>
    </div>

    <div className="person">
      <img src="\src\assets\frytigetAero.jpg" width="300" alt="I"/>
    </div>
    <div className="LabelForum">
      <h6>дата: никнейм:</h6>
      {forboardUser.length === 0 ? (
        <h3>Пока нет сообщений. Будь первым!</h3>
      ) : (
        forboardUser.map((nick, index) => (
        <h3 key={index}>
          {forboardDatatime[index]} | {nick}: {forboardMessade[index]}
          </h3>
          ))
          )}
</div>

    <footer class="MyFooter">
      <p>Everything what you watch this, belog you.</p>
      <p>"MIT license"</p>
    </footer>
</div>
  );
}

export default App;