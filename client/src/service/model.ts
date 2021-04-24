import axios from "@/utils/axios";

class ModelApi {
  // 获取所有训练模型列表
  async list(page: number, pagesize: number): Promise<any> {
    return axios.get("/api/model", { params: { page, pagesize } });
  }

  // 获取所有可以使用的模型列表
  async validList(): Promise<any> {
    return axios.get("/api/model/valid");
  }

  // 训练一个模型
  async train(name: string, dataset: string, desc: string): Promise<any> {
    return axios.post("/api/model/train", { name, dataset, desc });
  }

  // 使用模型预测
  async apply(id: number, data: string[], k?: number): Promise<any> {
    return axios.post("/api/model/apply", { id, data, k });
  }
}

export default new ModelApi();
