import Stack from 'react-bootstrap/Stack';
import Header from "./header/Header"
import Footer from "./footer/Footer"

export default function App() {
  return (
    <Stack>
      <Header className="p-4" />
      <Footer className="p-2" />
    </Stack>
  )
}
