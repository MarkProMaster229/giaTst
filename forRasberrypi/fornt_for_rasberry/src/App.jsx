import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function PhotoWall({ photos }) {
  if (!photos || photos.length === 0) {
    return null;
  }
}

function App() {
  const [count, setCount] = useState(0)
  const [userName, setUserName] = useState('')
  const [about, setAbout] = useState('')
  const [photos, setPhotos] = useState([])

  const [file, setFile] = useState(null);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  

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
          Choose photo
          <input 
            type="file" 
            accept="image/*" 
            onChange={handleFileChange} 
            className="file-input" 
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
