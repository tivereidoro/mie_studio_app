import axios from "axios";


const axiosInstance = axios.create({
    baseURL: "https://api-miestudio.onrender.com",
    withCredentials: true,
});

export default axiosInstance;
