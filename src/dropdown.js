import { useState } from "react";
import { Link } from "react-router-dom";
import Button from 'react-bootstrap/Button';

const Dropdown = () => {
    const [selected, setSelected] = useState('');

    const onHandleChange = (e) => {
        setSelected(e.target.value)
    }
    return (
        <div>
            <div style={{
                textAlign:"center"
            }}>
                <h1>Social Event Detection</h1>
            </div>
            <div style={{display:"flex", paddingLeft:"400px", paddingRight:"400px"}}>
            <div style={{
                display: 'block',
                width: '1000px',
                padding: 30,
                color: 'blue'
            }} >
                <select value={selected} onChange={onHandleChange}>
                    <option>Select the Category</option>
                    <option value="category1">Music</option>
                    <option value="category2">Dance</option>
                    <option value="category3">Webinar</option>
                    <option value="category4">Movies</option>
                    <option value="category5">Standup shows</option>
                </select>
            </div>
            <div style={{
                display: 'block',
                width: 700,
                padding: 30,
                color: 'blue'
            }} >
                <input type="text" placeholder="Enter Location"></input>
            </div>
            </div>
            <br />
            <div style={{display:"block", margin:"auto", paddingLeft:'600px'}}>
            <Button><Link to="/datafile" style={{textDecoration: 'none', alignContent:"center"}}>SUBMIT</Link></Button>
            </div>
        </div>
    )
}

export default Dropdown



