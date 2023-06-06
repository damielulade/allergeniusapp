import React from 'react';
import './App.css';
// import './static/css/style.css'
import Main from './components/Main';
import SidebarLeft from './components/SidebarLeft';
import SidebarRight from './components/SidebarRight';

export default function App() {
  return (
    <div>
      <SidebarLeft />
      <Main />
      <SidebarRight />
    </div>
  )
}