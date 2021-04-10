import Axios from "axios";

const axios = Axios.create();

axios.interceptors.response.use((response) => {
  if (response.status === 200) {
    const { code = 500, msg = "未知错误" } = response.data;
    if (code >= 300) return Promise.reject(msg);
    return response.data;
  }

  return Promise.reject(response.status);
});

export default axios;
