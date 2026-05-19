import { useState } from 'react'
import { useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function PhotoWall({ photos }) {
  if (!photos || photos.length === 0) return null;

  const cols = Math.floor(window.innerWidth / 200);
  const rows = Math.ceil((window.innerHeight * 2) / 200);
  const needed = cols * rows;

  let repeated = [];
  while (repeated.length < needed) {
    repeated = [...repeated, ...photos];
  }
  repeated = repeated.slice(0, needed);

  return (
    <div className="wall-container">
      <div className="wall-track">
        {repeated.map((item, index) => (
          <div key={index} className="wall-tile">
            <img src={item.file} className="wall-photo" alt="" />
            <div className="wall-caption">
              <span className="wall-username">{item.username || 'Аноним'}</span>
              {item.about && <span className="wall-about">{item.about}</span>}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function App() {
  const [count, setCount] = useState(0)
  const [userName, setUserName] = useState('')
  const [about, setAbout] = useState('')
  const [photos, setPhotos] = useState([])

  const [file, setFile] = useState(null);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  useEffect(()=>{
    fetch('http://localhost:5000/getMyImages',{
      method: 'GET',

    })
    .then(respounse => respounse.json())
    .then(data => {
      setPhotos(data);
    })
  }, [])
  

  const upload_to_the_server = () =>{
    const formData = new FormData();
    formData.append('user', userName);
    formData.append('about', about);
    if(file){
      formData.append('image', file);
    }
    fetch('http://localhost:5000/server', {
      method: 'POST',
      body: formData
    }).then(data => {
        setFile(null);
    })
  }
  return (
  <>
    <PhotoWall photos={photos} />

    <div className="overlay">
      <div className="form-card">
        <h1 className="title">Hello my guys</h1>
        <h2 className="subtitle">You can share your work with everyone!</h2>
        
        <label className="input-label">Your character name</label>
        <input 
          type="text" 
          value={userName} 
          onChange={(e) => setUserName(e.target.value)} 
          className="text-input"
          placeholder="Enter name..."
        />
        
        <label className="input-label">Character story</label>
        <input 
          type="text" 
          value={about} 
          onChange={(e) => setAbout(e.target.value)} 
          className="text-input"
          placeholder="Tell a story..."
        />
        
        <label className="file-label">
          {file ? `selected: ${file.name}` : 'Choose photo'}
          <input 
            type="file" 
            accept="image/*" 
            onChange={handleFileChange} 
            className="file-input"
            key={file ? 'has-file' : 'no-file'}
          />
        </label>
        
        
        <button onClick={upload_to_the_server} className="upload-btn">
          Booting up the fluff
        </button>
      </div>
    </div>
  </>
  )
}

export default App
