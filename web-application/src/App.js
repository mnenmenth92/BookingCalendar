import React, { Component } from 'react';

async function getData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'GET', // *GET, POST, PUT, DELETE, etc.
    mode: 'no-cors', // no-cors, *cors, same-origin

  });
  return response.json(); // parses JSON response into native JavaScript objects
}

class App extends Component {
  state = {}

  // componentDidMount() {
  //   const url = 'http://127.0.0.1:5000/users'
  //   const url2 = 'https://randomuser.me/api/'

  //   getData(url)
  //     .then(data => {
  //       console.log(data); // JSON data parsed by `data.json()` call
  //     });


  // }

  render() {
    return (

      <p>Booking Calendar - frontend init</p>

    );
  }
}

export default App;


