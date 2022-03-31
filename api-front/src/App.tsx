import { useEffect, useState } from 'react';
import { Notifications } from './Components/Notifications/Notifications';
import { Login } from './Components/Login/Login';

function App() {
  const [isLog, setIsLog] = useState(false);

  return (
    <div>
      <header>
        { !isLog ? <Login setIsLog={setIsLog}/> : <Notifications setIsLog={setIsLog}/>}        
      </header>
    </div>
  );
}


export default App;
