import axios from "@/utils/axios";

export interface DatasetModel {
  id: number;
  name: string;
  desc: string;
  updated_time: number;
}

class DatasetApi {
  async list(page: number, pagesize: number): Promise<any> {
    return axios.get("/api/dataset", { params: { page, pagesize } });
  }

  async add(name: string, desc: string) {
    return axios.post("/api/dataset", { name, desc });
  }

  async remove(id: number) {
    return axios.delete("/api/dataset", { params: { id } });
  }

  async update(id: number, name: string, desc: string) {
    return axios.post("/api/dataset/update", { id, name, desc });
  }
}

export default new DatasetApi();
