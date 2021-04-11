import axios from "./index";
import { formatTime } from "../utils";

interface LabelData {
  id?: string | number;
  label: string;
  data: string;
  key?: string;
}

export interface DatasetModel {
  id: number;
  name: string;
  desc: string;
  updated: string;
}

class DatasetApi {
  async list(page: number, pagesize: number): Promise<any> {
    return axios
      .get("/api/dataset", { params: { page, pagesize } })
      .then((res: any) => {
        const result = res.result.map((item: any[]) => ({
          id: item[0],
          name: item[1],
          desc: item[2],
          updated: formatTime(item[3]),
        }));
        return { ...res, result };
      });
  }

  async add(name: string, desc: string) {
    return axios.post("/api/dataset", { name, desc });
  }

  async remove(id: number) {
    return axios.delete("/api/dataset", { params: { id } });
  }

  async update(id: number, name: string, desc: string) {
    return axios.post("/api/dataset", { id, name, desc });
  }
}

export default new DatasetApi();
