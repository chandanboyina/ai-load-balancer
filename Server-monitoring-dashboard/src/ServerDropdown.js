import React from 'react';

function ServerDropdown({ selected, setSelected }) {
  const servers = ['Server A', 'Server B', 'Server C'];

  return (
    <div>
      <label>Choose Server: </label>
      <select value={selected} onChange={(e) => setSelected(e.target.value)}>
        {servers.map((server) => (
          <option key={server} value={server}>
            {server}
          </option>
        ))}
      </select>
    </div>
  );
}

export default ServerDropdown;
