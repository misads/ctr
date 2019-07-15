#### train表
| 字段 | 说明                             |
| --------- | ----------------------------------------------------- |
| label     | 是否点击，1表示点击，0表示未点击                      |
| **uId**(外键) | 用户唯一标识(示例：u100000001)          |
| **adId**(外键) | 广告Id                                     |
| operTime  | 操作时间(精确到毫秒，示例: "2019-04-01 10:45:20:257") |
| siteId    | 媒体Id                                                |
| slotId    | 广告位Id**(可能比较重要)**                                  |
| **contentId**(外键) | 素材Id                                                |
| netType   | 网络连接类型(示例：1, 2, 3, 4, 5, 6)                  |

#### 用户表
| uId       | 匿名化处理后的用户唯一标识(示例：u100000001) |
| --------- | -------------------------------------------- |
| age       | 年龄段(示例：1, 2, 3, 4, 5, 6)               |
| gender    | 性别(示例：1, 2, 3)                          |
| city      | 常住城市编码(示例：1, 2, 3…)                 |
| province  | 常驻省份编码(示例：1, 2, 3…)                 |
| phoneType | 设备型号(示例：1, 2, 3…)                     |
| carrier   | 运营商编号                                   |

#### 广告表
| adId         | 广告Id(示例：2556)                                           |
| ------------ | ------------------------------------------------------------ |
| billId       | 计费类型(示例：cpc, cpm, cpd)                                |
| primId       | 广告主唯一编号Id                                             |
| creativeType | 创意类型(示例：1. 文字广告，2. 图片广告，3. 图文广告，4. gif广告，5. 无具体创意类型) |
| intertype    | 交互类型(示例：0. 无交互，点击无响应，1. 点击后打开网，2. 点击下载应用，3. 点击后打开App) |
| spreadAppId  | 广告对应的appId                                              |

#### 素材表
| contentId   | 素材唯一标识Id                          |
| ----------- | --------------------------------------- |
| firstClass  | 素材内容文本的一级分类(示例：电商)      |
| secondClass | 素材内容文本的二级分类，多值使用‘#’分割 |

|                    |                |            |
| ------------------ | -------------- | ---------- |
| 文件               | 描述           | 数据量     |
| train_20190518.csv | 训练集(有标签) | 984w/1.59e |
| test_20190518.csv  | 测试集(无标签) | 100w       |
| user_info.csv      | 用户资料       |            |
| ad_info.csv        | 广告资料       | 5223       |
| content_info.csv   | 广告媒体资料   |            |

 
