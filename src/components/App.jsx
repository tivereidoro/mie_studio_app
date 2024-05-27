import Stack from 'react-bootstrap/Stack';
import Header from "./header/Header"
import Footer from "./footer/Footer"
import LandingPage from './homepage/LandingPage';
import '../index.css';

export default function App() {
  return (
    <Stack className="App">
      <Header className="p-4" />
      <Footer className="p-2" />
    </Stack>
  )
}
