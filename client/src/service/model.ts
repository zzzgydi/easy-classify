import axios from "./index";

// 训练模型
export function apiStartTrain(dataset: string, name: string): Promise<any> {
  return axios.post("/api/train", { dataset, name });
}

// 使用模型预测
export function apiApplyModel(
  name: string,
  data: string[],
  k?: number
): Promise<any> {
  return axios.post("/api/apply", { name, data, k });
}
