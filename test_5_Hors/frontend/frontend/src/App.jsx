import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  //пусть это будет компонент с массивом прикодит с фласка тут товары
  //состояние для отправить
  const [full_product, set_full_product] = useState([]);
  // состояние для получить 
  const [count, setCount] = useState(0);

  const get_priduct = () =>{
    fetch('http:localhost:5000/dataProduct',{
      method:'POST',
      headers:{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        product: full_product
      })
    }).then(respounse => respounse.json())
    .then(data => {
      get_full_product(data.product);//чел из бека обязуйся отправиить это
    })
  }
  return (
    <>
<div>
  <div className='nameLabel'>
    <h1>для администратора</h1>
  </div>
  <div className='labelTable'>
    
    {full_product.map((product, index) => (
      <div className='product-row' key={index}>
        <span>ID: {product.id}</span>
        <strong>Название: {product.name}</strong>
      </div>
    ))}

  </div>
</div>

    </>
  )
}

export default App
