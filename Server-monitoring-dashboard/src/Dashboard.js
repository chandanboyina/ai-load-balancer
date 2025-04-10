import React, { useEffect, useState } from 'react';
import ChartComponent from './ChartComponent';
import ServerDropdown from './ServerDropdown';

function Dashboard() {
  const [selectedServer, setSelectedServer] = useState('Server A');
  const [data, setData] = useState([]);

  useEffect(() => {
    // Replace with your backend endpoint
    fetch(`http://localhost:5000/monitor/${selectedServer}`)
      .then(res => res.json())
      .then(json => setData(json))
      .catch(err => console.error('Fetch error:', err));
  }, [selectedServer]);

  return (
    <div>
      <ServerDropdown selected={selectedServer} setSelected={setSelectedServer} />
      <ChartComponent data={data} />
    </div>
  );
}

export default Dashboard;
